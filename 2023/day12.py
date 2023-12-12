import os
import math
import time

def part(part_num):
    with open(os.path.dirname(__file__)+"/day12_input.txt", 'r') as input_text:
        result = 0
        for line in input_text:
            op, listofrecords = line.split(" ")
            counts = listofrecords.rstrip("\n")

            result += findarrangements(op, 0, "", counts)

    if part_num == "1":
        print(f"day12: Python solution for part 1: {result}, time: {round(time.time() - start, 3)} s")
    elif part_num == "2":
        print(f"day12: Python solution for part 2: {result}, time: {round(time.time() - start, 3)} s")

def findarrangements(op, currindex, currl, counts):
    result = 0
    while(currindex < len(op)):
        currentchar = op[currindex]
        if currentchar == "?":
            return findarrangements(op, currindex + 1, currl + "#", counts) \
            + findarrangements(op, currindex + 1, currl + ".", counts)
        else:
            return findarrangements(op, currindex + 1, currl + currentchar, counts)

    test = [len(asd) for asd in currl.split(".") if asd]
    if(test == list(map(int, counts.split(",")))):
        return 1
    
    return 0

start = time.time()
part("1")
#start = time.time()
#part("2")