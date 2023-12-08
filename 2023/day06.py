import os
import math
import time

def part(part_num):
    with open(os.path.dirname(__file__)+"/day06_input.txt", 'r') as input_text:
        lines = input_text.readlines()
        if(part_num == "1"):
            racetimes = ' '.join(lines[0].split(":")[1].split()).split(" ")
            racedistances= ' '.join(lines[1].split(":")[1].split()).split(" ")
            winning_times = [0 for i in range(len(racetimes))]
            
            for index, (race_time, race_dist) in enumerate(zip(racetimes, racedistances)):
                speed = 0
                for i in range(int(race_time)):
                    speed = i
                    traveltime = int(race_time) - i
                    dist_travelled = speed * traveltime
                    if(dist_travelled > int(race_dist)):
                        winning_times[index] += 1
        else:
            racetime = int(''.join(lines[0].split(":")[1].split()))
            racedistance = int(''.join(lines[1].split(":")[1].split()))
            number_of_winning_times = 0
            
            for i in range(racetime):
                speed = i
                traveltime = racetime - i
                dist_travelled = speed * traveltime
                if(dist_travelled > racedistance):
                    number_of_winning_times += 1

    if part_num == "1":
        print(f"day6: Python solution for part 1: {math.prod(winning_times)}, time: {time.time() - start} s")
    elif part_num == "2":
        print(f"day6: Python solution for part 2: {number_of_winning_times}, time: {time.time() - start} s")

start = time.time()
part("1")
start = time.time()
part("2")