import os
import time
start = time.time()

def part(part_num):
    result = 0
    with open(os.path.dirname(__file__)+"/day10_input.txt", 'r') as input_text:
        for line in input_text:
            pass
    
    return result

result = part("1")
print(f"day10: Python solution for part 1: {result}, time: {round(time.time() - start, 5)} s")
result = part("1")
print(f"day10: Python solution for part 2: {result}, time: {round(time.time() - start, 5)} s")