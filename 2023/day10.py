import os
import time
import math
from shapely.geometry import Polygon, Point

arr=[]
def part(part_num, start):
    with open(os.path.dirname(__file__)+"/day10_input.txt", 'r') as input_text:
        starting_index = ()
        for row, line in enumerate(input_text):
            if 'S' in line:
                starting_index = (row, line.index("S"))
            arr.append(line[:-1])

    (startrow, startcol) = starting_index
    length = 0
    visited = []
    current = arr[startrow][startcol]
    while(True):
        try:
            north=arr[startrow - 1][startcol]
        except IndexError:
            north = "."
        try:
            west=arr[startrow][startcol - 1]
        except IndexError:
            west = "."
        try:
            east=arr[startrow][startcol + 1]
        except IndexError:
            east = "."
        try:
            south=arr[startrow + 1][startcol]
        except IndexError:
            south = "."
       
        visited.append(( startrow,startcol ))

        if(current == "S" and length > 2):
            # part 1
            length = length // 2
            part1time = round(time.time() - start, 5)

            # part 2
            start = time.time()
            loop_polygon = Polygon(visited)
            part2res = 0
            for i in range(len(arr)):
                for j in range(len(arr[0])):
                    if((i, j) in visited):
                        continue
                    point = Point(i, j)
                    if loop_polygon.contains(point):
                        part2res += 1

            return length, part1time, part2res
        elif (current == "S"):
            if ((startrow, startcol + 1) not in visited and (east == "-" or east == "7" or east == "J")):
                current = east
                startcol += 1
            elif ((startrow, startcol - 1) not in visited and (west == "-" or west == "F" or west == "L")):
                current = west
                startcol -= 1
            elif ((startrow + 1, startcol) not in visited and (south == "L" or south == "J" or south == "|")):
                current = south
                startrow += 1
            elif ((startrow - 1, startcol) not in visited and (north == "7" or north == "F" or north == "|")):
                current = north
                startrow -= 1
        elif (current == "-"):
            if ((startrow, startcol + 1) not in visited and (east == "-" or east == "7" or east == "J") or east == "S" and length > 2):
                current = east
                startcol += 1
            elif ((startrow, startcol - 1) not in visited and (west == "-" or west == "F" or west == "L") or west == "S" and length > 2):
                current = west
                startcol -= 1
        elif (current == "|"):
            if ((startrow + 1, startcol) not in visited and (south == "L" or south == "J" or south == "|") or south == "S" and length > 2):
                current = south
                startrow += 1
            elif ((startrow - 1, startcol) not in visited and (north == "7" or north == "F" or north == "|") or north == "S" and length > 2):
                current = north
                startrow -= 1
        elif (current == "L"):
            if ((startrow, startcol + 1) not in visited and (east == "-" or east == "7" or east == "J") or east == "S" and length > 2):
                current = east
                startcol += 1
            elif ((startrow - 1, startcol) not in visited and (north == "7" or north == "F" or north == "|") or north == "S" and length > 2):
                current = north
                startrow -= 1
        elif (current == "J"):
            if ((startrow, startcol - 1) not in visited and (west == "-" or west == "F" or west == "L") or west == "S" and length > 2):
                current = west
                startcol -= 1
            elif ((startrow - 1, startcol) not in visited and (north == "7" or north == "F" or north == "|") or north == "S" and length > 2):
                current = north
                startrow -= 1
        elif (current == "7"):
            if ((startrow, startcol - 1) not in visited and (west == "-" or west == "F" or west == "L") or west == "S" and length > 2):
                current = west
                startcol -= 1
            elif ((startrow + 1, startcol) not in visited and (south == "L" or south == "J" or south == "|") or south == "S" and length > 2):
                current = south
                startrow += 1
        elif (current == "F"):
            if ((startrow, startcol + 1) not in visited and (east == "-" or east == "7" or east == "J") or east == "S" and length > 2):
                current = east
                startcol += 1
            elif ((startrow + 1, startcol) not in visited and (south == "L" or south == "J" or south == "|") or south == "S" and length > 2):
                current = south
                startrow += 1

        length += 1

start = time.time()
result, part1time, part2res = part("1", start)
print(f"day10: Python solution for part 1: {result}, time: {part1time} s")
print(f"day10: Python solution for part 2: {part2res}, time: {round(time.time() - start, 5)} s")