"""
Author: HSIEH Li-Yi
"""
import random

import numpy as np
import joblib


class MLPlay:
    def __init__(self, player):
        self.player_no = player[6]
        self._model = joblib.load('LSVC_model')
        print("Initial ml script")

        self._pwm = {
            'forward': [100, 100],
            'left': [0, 100],
            'right': [100, 0],
            'back': [-100, -100],
            'none': [50, 50]
        }

    def update(self, scene_info: dict):
        """
        Generate the command according to the received scene information
        """
        print(scene_info)
        frame = scene_info["frame"]
        right = scene_info["R_sensor"]
        left = scene_info["L_sensor"]
        front = scene_info["F_sensor"]

        #if front < 3:
        #    return self.pwm(random.randint(-5, -1), random.randint(-5, -1))

        result = self._model.predict(np.array([[right, left, front]]))[0]
        print(result)

        pwm_left = self._pwm[result][0] + random.randint(-5, 5)
        pwm_right = self._pwm[result][1] + random.randint(-5, 5)

        return self.pwm(pwm_left, pwm_right)

    def pwm(self, left, right):
        return [{"left_PWM": left, "right_PWM": right}]

    def reset(self):
        """
        Reset the status
        """
        print("reset ml script")
        pass
