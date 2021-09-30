"""
Author: HSIEH Li-Yi
"""

import random


class MLPlay:
    def __init__(self):
        """
        Constructor
        """
        self.ball_served = False
        self.prev_ball = {"x": 0, "y": 0}
        self.prev_command = "NONE"

    def update(self, scene_info):
        """
        Generate the command according to the received `scene_info`.
        """
        # Make the caller to invoke `reset()` for the next round.
        status = scene_info["status"]
        if status == "GAME_OVER" or status == "GAME_PASS":
            #pass
            return "RESET"

        if not self.ball_served:
            self.ball_served = True
            command = random.choice(["SERVE_TO_LEFT", "SERVE_TO_RIGHT"])
            return command
        #else:
        #    command = random.choice(["NONE", "MOVE_LEFT", "MOVE_RIGHT"])

        if status == "GAME_ALIVE":
            frame = scene_info["frame"]
            ball = {"x": scene_info["ball"][0], "y": scene_info["ball"][1]}
            platform = {
                "x": scene_info["platform"][0],
                "y": scene_info["platform"][1]
            }

            px = self.predict_x(ball, self.prev_ball)

            if px > platform["x"]:
                command = "MOVE_RIGHT"
            else:
                command = "MOVE_LEFT"

            #print(frame, ball, px, platform["x"], status)

            # store previous position of ball
            self.prev_ball = ball
            self.prev_command = command

        return command

    def predict_x(self, ball, prev_ball):
        y = ball["y"]
        x = ball["x"]

        delta_x = ball["x"] - prev_ball["x"]
        delta_y = ball["y"] - prev_ball["y"]
        '''
        x = ball["x"] + ((395 - y) / (delta_y + 0.000001)) * delta_x
        x = abs(x) % 200
        '''
        while y < 393 and delta_y > 0:
            x += delta_x
            y += delta_y
            if x < 7:
                delta_x = 0 - delta_x
            elif x > 193:
                delta_x = 0 - delta_x

        if random.choice([1, 5]) == 1:
            return x - random.randint(-20, 10)
        else:
            return x - random.randint(10, 20)

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
