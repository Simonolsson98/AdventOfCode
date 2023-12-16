import os
import math
import time

def part(part_num):
    with open(os.path.dirname(__file__)+"/day17_input.txt", 'r') as input_text:
        for line in input_text:
            pass

    if(part_num == "1"):
        pass
    else:
        pass

start = time.time()
print(f"day17: Python solution for part 1: {part('1')}, time: {round(time.time() - start, 4)} s")

start = time.time()
print(f"day17: Python solution for part 2: {part('2')}, time: {round(time.time() - start, 4)} s")
