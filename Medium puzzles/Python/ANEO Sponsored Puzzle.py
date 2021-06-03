import sys
import math

Speeds_data = []
Lights_data = []
speed = int(input())
light_count = int(input())
for i in range(light_count):
    distance, duration = [int(j) for j in input().split()]
    Lights_data.append([distance, duration])
    Speeds_data.append([3.6*distance, 3.6*distance/duration])
    Times_duration = 0
    Lights_data[i].append(Times_duration)
    while 3.6*distance/(duration*(Times_duration + 1)) > speed:
        Times_duration += 2
        if speed > 3.6*distance/(duration*(Times_duration+1)):
            Lights_data[i][2] = Times_duration
            Speeds_data[i] = ([3.6*distance/(duration*Times_duration),  3.6*distance/(duration*(Times_duration+1))])
    else:
        continue

found = False
Max_speed_found = False


def finding_speed(speeding, found):
    true_counter = 0
    for j in range(light_count):
        for k in range(0, len(Speeds_data[j])-1, 2):
            if Speeds_data[j][k] >= speeding > Speeds_data[j][k + 1]:
                true_counter += 1
                if true_counter == light_count:
                    found = True
    return found


while not Max_speed_found:
    for speeding in range(speed, 1, -1):
        Max_speed_found = finding_speed(speeding, found)
        if Max_speed_found is True:
            print(speeding)
            break
        elif Max_speed_found is False:
            for m in range(light_count):
                Lights_data[m][2] += 2
                Speeds_data[m].append((3.6*Lights_data[m][0]/(Lights_data[m][1]*(Lights_data[m][2]))))
                Speeds_data[m].append((3.6*Lights_data[m][0]/(Lights_data[m][1]*(Lights_data[m][2]+1))))
