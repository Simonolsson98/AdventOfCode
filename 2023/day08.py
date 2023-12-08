import os
from math import lcm
import time

def part(part_num):
    with open(os.path.dirname(__file__)+"/day08_input.txt", 'r') as input_text:
        leftright = input_text.readline()[:-1]
        input_text.readline()

        locations = []
        directions = []
        while i := input_text.readline():
            yes = i.split(" = (")
            locations.append(yes[0])
            directions.append((yes[1].split(", ")[0], yes[1].split(", ")[1].replace(")", "")[:-1]))

    result = 0
    if(part_num == "1"):
        current = "AAA"
    else:
        current = [[loc] for loc in locations if loc[2] == "A"]

    saved = leftright
    while(current!=[]):
        if(part_num == "1"):
            for char in leftright:
                current_index = locations.index(current)
                if char == "L":
                    current = directions[current_index][0]
                else: #char == "R"
                    current = directions[current_index][1]
                result += 1
            if(current == "ZZZ"):
                break
        else:
            loops = []
            for i, curr in enumerate(current):
                for char in leftright:
                    current_index = locations.index(curr[-1])
                    if char == 'L':
                        new_current = directions[current_index][0]
                    elif char == 'R':
                        new_current = directions[current_index][1]
                    if(new_current.endswith('Z')):
                        loopsize = len(current[i])
                        loops.append(loopsize)
                        current.remove(current[i])
                        break
                    else:
                        current[i].append(new_current)

    if(part_num == "1"):
        return result
    elif(part_num == "2"):
        result = 1
        for loop in loops:
            result = lcm(loop, result)
        return result

start = time.time()
result = part("1")
print(f"day8: Python solution for part 1: {result}, time: {round(time.time() - start, 3)} s")

start = time.time()
result = part("2")
print(f"day8: Python solution for part 2: {result}, time: {round(time.time() - start, 3)} s")
