"""
Author: HSIEH Li-Yi
"""
import random

import numpy as np
import joblib


class MLPlay:
    def __init__(self, player):
        self.player_no = player[6]
        self._model = joblib.load('LR_model')
        print("Initial ml script")

    def update(self, scene_info: dict):
        """
        Generate the command according to the received scene information
        """
        print(scene_info)
        frame = scene_info["frame"]
        right = scene_info["R_sensor"]
        left = scene_info["L_sensor"]
        front = scene_info["F_sensor"]

        result = self._model.predict(np.array([[right, left, front]]))
        print(result)

        return self.pwm(result[0][0], result[0][1])

    def pwm(self, left, right):
        return [{"left_PWM": left, "right_PWM": right}]

    def reset(self):
        """
        Reset the status
        """
        print("reset ml script")
        pass
