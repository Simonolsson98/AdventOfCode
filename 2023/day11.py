import os
import math
import time

def part(part_num):
    arr=[]
    with open(os.path.dirname(__file__)+"/day11_input.txt", 'r') as input_text:
        empty_rows = []
        curr_index = 0
        for index, line in enumerate(input_text):
            arr.append(line.rstrip("\n"))
            if "#" not in line:
                if(part_num == "1"):
                    arr[curr_index:curr_index + 1] = ["." * len(arr[0])] + ["." * len(arr[0])]
                    curr_index += 1
                else:
                    empty_rows.append(index)
            curr_index += 1

    transposed = [''.join(list(x)) for x in zip(*arr)]
    index = 0
    empty_cols = []
    while index < len(transposed):
        row = transposed[index]
        if "#" not in row:
            if(part_num == "1"):
                # part 1
                transposed[index:index + 1] = ["." * len(transposed[0])] + ["." * len(transposed[0])]
                index += 1
            else:
                # part 2
                empty_cols.append(index)
        index += 1

    galaxies=[]
    transposed_back = [''.join(list(x)) for x in zip(*transposed)]
    for i, row in enumerate(transposed_back):
        if "#" in row:
            indices = [i for i, x in enumerate(row) if x == "#"]
            for index in indices:
                galaxies.append((i, index))

    visited = []
    result = 0
    for elem in galaxies:
        for elem_iter in galaxies:
            if elem_iter != elem and elem_iter not in visited:
                if(part_num == "1"):
                    # part 1
                    result += abs(elem[0] - elem_iter[0]) + abs(elem[1] - elem_iter[1])
                else:
                    # part 2
                    rowval = 0
                    colval = 0
                    for emptyrow in empty_rows:
                        if (elem[0] > emptyrow and elem_iter[0] < emptyrow) or (elem[0] < emptyrow and elem_iter[0] > emptyrow):
                            rowval += 999999
                    for emptycol in empty_cols:
                        if (elem[1] > emptycol and elem_iter[1] < emptycol) or (elem[1] < emptycol and elem_iter[1] > emptycol):
                            colval += 999999

                    result += abs(elem[0] - elem_iter[0]) + rowval + abs(elem[1] - elem_iter[1]) + colval
        visited.append(elem)

    if part_num == "1":
        print(f"day11: Python solution for part 1: {result}, time: {round(time.time() - start, 3)} s")
    elif part_num == "2":
        print(f"day11: Python solution for part 2: {result}, time: {round(time.time() - start, 3)} s")

start = time.time()
part("1")
start = time.time()
part("2")