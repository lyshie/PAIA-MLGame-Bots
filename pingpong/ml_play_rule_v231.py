"""
Author: HSIEH Li-Yi
"""

import random


class MLPlay:

    def __init__(self, ai_name, *args, **kwargs):
        """
        Constructor

        @param side A string "1P" or "2P" indicates that the `MLPlay` is used by
               which side.
        """
        self.ball_served = False
        self.side = ai_name
        self.has_blocker = False

    def update(self, scene_info, keyboard=[], *args, **kwargs):
        """
        Generate the command according to the received scene information
        """
        if scene_info["status"] != "GAME_ALIVE":
            return "RESET"

        if not self.ball_served:
            if 'blocker' in scene_info:
                self.has_blocker = True

            self.ball_served = True
            # 隨機選擇發球方向
            #return "SERVE_TO_RIGHT"
            return random.choice(["SERVE_TO_RIGHT", "SERVE_TO_LEFT"])
        else:
            # 球的位置
            ball = {'x': scene_info['ball'][0], 'y': scene_info['ball'][1]}

            # 球目前的速度
            speed = {
                'x': scene_info['ball_speed'][0],
                'y': scene_info['ball_speed'][1]
            }

            # 平台的位置
            platform = {
                'x': scene_info['platform_' + self.side][0],
                'y': scene_info['platform_' + self.side][1],
            }

            # 透過球速(方向)預測 X 在平台上的位置
            x = self.predict_x(speed=speed, ball=ball)
            #print(self.side, x, ball)
            '''
              o
                 <---       向左移
                       o
                 --->       向右移
            '''
            if abs(x - platform['x']) >= 1:
                if x > platform['x']:
                    return "MOVE_RIGHT"
                elif x < platform['x']:
                    return "MOVE_LEFT"
            else:
                return "MOVE_NONE"

    def predict_x(self, speed, ball):
        """
        predict the final X position on platform
        """

        delta_x = speed['x']
        delta_y = speed['y']

        # TODO: 精確計算剩餘位置，依據 Y=80 或 Y=420
        if self.side == '1P':
            if delta_y > 0:
                y = ball['y']
                x = ball['x']
                while y <= 415:
                    x += delta_x
                    y += delta_y
                    if x > 195:  # rightmost
                        x = 195
                        delta_x = 0 - delta_x
                    elif x < 0:  # leftmost
                        x = 0
                        delta_x = 0 - delta_x

                # 加上剩餘的差異
                return x - 20 + int((415 - y) * (delta_x / delta_y))
            else:
                # 跟著球走才來得及反應
                if self.has_blocker:
                    return 80
                else:
                    return 80
                    #return ball['x']
        elif self.side == '2P':
            if delta_y < 0:
                y = ball['y']
                x = ball['x']
                while y >= 80:
                    x += delta_x
                    y += delta_y
                    if x > 195:  # rightmost
                        x = 195
                        delta_x = 0 - delta_x
                    elif x < 0:  # leftmost
                        x = 0
                        delta_x = 0 - delta_x

                # 加上剩餘的差異
                return x - 20 + int((80 - y) * (delta_x / delta_y))
            else:
                # 跟著球走才來得及反應
                if self.has_blocker:
                    return 80
                else:
                    return 80
                    #return ball['x']

    def reset(self):
        """
        Reset the status
        """
        print("reset " + self.side)
        self.ball_served = False
