import pickle
import os
from numbers import Number

_E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F = None
_E7_90_83X_E9_80_9F_E5_BA_A6 = None
_E7_90_83Y_E9_80_9F_E5_BA_A6 = None
_E7_90_83X_E4_BD_8D_E7_BD_AE = None
_E7_90_83Y_E4_BD_8D_E7_BD_AE = None
_E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83 = None
x = None
_E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_991P = None
y = None
_E7_A7_BB_E5_8B_95_E7_B5_90_E6_9E_9C1P = None
_E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_992P = None
_E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8 = None
_E7_A7_BB_E5_8B_95_E7_B5_90_E6_9E_9C2P = None

# 描述此函式...
def _E9_A0_90_E6_B8_ACX_E4_BD_8D_E7_BD_AE(_E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F, _E7_90_83X_E9_80_9F_E5_BA_A6, _E7_90_83Y_E9_80_9F_E5_BA_A6, _E7_90_83X_E4_BD_8D_E7_BD_AE, _E7_90_83Y_E4_BD_8D_E7_BD_AE):
    global _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83, x, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_991P, y, _E7_A7_BB_E5_8B_95_E7_B5_90_E6_9E_9C1P, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_992P, _E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8, _E7_A7_BB_E5_8B_95_E7_B5_90_E6_9E_9C2P
    x = 0
    y = 0
    if _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F == '1P':
        if _E7_90_83Y_E9_80_9F_E5_BA_A6 > 0:
            x = _E7_90_83X_E4_BD_8D_E7_BD_AE
            y = _E7_90_83Y_E4_BD_8D_E7_BD_AE
            while y < 415:
                x = (x if isinstance(x, Number) else 0) + _E7_90_83X_E9_80_9F_E5_BA_A6
                y = (y if isinstance(y, Number) else 0) + _E7_90_83Y_E9_80_9F_E5_BA_A6
                if x > 195:
                    x = 195
                    _E7_90_83X_E9_80_9F_E5_BA_A6 = 0 - _E7_90_83X_E9_80_9F_E5_BA_A6
                if x < 0:
                    x = 0
                    _E7_90_83X_E9_80_9F_E5_BA_A6 = 0 - _E7_90_83X_E9_80_9F_E5_BA_A6
            return x - 20
        else:
            return 80
    if _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F == '2P':
        if _E7_90_83Y_E9_80_9F_E5_BA_A6 < 0:
            x = _E7_90_83X_E4_BD_8D_E7_BD_AE
            y = _E7_90_83Y_E4_BD_8D_E7_BD_AE
            while y > 80:
                x = (x if isinstance(x, Number) else 0) + _E7_90_83X_E9_80_9F_E5_BA_A6
                y = (y if isinstance(y, Number) else 0) + _E7_90_83Y_E9_80_9F_E5_BA_A6
                if x > 195:
                    x = 195
                    _E7_90_83X_E9_80_9F_E5_BA_A6 = 0 - _E7_90_83X_E9_80_9F_E5_BA_A6
                if x < 0:
                    x = 0
                    _E7_90_83X_E9_80_9F_E5_BA_A6 = 0 - _E7_90_83X_E9_80_9F_E5_BA_A6
            return x - 20
        else:
            return 80
    return x


