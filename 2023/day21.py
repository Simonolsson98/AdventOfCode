import os
import time

def part(part_num):
    indices = []
    arr = []
    steps = 64
    with open(os.path.dirname(__file__)+"/day21_input.txt", 'r') as input_text:
        for row, line in enumerate(input_text.readlines()):
            if("S" in line):
                indices = [(row, line.find("S"))]
            arr.append(line.rstrip("\n"))
        
    row, col = indices[0]
    arr[row] = arr[row][:col] + "." + arr[row][col + 1:]

    for i in range(steps):
        temp = []
        for (xindex, yindex) in indices:
            try:
                if(arr[xindex][yindex - 1] == "."):
                    temp.append((xindex, yindex - 1))
                if(arr[xindex + 1][yindex] == "."):
                    temp.append((xindex + 1, yindex))
                if(arr[xindex][yindex + 1] == "."):
                    temp.append((xindex, yindex + 1))
                if(arr[xindex - 1][yindex] == "."):
                    temp.append((xindex - 1, yindex))
            except:
                pass

        indices = list(set(temp))
    return len(indices)


start = time.time()
print(f"day21: Python solution for part 1: {part('1')}, time: {round(time.time() - start, 5)} s")
#start = time.time()
#print(f"day21: Python solution for part 2: {part('2')}, time: {round(time.time() - start, 5)} s")