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
                    print(f"curr: {curr}")
                    if curr == "O":
                        result += (load_per_row - (stopping_index + 1))
                        stopping_index += 1
                    elif curr == "#":
                        stopping_index = j

                print(f"result after arr[j]: {arr[j]}: {result}")
        else:
            savedarr = []
            x = 0
            while(x < 1_000_000_000):
                #print(x)
                for i in range(4):
                    for i in range(len(arr[0])):
                        stopping_index = 0
                        # HARD CODED 100
                        test = ["x" * 100]
                        for j in range(len(arr)):
                            curr = arr[j][i]
                            
                            if curr == "O":
                                if(test[0][stopping_index] == "."):
                                    test[0] = test[0][:stopping_index] + curr + test[0][stopping_index:-1]
                                else:
                                    test[0] = test[0][:stopping_index] + curr + test[0][stopping_index + 1:]
                                
                                stopping_index += 1
                            elif curr == ".":
                                test[0] = test[0][:j] + curr + test[0][j + 1:]
                            elif curr == "#":
                                stopping_index = j + 1
                                test[0] = test[0][:j] + curr + test[0][j + 1:]

                        for j in range(len(arr)):
                            arr[j] = arr[j][:i] + test[0][j] + arr[j][i+1:]

                    #ROTATE
                    arr = [list(asd) for asd in arr]

                    na = np.array(arr)
                    arr = np.rot90(na, 3)
                    
                    #convert back to my format
                    arr = ["".join(a) for a in arr]
                    nparr = arr[:]

                if(nparr == savedarr):
                    inc = x - 1000
                    while(x < (1_000_000_000 - inc)):
                        #print(x)
                        x += inc
                    print(f"out at: {x}")

                if (x == 1000):
                    savedarr = nparr

                x += 1
                print(x)
                #[print(a) for a in nparr]
                #print("\n\n")

            load_per_row = len(arr)
            result = 0
            for i in range(len(arr)):
                for j in range(len(arr[0])):
                    curr = arr[i][j]
                    if curr == "O":
                        result += load_per_row

                load_per_row -= 1

    return result

#start = time.time()
#print(f"day14: Python solution for part 1: {part('1')}, time: {round(time.time() - start, 4)} s")

start = time.time()
print(f"day14: Python solution for part 2: {part('2')}, time: {round(time.time() - start, 4)} s")