class MLPlay:
    def __init__(self, side):
        global _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F, _E7_90_83X_E9_80_9F_E5_BA_A6, _E7_90_83Y_E9_80_9F_E5_BA_A6, _E7_90_83X_E4_BD_8D_E7_BD_AE, _E7_90_83Y_E4_BD_8D_E7_BD_AE, _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83, x, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_991P, y, _E7_A7_BB_E5_8B_95_E7_B5_90_E6_9E_9C1P, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_992P, _E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8, _E7_A7_BB_E5_8B_95_E7_B5_90_E6_9E_9C2P
        _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83 = False
        _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F = side
        _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_991P = []
        _E7_A7_BB_E5_8B_95_E7_B5_90_E6_9E_9C1P = []
        _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_992P = []
        _E7_A7_BB_E5_8B_95_E7_B5_90_E6_9E_9C2P = []
        # 請務必自行修改數字，避免覆蓋原來的資料喔!
        _E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8 = 1
    def update(self, scene_info):
        global _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F, _E7_90_83X_E9_80_9F_E5_BA_A6, _E7_90_83Y_E9_80_9F_E5_BA_A6, _E7_90_83X_E4_BD_8D_E7_BD_AE, _E7_90_83Y_E4_BD_8D_E7_BD_AE, _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83, x, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_991P, y, _E7_A7_BB_E5_8B_95_E7_B5_90_E6_9E_9C1P, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_992P, _E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8, _E7_A7_BB_E5_8B_95_E7_B5_90_E6_9E_9C2P
        # 收集玩家1P的資料
        if _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F == '1P':
            # 收集的資料也可以改成，只收集1P勝利或平手喔!
            if scene_info['status'] != "GAME_ALIVE":
                with open(os.path.join(os.path.dirname(__file__), 'feature_1P' + str(_E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8) + '.pickle'), 'wb') as f:
                    pickle.dump(_E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_991P, f)
                with open(os.path.join(os.path.dirname(__file__), 'target_1P' + str(_E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8) + '.pickle'), 'wb') as f:
                    pickle.dump(_E7_A7_BB_E5_8B_95_E7_B5_90_E6_9E_9C1P, f)
                return "RESET"
            if not _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83:
                _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83 = True
                return "SERVE_TO_LEFT"
            else:
                if _E9_A0_90_E6_B8_ACX_E4_BD_8D_E7_BD_AE(_E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F, scene_info['ball_speed'][0], scene_info['ball_speed'][1], scene_info['ball'][0], scene_info['ball'][1]) > scene_info['platform_1P'][0]:
                    _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_991P.append([scene_info['ball_speed'][0], scene_info['ball_speed'][1], scene_info['ball'][0], scene_info['ball'][1], scene_info['platform_1P'][0]])
                    _E7_A7_BB_E5_8B_95_E7_B5_90_E6_9E_9C1P.append(1)
                    return "MOVE_RIGHT"
                else:
                    _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_991P.append([scene_info['ball_speed'][0], scene_info['ball_speed'][1], scene_info['ball'][0], scene_info['ball'][1], scene_info['platform_1P'][0]])
                    _E7_A7_BB_E5_8B_95_E7_B5_90_E6_9E_9C1P.append(2)
                    return "MOVE_LEFT"
        else:
            # 收集玩家2P的資料
            if scene_info['status'] != "GAME_ALIVE":
                with open(os.path.join(os.path.dirname(__file__), 'feature_2P' + str(_E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8) + '.pickle'), 'wb') as f:
                    pickle.dump(_E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_992P, f)
                with open(os.path.join(os.path.dirname(__file__), 'target_2P' + str(_E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8) + '.pickle'), 'wb') as f:
                    pickle.dump(_E7_A7_BB_E5_8B_95_E7_B5_90_E6_9E_9C2P, f)
                return "RESET"
            if not _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83:
                _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83 = True
                return "SERVE_TO_RIGHT"
            else:
                if _E9_A0_90_E6_B8_ACX_E4_BD_8D_E7_BD_AE(_E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F, scene_info['ball_speed'][0], scene_info['ball_speed'][1], scene_info['ball'][0], scene_info['ball'][1]) > scene_info['platform_2P'][0]:
                    _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_992P.append([scene_info['ball_speed'][0], scene_info['ball_speed'][1], scene_info['ball'][0], scene_info['ball'][1], scene_info['platform_2P'][0]])
                    _E7_A7_BB_E5_8B_95_E7_B5_90_E6_9E_9C2P.append(1)
                    return "MOVE_RIGHT"
                else:
                    _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_992P.append([scene_info['ball_speed'][0], scene_info['ball_speed'][1], scene_info['ball'][0], scene_info['ball'][1], scene_info['platform_2P'][0]])
                    _E7_A7_BB_E5_8B_95_E7_B5_90_E6_9E_9C2P.append(2)
                    return "MOVE_LEFT"
    def reset(self):
        global _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F, _E7_90_83X_E9_80_9F_E5_BA_A6, _E7_90_83Y_E9_80_9F_E5_BA_A6, _E7_90_83X_E4_BD_8D_E7_BD_AE, _E7_90_83Y_E4_BD_8D_E7_BD_AE, _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83, x, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_991P, y, _E7_A7_BB_E5_8B_95_E7_B5_90_E6_9E_9C1P, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_992P, _E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8, _E7_A7_BB_E5_8B_95_E7_B5_90_E6_9E_9C2P
        _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83 = False
        _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_991P = []
        _E7_A7_BB_E5_8B_95_E7_B5_90_E6_9E_9C1P = []
        _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_992P = []
        _E7_A7_BB_E5_8B_95_E7_B5_90_E6_9E_9C2P = []
        # 每一次遊戲都會自動加1，讓資料檔案不會被覆蓋
        _E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8 = (_E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8 if isinstance(_E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8, Number) else 0) + 1
