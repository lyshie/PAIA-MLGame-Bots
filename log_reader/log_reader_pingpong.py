import pickle
import sys
import re

CMD_MAP = {'NONE': 0, 'MOVE_RIGHT': 1, 'MOVE_LEFT': 2, 'MOVE_NONE': 0}


def main():
    ''' log files
    '''
    log_files = sys.argv[1:]
    ''' final data
    '''
    print('ball_x',
          'ball_y',
          'speed_x',
          'speed_y',
          '1p_x',
          '1p_y',
          '2p_x',
          '2p_y',
          'command',
          sep=", ")

    raw_data = []
    for f in log_files:
        with open(f, 'rb') as fp:
            raw_data = pickle.load(fp)

        for s, c in zip(raw_data['ml_1P']['scene_info'],
                        raw_data['ml_1P']['command']):
            if c and (c not in ['NONE', 'MOVE_NONE'
                                ]) and s['ball_speed'][1] > 0:
                print(s['ball'][0],
                      s['ball'][1],
                      s['ball_speed'][0],
                      s['ball_speed'][1],
                      s['platform_1P'][0],
                      s['platform_1P'][1],
                      s['platform_2P'][0],
                      s['platform_2P'][1],
                      CMD_MAP[c],
                      sep=", ")


if __name__ == "__main__":
    main()
