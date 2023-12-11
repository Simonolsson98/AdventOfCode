import os
import math
import time

def part(part_num):
    arr=[]
    galaxies=[]
    empty_rows = []
    empty_cols = []
    with open(os.path.dirname(__file__)+"/day11_input.txt", 'r') as input_text:
        curr_index = 0
        for index, line in enumerate(input_text):
            arr.append(line.rstrip("\n"))
            if "#" in line:
                pass
            else:
                empty_rows.append(index)
                arr[curr_index:curr_index + 1] = ["." * len(arr[0])] + ["." * len(arr[0])]
                curr_index += 1
            curr_index += 1

    transposed = [''.join(list(x)) for x in zip(*arr)]
    index = 0
    added = 0
    while index < len(transposed):
        row = transposed[index]
        if "#" in row:
            pass
        else:
            empty_cols.append(index - added)
            transposed[index:index + 1] = ["." * len(transposed[0])] + ["." * len(transposed[0])]
            index += 1
            added += 1
        
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
                if(part_num == "1"):
                    result += abs(elem[0] - elem_iter[0]) + abs(elem[1] - elem_iter[1])
                else:
                    rowval = 0
                    colval = 0
                    print(empty_rows)
                    print(empty_cols)
                    for emptyrow in empty_rows:
                        if (elem[0] > emptyrow and elem_iter[0] < emptyrow) or (elem[0] < emptyrow and elem_iter[0] > emptyrow):
                            rowval += 999999
                    for emptycol in empty_cols:
                        if (elem[1] > emptycol and elem_iter[1] < emptycol) or (elem[1] < emptycol and elem_iter[1] > emptycol):
                            colval += 999999

                    print(f"rowval: {rowval}, colval: {colval} for elem: {elem} + elem_iter: {elem_iter}")
                    result += abs(elem[0] - elem_iter[0]) + rowval - 1 + abs(elem[1] - elem_iter[1]) + colval - 1
        done.append(elem)

    if part_num == "1":
        print(f"day11: Python solution for part 1: {result}, time: {round(time.time() - start, 2)} s")
    elif part_num == "2":
        print(f"day11: Python solution for part 2: {result - len(arr[0])}, time: {round(time.time() - start, 2)} s")

start = time.time()
part("1")
start = time.time()
part("2")
# too high 416944935244