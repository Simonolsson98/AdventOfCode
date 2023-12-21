import os
import time

result = 0
def part(part_num):
    with open(os.path.dirname(__file__)+"/day20_input.txt", 'r') as input_text:
        line = input_text.readline().rstrip()
        while line != "":
            line = input_text.readline().rstrip()

start = time.time()
print(f"day20: Python solution for part 1: {part('1')}, time: {round(time.time() - start, 5)} s")
start = time.time()
print(f"day20: Python solution for part 2: {part('2')}, time: {round(time.time() - start, 5)} s")