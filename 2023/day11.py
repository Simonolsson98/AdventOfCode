import os
import math
import time

arr=[]
galaxies=[]
def part(part_num):
    with open(os.path.dirname(__file__)+"/day11_input.txt", 'r') as input_text:
        curr_index = 0
        for line in input_text:
            arr.append(line.rstrip("\n"))
            if "#" in line:
                pass
                #indices = [i for i, x in enumerate(line) if x == "#"]
                #for index in indices:
                #    row = len(arr)
                #    galaxies.append((row - 1, index))
            else:
                arr[curr_index:curr_index + 1] = ["." * len(arr[0])] + ["." * len(arr[0])]
                curr_index += 1
            curr_index += 1

    transposed = [''.join(list(x)) for x in zip(*arr)]
    index = 0
    while index < len(transposed):
        row = transposed[index]
        if "#" in row:
            pass
        else:
            transposed[index:index + 1] = ["." * len(transposed[0])] + ["." * len(transposed[0])]
            index += 1
        
        index += 1

    test = [''.join(list(x)) for x in zip(*transposed)]
    for i, row in enumerate(test):
        if "#" in row:
            indices = [i for i, x in enumerate(row) if x == "#"]
            for index in indices:
                galaxies.append((i, index))

    done = []
    result = 0
    i = 0
    for elem in galaxies:
        for elem_iter in galaxies:
            if elem_iter != elem and elem_iter not in done:
                result += abs(elem[0] - elem_iter[0]) + abs(elem[1] - elem_iter[1])
        done.append(elem)

    print(result)

    if part_num == "1":
        print(f"day11: Python solution for part 1: {result}, time: {round(time.time() - start, 2)} s")
    elif part_num == "2":
        print(f"day11: Python solution for part 2: {result}, time: {round(time.time() - start, 2)} s")

start = time.time()
part("1")
#start = time.time()
#part("2")