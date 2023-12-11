import os
import math
import time

arr=[]
galaxies=[]
def part(part_num):
    with open(os.path.dirname(__file__)+"/day11_input.txt", 'r') as input_text:
        for line in input_text:
            arr.append(line[:-1])
            if "#" in line:
                col = line.index("#")
                row = len(arr)
                galaxies.append((row, col))

    print(galaxies)
    return
    for rowindex in range(len(arr)):
        for colindex in range(len(arr[rowindex])):
            value = arr[rowindex][colindex]
            try:
                topleft  = arr[rowindex - 1][colindex - 1]
                topmid   = arr[rowindex - 1][colindex]
                topright = arr[rowindex - 1][colindex + 1]
                midleft  = arr[rowindex][colindex - 1]
                midright = arr[rowindex][colindex + 1]
                botleft  = arr[rowindex + 1][colindex - 1]
                botmid   = arr[rowindex + 1][colindex]
                botright = arr[rowindex + 1][colindex + 1]
            except:
                pass   

    if part_num == "1":
        print(f"day11: Python solution for part 1: {result}, time: {round(time.time() - start, 2)} s")
    elif part_num == "2":
        print(f"day11: Python solution for part 2: {result}, time: {round(time.time() - start, 2)} s")

start = time.time()
part("1")
start = time.time()
part("2")