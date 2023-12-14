import os
import math
import time
import numpy as np

def part(part_num):
    with open(os.path.dirname(__file__)+"/day14_input.txt", 'r') as input_text:
        result = 0
        arr = []
        for line in input_text:
            arr.append(line.rstrip("\n"))
        
        if(part_num == "1"):
            for i in range(len(arr[0])):
                stopping_index = -1
                load_per_row = len(arr)
                blocked = False
                for j in range(len(arr)):
                    curr = arr[j][i]
                    if curr == "O":
                        result += (load_per_row - (stopping_index + 1))
                        stopping_index += 1
                    elif curr == "#":
                        stopping_index = j
        else:
            savedarr = []
            x = 0
            while(x < 1_000_000_000):
                for i in range(4):
                    for i in range(len(arr[0])):
                        stopping_index = 0

                        newarr = ["x" * len(arr)]
                        for j in range(len(arr)):
                            curr = arr[j][i]
                            
                            if curr == "O":
                                if(newarr[0][stopping_index] == "."):
                                    # This is needed to simulate the O "falling" past the dot
                                    newarr[0] = newarr[0][:stopping_index] + curr + newarr[0][stopping_index:-1]
                                else:
                                    newarr[0] = newarr[0][:stopping_index] + curr + newarr[0][stopping_index + 1:]
                                
                                stopping_index += 1
                            elif curr == ".":
                                newarr[0] = newarr[0][:j] + curr + newarr[0][j + 1:]
                            elif curr == "#":
                                stopping_index = j + 1
                                newarr[0] = newarr[0][:j] + curr + newarr[0][j + 1:]

                        for j in range(len(arr)):
                            arr[j] = arr[j][:i] + newarr[0][j] + arr[j][i+1:]

                    # rotate 3 times counter clock wise (i.e. once clock wise)
                    arr = [list(asd) for asd in arr]
                    na = np.array(arr)
                    arr = np.rot90(na, 3)

                    arr = ["".join(a) for a in arr]

                    # need to break reference here, since arr will change later on, and we want to keep the old version
                    nparr = arr[:]

                if(nparr == savedarr):
                    inc = x - 1000
                    x = 1_000_000_000 - inc

                if (x == 1000):
                    savedarr = nparr
                    
                x += 1

            load_per_row = len(arr)
            result = 0
            for i in range(len(arr)):
                for j in range(len(arr[0])):
                    curr = arr[i][j]
                    if curr == "O":
                        result += load_per_row
                load_per_row -= 1

    return result

start = time.time()
print(f"day14: Python solution for part 1: {part('1')}, time: {round(time.time() - start, 4)} s")
start = time.time()
print(f"day14: Python solution for part 2: {part('2')}, time: {round(time.time() - start, 4)} s")
