import pickle
import json
import sys


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
        ''' pwm info
        '''
        p1_cmds = raw_data['ml_1P']['command']
        ''' sensors info
        '''
        frames = raw_data['ml_1P']['scene_info']

        for a, b in zip(p1_cmds, frames):
            if a is not None:
                '''
                    direction
                '''
                if a[0]['left_PWM'] > a[0]['right_PWM']:  # Oo
                    direction = 'right'
                elif a[0]['left_PWM'] < a[0]['right_PWM']:  # oO
                    direction = 'left'
                else:  # equal pwm
                    if a[0]['left_PWM'] < 0 and a[0]['right_PWM'] < 0:  # vv
                        direction = 'back'
                    elif a[0]['left_PWM'] > 0 and a[0]['right_PWM'] > 0:  # ^^
                        direction = 'forward'
                    else:
                        direction = 'none'
                '''
                    direction and sensor >= 0
                    only store positive data
                '''
                if direction != 'none' and b['L_sensor'] >= 0 and b[
                        'F_sensor'] >= 0 and b['R_sensor'] >= 0:
                    data.append({
                        'direction': direction,
                        'left_PWM': a[0]['left_PWM'],
                        'right_PWM': a[0]['right_PWM'],
                        'L_sensor': b['L_sensor'],
                        'F_sensor': b['F_sensor'],
                        'R_sensor': b['R_sensor'],
                    })

    print(json.dumps(data))


if __name__ == "__main__":
    main()
