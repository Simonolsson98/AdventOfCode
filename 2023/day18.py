import os
import time
import math
from shapely.geometry import Polygon, Point

edges=[]
def part(part_num, start):
    with open(os.path.dirname(__file__)+"/day18_input.txt", 'r') as input_text:
        starting_index = ()
        row = 0
        col = 0
        edges.append((row, col))
        for line in input_text:
            (direction, count, color) = line.split(" ")
            if(direction == "U"):
                for _ in range(int(count)):
                    row -= 1
                    edges.append((row, col))
            elif(direction == "R"):
                for _ in range(int(count)):
                    col += 1
                    edges.append((row, col))
            elif(direction == "D"):
                for _ in range(int(count)):
                    row += 1
                    edges.append((row, col))
            elif(direction == "L"):
                for _ in range(int(count)):
                    col -= 1
                    edges.append((row, col))

        loop_polygon = Polygon(edges)
        minx, miny, maxx, maxy = loop_polygon.bounds
        result = 0
        for i in range(int(minx), int(maxx) + 1):
            for j in range(int(miny), int(maxy) + 1):
                point = Point(i, j)
                if loop_polygon.contains(point):
                    result += 1

        return result + len(list(set(edges)))

start = time.time()
result = part("1", start)
print(f"day18: Python solution for part 1: {result}, time: {round(time.time() - start, 5)} s")
#print(f"day18: Python solution for part 2: {part2res}, time: {round(time.time() - start, 5)} s")