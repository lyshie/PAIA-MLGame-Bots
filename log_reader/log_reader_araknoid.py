import pickle
import json
import sys
import re
import pandas as pd


def main():
    ''' log files
    '''
    log_files = sys.argv[1:]
    ''' final data
    '''
    data = []

    raw_data = []
    for f in log_files:
        with open(f, 'rb') as fp:
            raw_data = pickle.load(fp)

        partial = []

        last_x = raw_data['ml']['scene_info'][0]['ball'][0]
        last_y = raw_data['ml']['scene_info'][0]['ball'][1]

        last_x2 = raw_data['ml']['scene_info'][0]['ball'][0]
        last_y2 = raw_data['ml']['scene_info'][0]['ball'][1]

        for s, c in zip(raw_data['ml']['scene_info'],
                        raw_data['ml']['command']):

            s['command'] = c
            s['ball_x'], s['ball_y'] = s['ball'][0], s['ball'][1]
            s['platform_x'], s['platform_y'] = s['platform'][0], s['platform'][
                1]
            ''' direction of ball
                last_x ---> x
                last_y ---> y
            '''
            s['dir_x'] = s['ball_x'] - last_x
            s['dir_y'] = s['ball_y'] - last_y

            s['dir_x2'] = last_x - last_x2
            s['dir_y2'] = last_y - last_y2

            last_x2 = last_x
            last_y2 = last_y

            last_x = s['ball_x']
            last_y = s['ball_y']

            if s['command'] and 'SERVE' not in s['command'] and s[
                    'status'] == 'GAME_ALIVE':
                # do not append 'SERVE_TO_LEFT', 'SERVE_TO_RIGHT'
                partial.append(s)
            elif s['status'] == 'GAME_PASS':
                # only save GAME_PASS
                data.extend(partial)
                partial = []

    #dfs = pd.DataFrame(data=data)
    print(json.dumps(data))


if __name__ == "__main__":
    main()
