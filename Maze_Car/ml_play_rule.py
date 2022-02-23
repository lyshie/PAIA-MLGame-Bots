class MLPlay:
    def __init__(self, player):
        self.player_no = player[6]

        self.left = 0
        self.left_front = 0
        self.front = 0
        self.right_front = 0
        self.right = 0

        print("Initial ml script")

    def motor(self, left=0, right=0):
        ''' 回傳左右輪轉速 '''
        return [{"left_PWM": left, "right_PWM": right}]

    def update(self, scene_info: dict):
        """
        Generate the command according to the received scene information
        """
        self.left = scene_info["L_sensor"]
        self.left_front = scene_info["L_T_sensor"]
        self.front = scene_info["F_sensor"]
        self.right_front = scene_info["R_T_sensor"]
        self.right = scene_info["R_sensor"]
        ''' -1
        '''
        if self.front < 0:
            return self.motor(255, 255)

        if self.left_front <= 5.656 and self.front <= 4:    ''' 遇到圍牆轉角 '''
            return self.motor(255, -65)
        elif self.left > 1 and self.left_front > 1.414:     ''' 未靠左邊 '''
            return self.motor(225, 255)
        elif self.left <= 0 and self.left_front > 2.828:    ''' 遇到路口轉角 '''
            return self.motor(-145, 255)
        elif self.front <= 0:                               ''' 卡住脫困 '''
            self.motor(-135, 255)
        else:
            return self.motor(255, 255)

    def reset(self):
        """
        Reset the status
        """
        print("reset ml script")
        pass
