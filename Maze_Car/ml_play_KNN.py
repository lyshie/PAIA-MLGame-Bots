"""
Author: HSIEH Li-Yi
"""
import random

import numpy as np
import joblib


class MLPlay:
    def __init__(self, player):
        self.player_no = player[6]
        self._model = joblib.load('KNN_model')
        self._classes = ['back', 'forward', 'left', 'right']
        print("Initial ml script")

        self._pwm = {
            'forward': [150, 150],
            'left': [-70, 70],
            'right': [70, -70],
            'back': [-120, -120],
            'none': [50, 50]
        }

    def update(self, scene_info: dict):
        """
        Generate the command according to the received scene information
        """
        frame = scene_info["frame"]
        left = scene_info["L_sensor"]
        front = scene_info["F_sensor"]
        right = scene_info["R_sensor"]

        #if front < 1:
        #    return self.pwm(0 - round(min(right, 50)),
        #                    0 - round(min(left, 50)))

        result = self._model.predict(np.array([[left, front, right]]))[0]
        result = self._classes[result]

        print(result, scene_info)

        pwm_left = round(self._pwm[result][0] + min(right, 50))
        pwm_right = round(self._pwm[result][1] + min(left, 50))

        return self.pwm(pwm_left, pwm_right)

    def pwm(self, left, right):
        return [{"left_PWM": left, "right_PWM": right}]

    def reset(self):
        """
        Reset the status
        """
        print("reset ml script")
        pass
