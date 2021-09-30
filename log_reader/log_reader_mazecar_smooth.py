import pickle
import json
import sys
from collections import deque


class Smoother():
    """ 平滑數據 """
    _size = 10  # 取樣區間大小
    _left = deque([0] * _size, _size)
    _front = deque([0] * _size, _size)
    _right = deque([0] * _size, _size)
    _warmed = False

    def __init__(self, size=10):
        self._size = size

    @property
    def warmed(self):
        """ 取得是否暖機了 """
        return self._warmed

    def warm(self, left=0, front=0, right=0):
        self._warmed = True
        """ 預先填入相同數值，平均後不變 """
        self._left = deque([left] * self._size, self._size)
        self._front = deque([front] * self._size, self._size)
        self._right = deque([right] * self._size, self._size)

    def smooth(self, val=0, bucket=[]):
        if val >= 0:
            bucket.append(val)

        y = sorted(bucket)  # 排出順序，篩掉極大、極小值
        n = 3
        y = y[n:self._size - n]  # 前、後各三個極端值不要

        return sum(y) / len(y)  # 取平均值


def main():
    """ 接受所有檔案名稱透過參數讀入 """
    log_files = sys.argv[1:]
    """ 最後要輸出 JSON 的資料 """
    data = []

    raw_data = []
    for f in log_files:
        with open(f, 'rb') as fp:
            raw_data = pickle.load(fp)
        """
            PWM 數據 => left_PWM, right_PWM
        """
        p1_cmds = raw_data['ml_1P']['command']
        """
            超音波數據 => L_sensor, F_sensor, R_sensor
        """
        frames = raw_data['ml_1P']['scene_info']
        """
            平滑
        """
        smoother = Smoother(8)

        for a, b in zip(p1_cmds, frames):
            #print(b['L_sensor'], b['F_sensor'], b['R_sensor'])
            if a is not None:
                if smoother.warmed:
                    pass
                else:
                    if b['F_sensor'] > 0:
                        smoother.warm(b['L_sensor'], b['F_sensor'],
                                      b['R_sensor'])
                    else:
                        #print(b['L_sensor'], b['F_sensor'], b['R_sensor'],  'not-warmed')
                        continue
                        pass
                """
                    依據左右 PWM，判斷動作方向
                """
                #print(b['L_sensor'], b['F_sensor'], b['R_sensor'], 'warmed')
                if a[0]['left_PWM'] > a[0]['right_PWM']:  # Oo
                    direction = 'right'
                elif a[0]['left_PWM'] < a[0]['right_PWM']:  # oO
                    direction = 'left'
                else:  # equal pwm
                    if a[0]['left_PWM'] < 0 and a[0]['right_PWM'] < 0:  # vv
                        direction = 'back'
                    elif a[0]['left_PWM'] > 0 and a[0]['right_PWM'] > 0:  # ^^
                        direction = 'forward'
                    else:
                        direction = 'none'
                """
                    處理超音波感應器數據 / 平滑化
                    direction != 'none' AND all sensors >= 0
                    Only store positive data
                """
                smooth_left = smoother.smooth(b['L_sensor'], smoother._left)
                smooth_front = smoother.smooth(b['F_sensor'], smoother._front)
                smooth_right = smoother.smooth(b['R_sensor'], smoother._right)
                if direction != 'none' and b['L_sensor'] >= 0 and b[
                        'F_sensor'] >= 0 and b['R_sensor'] >= 0:
                    data.append({
                        'direction': direction,
                        'left_PWM': a[0]['left_PWM'],
                        'right_PWM': a[0]['right_PWM'],
                        'smooth_left': smooth_left,
                        'smooth_front': smooth_front,
                        'smooth_right': smooth_right,
                        'L_sensor': b['L_sensor'],
                        'F_sensor': b['F_sensor'],
                        'R_sensor': b['R_sensor'],
                    })
                """
                print("L=%6s[%3s] F=%6s[%3s] R=%6s[%3s]" %
                      (b['L_sensor'], smooth_left, b['F_sensor'], smooth_front,
                       b['R_sensor'], smooth_right))
                """

    print(json.dumps(data))  # 最後輸出 JSON 格式


if __name__ == "__main__":
    main()
