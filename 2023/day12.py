import os
import math
import time
from functools import lru_cache

def part(part_num):
    with open(os.path.dirname(__file__)+"/day12_input.txt", 'r') as input_text:
        result = 0
        for i, line in enumerate(input_text):
            print(i)
            if(part_num == "1"):
                op, listofrecords = line.split(" ")
                counts = listofrecords.rstrip("\n")
            else:
                op, listofrecords = line.split(" ")
                op = (op + "?") * 5
                op = op[:-1]
                listofrecords = (listofrecords.rstrip("\n") + ",") * 5
                listofrecords = listofrecords[:-1]
                counts = listofrecords

            listcounts = list(map(int, counts.split(",")))
            result += findarrangements(op, 0, [0][:], listcounts)

    if part_num == "1":
        print(f"day12: Python solution for part 1: {result}, time: {round(time.time() - start, 3)} s")
    elif part_num == "2":
        print(f"day12: Python solution for part 2: {result}, time: {round(time.time() - start, 3)} s")

def findarrangements(op, currindex, currl, listcounts):
    result = 0
    while(len(currl) < len(op)):
        currentchar = op[currindex]
        print(f"currl: {currl}, currindex: {currindex}, currentchar: {currentchar}")
        if currentchar == "?":
            fst = currl[:]
            kys = currl[:]
            if(fst[-1] != 0):
                fst.append(0)
            kys[-1] += 1

            return findarrangements(op, currindex + 1, fst[:], listcounts) + \
                findarrangements(op, currindex + 1, kys[:], listcounts)
        elif currentchar == ".":
            current_ele = currl[-1]
            print(f"WHEN DOT: current_ele: {current_ele}")
            if(current_ele > int(listcounts[len(currl) - 1])):
                print(f"dotkill: currl: {currl}, listcounts: {listcounts}")
                return 0

            currl.append(0)
            return findarrangements(op, currindex + 1, currl, listcounts)
        else:
            currl[-1] += 1
            current_ele = currl[-1]
            print(f"WHEN HASH: current_ele: {current_ele}")
            if(current_ele > int(listcounts[len(currl) - 1])):
                print(f"hashkill: currl: {currl}, listcounts: {listcounts}")
                return 0
        
        if(len(currl) > len(listcounts)):
            return 0
            
        if(currl == listcounts):
            return 1
    
    return 0

start = time.time()
part("1")
#start = time.time()
#part("2")