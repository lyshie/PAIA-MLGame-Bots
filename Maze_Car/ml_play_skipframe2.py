"""
Author: HSIEH Li-Yi
"""
import random


class MLPlay:
    def __init__(self, player):
        self.player_no = player[6]
        self._last_command = self.pwm(1, 1)
        self._last_sensors = {'R': 0, 'L': 0, 'F': 0}
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

        if frame % 3 != 1:
            return self._last_command

        p = random.randint(100, 130)
        a = random.randint(0, 2)
        b = random.randint(0, 2)
        pwm_left = 0
        pwm_right = 0

        #if front > 0 and right > 0 and left > 0:
        '''
        if (front > right) and (front > left):
            pwm_left = 255
            pwm_right = 255
        elif (left > front) and (left > right):
            pwm_left = 0 - p
            pwm_right = p
        elif (right > front) and (right > left):
            pwm_left = p
            pwm_right = 0 - p
        else:
            pwm_left = 0 - (p + 30)
            pwm_right = 0 - (p + 30)
        '''
        if front < 2:
            pwm_left = 0 - p / 3 + a
            pwm_right = 0 - p / 3 + b
        elif (front > right) and (front > left):
            pwm_left = p + a
            pwm_right = p + b
        elif (left > front) and (left > right):
            pwm_left = 0 - p / 2 + a
            pwm_right = p / 2 + b
        elif (right > front) and (right > left):
            pwm_left = p / 2 + a
            pwm_right = 0 - p / 2 + b
        #else:
        #    pwm_left = random.randint(-5, 5)
        #    pwm_right = random.randint(-5, 5)

        command = self.pwm(pwm_left, pwm_right)
        print(command)
        self._last_command = command

        return command

    def pwm(self, left, right):
        return [{"left_PWM": left, "right_PWM": right}]

    def reset(self):
        """
        Reset the status
        """
        print("reset ml script")
        pass
