import os
import math
import time

def part(part_num):
    with open(os.path.dirname(__file__)+"/day13_input.txt", 'r') as input_text:
        result = 0
        mirrors = []
        for index, line in enumerate(input_text):
            if(line.rstrip("\n") == ""):
                smudges = find_smudges(mirrors, part_num)
                if(smudges != -1):
                    result += ((smudges + 1) * 100)
                    mirrors = []
                    continue

                # map list zip = transpose, python btw
                transposed_mirrors = ["".join(asd) for asd in list(map(list, zip(*mirrors)))]
                smudges = find_smudges(transposed_mirrors, part_num)
                if(smudges != -1):
                    result += (smudges + 1)
                    mirrors = []
                    continue

                mirrors = []
                transposed_mirrors = []
            else:
                mirrors.append(line.rstrip("\n"))

    return result
  
def find_smudges(mirrors: list, part_num: str) -> int:
    for i in range(len(mirrors) - 1):
        smudges = 0
        for j in range(len(mirrors)):
            above_part = i + j + 1
            below_part = i - j

            if(above_part > len(mirrors) - 1 or below_part < 0):
                continue

            diff = sum(mirrors[above_part][charindex] != mirrors[below_part][charindex] for charindex in range(len(mirrors[above_part])))
            smudges += diff

        # part 1 allows no differences, part 2 allows 1 difference
        if((smudges == 0 and part_num == "1") or (smudges == 1 and part_num == "2")):
            return i

    # no reflection point was found
    return -1

start = time.time()
print(f"day13: Python solution for part 1: {part('1')}, time: {round(time.time() - start, 4)} s")

start = time.time()
print(f"day13: Python solution for part 2: {part('2')}, time: {round(time.time() - start, 4)} s")
