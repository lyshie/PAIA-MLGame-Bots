import pickle
import sys
import csv

files = sys.argv[1:]

all_data = []
for f in files:
    with open(f, "rb") as f:
        p = pickle.load(f)

        data = []
        for line in zip(p['ml_1P']['scene_info'], p['ml_1P']['command']):
            if line[0] and line[1]:
                row = [
                    line[0]['L_T_sensor'],
                    line[0]['L_sensor'],
                    line[0]['F_sensor'],
                    line[0]['R_sensor'],
                    line[0]['R_T_sensor'],
                    line[1][0]['left_PWM'],
                    line[1][0]['right_PWM'],
                ]
                data.append(row)
                #print(row)

            if line[0]['status'] == 'GAME_PASS':
                print(f.name)
                all_data.extend(data)

with open('all.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(all_data)
