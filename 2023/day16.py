import os
import math
import time

global test
def part(part_num):
    with open(os.path.dirname(__file__)+"/day16_input.txt", 'r') as input_text:
        mirrors = []
        visited = []
        for line in input_text:
            mirrors.append(line.rstrip("\n"))

    global test
    test = mirrors[:]
    if(part_num == "1"):
        traverse(mirrors, visited, 0, -1, "right")
        result = 0
        result = sum([row.count("x") for row in test])
        return result
    else:
        result = 0
        energizes = []
        for height in range(len(mirrors)):
            test = mirrors[:]
            visited = []
            traverse(mirrors, visited, height, -1, "right")
            energizes.append(sum([row.count("x") for row in test]))

            test = mirrors[:]
            visited = []
            traverse(mirrors, visited, height, len(mirrors[0]), "left")
            energizes.append(sum([row.count("x") for row in test]))

        for width in range(len(mirrors[0])):
            test = mirrors[:]
            visited = []
            traverse(mirrors, visited, -1, width, "down")
            energizes.append(sum([row.count("x") for row in test]))

            test = mirrors[:]
            visited = []
            traverse(mirrors, visited, len(mirrors), width, "up")
            energizes.append(sum([row.count("x") for row in test]))

        print(max(energizes))
        return max(energizes)

def traverse(mirrors: list, visited: list, height: int, width: int, direction: str):
    global test
    while(True):
        match direction:
            case "left":
                width -= 1
            case "right":
                width += 1
            case "up":
                height -= 1
            case "down":
                height += 1

        if(height >= len(mirrors) or height < 0 or width >= len(mirrors[0]) or width < 0):
            return

        next_ele = mirrors[height][width]
        if(next_ele == "."):
            visited.append((height, width))
            test[height] = test[height][:width] + "x" + test[height][width + 1:]
        elif(next_ele == "\\"):
            if direction == "right" or direction == "up":
                if((height, width, "rightup")) in visited:
                    return

                visited.append((height, width, "rightup"))
                test[height] = test[height][:width] + "x" + test[height][width + 1:]
                if(direction == "right"):
                    direction = "down"
                else:
                    direction = "left"
            else: #direction == left or down
                if((height, width, "leftdown")) in visited:
                    return

                visited.append((height, width, "leftdown"))
                test[height] = test[height][:width] + "x" + test[height][width + 1:]
                if(direction == "left"):
                    direction = "up"
                else:
                    direction = "right"
        elif(next_ele == "/"):
            if direction == "right" or direction == "down":
                if((height, width, "rightdown")) in visited:
                    return

                visited.append((height, width, "rightdown"))
                test[height] = test[height][:width] + "x" + test[height][width + 1:]
                if(direction == "right"):
                    direction = "up"
                else:
                    direction = "left"
            else: #direction == left or up
                if((height, width, "leftup")) in visited:
                    return

                visited.append((height, width, "leftup"))
                test[height] = test[height][:width] + "x" + test[height][width + 1:]
                if(direction == "left"):
                    direction = "down"
                else:
                    direction = "right"
        elif next_ele == "|":
            if direction == "up" or direction == "down":
                if((height, width, "updown")) in visited:
                    return
                visited.append((height, width, "updown"))
                test[height] = test[height][:width] + "x" + test[height][width + 1:]
            else:
                if((height, width, "leftright")) in visited:
                    return
                visited.append((height, width, "leftright"))
                test[height] = test[height][:width] + "x" + test[height][width + 1:]

                traverse(mirrors, visited, height, width, "up")
                traverse(mirrors, visited, height, width, "down")
                return
        elif next_ele == "-":
            if direction == "left" or direction == "right":
                if((height, width, "leftright")) in visited:
                    return
                visited.append((height, width, "leftright"))
                test[height] = test[height][:width] + "x" + test[height][width + 1:]
            else:
                if((height, width, "updown")) in visited:
                    return
                visited.append((height, width, "updown"))
                test[height] = test[height][:width] + "x" + test[height][width + 1:]

                traverse(mirrors, visited, height, width, "left")
                traverse(mirrors, visited, height, width, "right")
                return


start = time.time()
print(f"day16: Python solution for part 1: {part('1')}, time: {round(time.time() - start, 4)} s")

start = time.time()
print(f"day16: Python solution for part 2: {part('2')}, time: {round(time.time() - start, 4)} s")
