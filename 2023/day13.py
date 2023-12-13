import os
import math
import time

def part(part_num):
    arr=[]
    with open(os.path.dirname(__file__)+"/day13_input.txt", 'r') as input_text:
        result = 0
        subarr = []
        for index, line in enumerate(input_text):
            if(line.rstrip("\n") == ""):
                arr.append(subarr)
                savedup = 0

                for subindex, subline in enumerate(subarr):
                    lowerindex = subindex - 1
                    upperindex = subindex
                    if(subarr[lowerindex] == subarr[upperindex]):
                        savedup = lowerindex + 1
                        #print(f"savedup = lowerindex {lowerindex}")
                        #print(f"subarr[lowerindex]: {subarr[lowerindex]}, subarr[upperindex]: {subarr[upperindex]}, low: {lowerindex}, high: {upperindex}")                  
                        success = True
                        while(upperindex < len(subarr) - 1 and lowerindex > 0):
                            lowerindex -= 1
                            upperindex += 1
                            #print(f"comparing: {subarr[lowerindex]} != {subarr[upperindex]}, low: {lowerindex}, high: {upperindex}")
                            if(subarr[lowerindex] != subarr[upperindex]):
                                success = False
                                print("rip reflection")
                                break
                        if(success):
                            #print(f"survived?: {lowerindex} == {upperindex}")
                            #print(f"savedup: {savedup}")
                            result += (savedup * 100)

                lawl = [[el] for el in subarr if el]
                hmm = list(map(list, zip(*subarr)))
                transposed = ["".join(asd) for asd in hmm]
                savedleft = 0
                print(f"subarr: {subarr}")
                print(f"transposed: {transposed}")
                for subindex, subline in enumerate(transposed):
                    lowerindex = subindex - 1
                    upperindex = subindex
                    if(transposed[lowerindex] == transposed[upperindex]):
                        savedleft = lowerindex + 1
                        success = True
                        #print(f"transposed[lowerindex]: {transposed[lowerindex]}, {lowerindex} transposed[upperindex]: {transposed[upperindex]}")                  
                        while(upperindex < len(transposed) - 1 and lowerindex > 0):
                            lowerindex -= 1
                            upperindex += 1
                            #print(f"comparing: {transposed[lowerindex]} != {transposed[upperindex]}")
                            if(transposed[lowerindex] != transposed[upperindex]):
                                #print("rip reflection")
                                success = False
                                break
                        if(success):
                            #print(f"survived?: {lowerindex} == {upperindex}")
                            #print(f"savedleft: {savedleft}")
                            result += savedleft

                subarr = []
                transposed = []
            else:
                lul = line.rstrip("\n")
                print(f"appending: {lul}")

                subarr.append(line.rstrip("\n"))

    if part_num == "1":
        print(f"day13: Python solution for part 1: {result}, time: {round(time.time() - start, 3)} s")
    elif part_num == "2":
        print(f"day13: Python solution for part 2: {result}, time: {round(time.time() - start, 3)} s")

start = time.time()
part("1")
#start = time.time()
#part("2")