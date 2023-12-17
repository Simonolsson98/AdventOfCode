import os
import math
import time

def part(part_num):
    with open(os.path.dirname(__file__)+"/day17_input.txt", 'r') as input_text:
        global edges
        global visited
        global values 
        edges = []
        visited = []
        values = []
        for line in input_text:
            edges.append(list(map(int, str(line.strip()))))
            visited.append([not elem for elem in list(map(bool, str(line.strip())))])
            values.append([999] * len(line.rstrip("\n")))

        curr_i = 0
        curr_j = 0
        istraightcounter = 0
        jstraightcounter = 0
        values[0][0] = 0
        while (not visited[len(visited) - 1][len(visited) - 1]):
            visit_neighbour(curr_i, curr_j, istraightcounter, jstraightcounter, "right")

    if(part_num == "1"):
        [print(i) for i in values]
        return values[len(visited) - 1][len(visited) - 1]
    else:
        pass

def visit_neighbour(i: int, j: int, istraightcounter: int, jstraightcounter: int, direc: str):
    if(i == 1 and j == 5):
        print(f"UP: {values[i - 1][j]}, LEFT: {values[i][j - 1]}, RIGHT: {values[i][j + 1]}, DOWN: {values[i + 1][j]}")

    if(direc != "down" and i - 1 >= 0 and istraightcounter < 3):
        up = edges[i - 1][j]
        if(values[i][j] + up < values[i - 1][j]):
            values[i - 1][j] = values[i][j] + up
            visit_neighbour(i - 1, j, istraightcounter + 1, 0, "up")

    if(direc != "right" and j - 1 >= 0 and jstraightcounter < 3):
        left = edges[i][j - 1]
        if(values[i][j] + left < values[i][j - 1]):
            values[i][j - 1] = values[i][j] + left
            visit_neighbour(i, j - 1, 0, jstraightcounter + 1, "left")

    if(direc != "left" and j + 1 < len(visited[0]) and jstraightcounter < 3):
        right = edges[i][j + 1]
        if(values[i][j] + right < values[i][j + 1]):
            values[i][j + 1] = values[i][j] + right
            visit_neighbour(i, j + 1, 0, jstraightcounter + 1, "right")

    if(direc != "up" and i + 1 < len(visited) and istraightcounter < 3):
        down = edges[i + 1][j]
        if(values[i][j] + down < values[i + 1][j]):
            values[i + 1][j] = values[i][j] + down
            visit_neighbour(i + 1, j, istraightcounter + 1, 0, "down")
   
    if(i == 1 and j == 5):
        print(f"AFTER:::: UP: {values[i - 1][j]}, LEFT: {values[i][j - 1]}, RIGHT: {values[i][j + 1]}, DOWN: {values[i + 1][j]}")

    visited[i][j] = True
    return

start = time.time()
print(f"day17: Python solution for part 1: {part('1')}, time: {round(time.time() - start, 4)} s")

#start = time.time()
#print(f"day17: Python solution for part 2: {part('2')}, time: {round(time.time() - start, 4)} s")
