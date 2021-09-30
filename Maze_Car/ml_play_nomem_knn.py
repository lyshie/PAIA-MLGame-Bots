"""
Author: HSIEH Li-Yi
"""
import random
from collections import deque

import numpy as np
import joblib


class MLPlay:
    def __init__(self, player):
        self.player_no = player[6]

        self._pwm_left = 100
        self._pwm_right = 100

        self._size = 10

        self._left = deque([0] * self._size, self._size)
        self._front = deque([10] * self._size, self._size)
        self._right = deque([0] * self._size, self._size)

        self._model = joblib.load('KNN_model')
        self._scaler = joblib.load('KNN_scaler')
        self._classes = joblib.load('KNN_classes')

        print("Initial ml script")

    def smooth(self, val, bucket):
        if val >= 0:
            bucket.append(val)

        y = sorted(bucket)
        n = 3
        y = y[3:self._size - n]

        return sum(y) / len(y)

    def update(self, scene_info: dict):
        """
        Generate the command according to the received scene information
        """
        frame = scene_info["frame"]
        left = scene_info["L_sensor"]
        front = scene_info["F_sensor"]
        right = scene_info["R_sensor"]

        if frame < 10:
            return self.pwm(0, 0)
        '''
        store smooth ultrasonic sensor value
        '''
        smooth_left = 0
        smooth_front = 0
        smooth_right = 0
        '''
        default 100
        '''
        pwm_left = self._pwm_left
        pwm_right = self._pwm_right

        smooth_left = round(self.smooth(left, self._left))
        smooth_front = round(self.smooth(front, self._front))
        smooth_right = round(self.smooth(right, self._right))

        x = np.array([[smooth_left, smooth_front, smooth_right]])
        x_normal = self._scaler.transform(x)
        print(x, x_normal)

        result = self._model.predict(x_normal)[0]
        result = self._classes[result]

        if smooth_front < 1:
            if smooth_left > smooth_right:
                pwm_left = 0 - pwm_left
                pwm_right = pwm_right
            else:
                pwm_left = pwm_left
                pwm_right = 0 - pwm_right
        else:
            if smooth_left < smooth_right:
                pwm_left -= 10
                pwm_right += 10
            elif smooth_left > smooth_right:
                pwm_left += 10
                pwm_right -= 10
            else:
                pass

        print("%6s L=%6s[%3s](%3s) F=%6s[%3s] R=%6s[%3s](%3s)" %
              (frame, left, smooth_left, pwm_left, front, smooth_front, right,
               smooth_right, pwm_right))

        return self.pwm(pwm_left, pwm_right)

    def pwm(self, left, right):
        return [{"left_PWM": left, "right_PWM": right}]

    def reset(self):
        """
        Reset the status
        """
        print("reset ml script")
        pass
