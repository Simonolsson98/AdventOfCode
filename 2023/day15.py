import os
import time

def part(part_num):
    result = 0
    with open(os.path.dirname(__file__)+"/day15_input.txt", 'r') as input_text:
        for index, line in enumerate(input_text):
            pass

    if part_num == "1":
        print(f"day15: Python solution for part 1: {result}, time: {time.time() - start} s")
    elif part_num == "2":
        print(f"day15: Python solution for part 2: {part2res}, time: {time.time() - start} s")

start = time.time()
part("1")
start = time.time()
part("2")