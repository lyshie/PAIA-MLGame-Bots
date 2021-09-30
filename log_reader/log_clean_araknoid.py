import pickle
import sys
import os


def main():
    ''' log files
    '''
    log_files = sys.argv[1:]
    ''' final data
    '''
    data = []

    raw_data = []
    for f in log_files:
        #print("Processing file %s" % (f, ))
        with open(f, 'rb') as fp:
            raw_data = pickle.load(fp)

            rows = raw_data['ml']['scene_info']

            total = len(rows[0]['bricks'])
            remained = len(rows[-1]['bricks'])

            if rows[-1]['status'] == 'GAME_PASS':
                pass
            #elif rows[-1]['status'] == 'GAME_OVER' and remained / total < 0.1:
            #    pass
            else:
                os.remove(f)
                print("%s has been removed." % (f, ))


if __name__ == "__main__":
    main()
