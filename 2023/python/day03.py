import os

def part(part_num):
    with open(os.path.dirname(__file__)+"/day02_input.txt", 'r') as input_text:
        for line in input_text:

    if part_num == "1":
        print(f"day3: Python solution for part 1: {result}")
    elif part_num == "2":
        print(f"day3: Python solution for part 2: {part2result}")

part("1")
part("2")