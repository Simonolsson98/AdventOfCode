import os
import math
import time

def part(part_num):
    arr=[]
    with open(os.path.dirname(__file__)+"/day12_input.txt", 'r') as input_text:
        pass

    if part_num == "1":
        print(f"day12: Python solution for part 1: {result}, time: {round(time.time() - start, 3)} s")
    elif part_num == "2":
        print(f"day12: Python solution for part 2: {result}, time: {round(time.time() - start, 3)} s")

start = time.time()
part("1")
start = time.time()
part("2")