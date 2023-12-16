import os
import math
import time

def part(part_num):
    with open(os.path.dirname(__file__)+"/day16_input.txt", 'r') as input_text:
        mirrors = []
        visited = []
        for line in input_text:
            mirrors.append(line.rstrip("\n"))

    if(part_num == "1"):
        traverse(mirrors, visited, 0, -1, "right")
        return len(list(set([(t[0], t[1]) for t in visited])))
    else:
        energizes = []
        # len(mirrors) == len(mirrors[i]), so we can use whichever for all directions
        for span in range(len(mirrors)):
            visited = []
            traverse(mirrors, visited, len(mirrors), span, "up")
            energizes.append(len(list(set([(t[0], t[1]) for t in visited]))))

            visited = []
            traverse(mirrors, visited, -1, span, "down")
            energizes.append(len(list(set([(t[0], t[1]) for t in visited]))))

            visited = []
            traverse(mirrors, visited, span, len(mirrors), "left")
            energizes.append(len(list(set([(t[0], t[1]) for t in visited]))))

            visited = []
            traverse(mirrors, visited, span, -1, "right")
            energizes.append(len(list(set([(t[0], t[1]) for t in visited]))))

        return max(energizes)

def traverse(mirrors: list, visited: list, height: int, width: int, direction: str):
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
        match next_ele:
            case ".":
                visited.append((height, width))
            case "|":
                if((height, width)) in visited:
                    return
                visited.append((height, width))

                if direction == "right" or direction == "left":
                    # split into both directions
                    traverse(mirrors, visited, height, width, "up")
                    traverse(mirrors, visited, height, width, "down")
                    return
            case "-":
                if((height, width)) in visited:
                    return
                visited.append((height, width))

                if direction == "up" or direction == "down":
                    # split into both directions
                    traverse(mirrors, visited, height, width, "left")
                    traverse(mirrors, visited, height, width, "right")
                    return
            case "\\":
                # special case, it matters what directions we come from for the 90 deg turns
                if direction == "right" or direction == "up":
                    if((height, width, "rightup")) in visited:
                        return

                    visited.append((height, width, "rightup"))
                    # ¯|
                    if(direction == "right"):
                        direction = "down"
                    else:
                        direction = "left"
                else: #direction == left or down
                    if((height, width)) in visited:
                        return

                    visited.append((height, width))
                    # |_
                    if(direction == "left"):
                        direction = "up"
                    else:
                        direction = "right"
            case "/":
                # special case, it matters what directions we come from for the 90 deg turns
                if direction == "right" or direction == "down":
                    if((height, width, "rightdown")) in visited:
                        return

                    visited.append((height, width, "rightdown"))
                    # _|
                    if(direction == "right"):
                        direction = "up"
                    else:
                        direction = "left"
                else: #direction == left or up
                    if((height, width)) in visited:
                        return

                    visited.append((height, width))
                    # |¯
                    if(direction == "left"):
                        direction = "down"
                    else:
                        direction = "right"


start = time.time()
print(f"day16: Python solution for part 1: {part('1')}, time: {round(time.time() - start, 4)} s")

start = time.time()
print(f"day16: Python solution for part 2: {part('2')}, time: {round(time.time() - start, 4)} s")
