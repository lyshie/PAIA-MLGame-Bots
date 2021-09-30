"""
Author: HSIEH Li-Yi
"""
import random

import numpy as np
import joblib


class MLPlay:
    def __init__(self, player):
        self.player_no = player[6]
        self._pwm_left = 100
        self._pwm_right = 100

        print("Initial ml script")

    def update(self, scene_info: dict):
        """
        Generate the command according to the received scene information
        """
        frame = scene_info["frame"]
        left = scene_info["L_sensor"]
        front = scene_info["F_sensor"]
        right = scene_info["R_sensor"]

        pwm_left = self._pwm_left + random.randint(-1, 1)
        pwm_right = self._pwm_right + random.randint(-1, 1)

        if front < 0:
            '''
            -1 stop
            '''
            pwm_left = 0
            pwm_right = 0
        elif front < left and front < right:
            if abs(left - right) > 5:
                if left > right:
                    pwm_left = -100
                    pwm_right = 100
                else:
                    pwm_left = 100
                    pwm_right = -100
            else:
                pwm_left = 0 - pwm_left + random.randint(-3, 3)
                pwm_right = 0 - pwm_right + random.randint(-3, 3)

        print("%6s L=%6s[%3s] F=%6s R=%6s[%3s]" %
              (frame, left, pwm_left, front, right, pwm_right))

        return self.pwm(pwm_left, pwm_right)

    def pwm(self, left, right):
        return [{"left_PWM": left, "right_PWM": right}]

    def reset(self):
        """
        Reset the status
        """
        print("reset ml script")
        pass
