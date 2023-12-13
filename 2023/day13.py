import os
import math
import time

def part(part_num):
    arr=[]
    with open(os.path.dirname(__file__)+"/day13_input.txt", 'r') as input_text:
        result = 0
        subarr = []
        if(part_num == "1"):
            for index, line in enumerate(input_text):
                if(line.rstrip("\n") == ""):
                    arr.append(subarr)
                    savedup = 0

                    for subindex, subline in enumerate(subarr):
                        lowerindex = subindex - 1
                        upperindex = subindex
                        if(subarr[lowerindex] == subarr[upperindex]):
                            savedup = lowerindex + 1
                            success = True
                            while(upperindex < len(subarr) - 1 and lowerindex > 0):
                                lowerindex -= 1
                                upperindex += 1
                                if(subarr[lowerindex] != subarr[upperindex]):
                                    success = False
                                    break
                            if(success):
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
                            while(upperindex < len(transposed) - 1 and lowerindex > 0):
                                lowerindex -= 1
                                upperindex += 1
                                if(transposed[lowerindex] != transposed[upperindex]):
                                    success = False
                                    break
                            if(success):
                                result += savedleft

                    subarr = []
                    transposed = []
                else:
                    lul = line.rstrip("\n")
                    print(f"appending: {lul}")

                    subarr.append(line.rstrip("\n"))
        else:
            for index, line in enumerate(input_text):
                if(line.rstrip("\n") == ""):
                    arr.append(subarr)

                    [print(f"arr before: {i}") for i in subarr]
                    res, modifiedarr = checksmudge(subarr, part_num, False)
                    if(res != -1):
                        result += (100 * res)
                        subarr = []
                        continue 

                    [print(f"arr after: {i}") for i in modifiedarr]

                    lawl = [[el] for el in modifiedarr if el]
                    hmm = list(map(list, zip(*modifiedarr)))
                    transposed = ["".join(asd) for asd in hmm]
                    
                    res, modifiedarr = checksmudge(transposed, part_num, False)
                    if(res != -1):
                        result += res
                        subarr = []
                        continue 
                else:
                    lul = line.rstrip("\n")
                    subarr.append(line.rstrip("\n"))

    if part_num == "1":
        print(f"day13: Python solution for part 1: {result}, time: {round(time.time() - start, 3)} s")
    elif part_num == "2":
        print(f"day13: Python solution for part 2: {result}, time: {round(time.time() - start, 3)} s")

def checksmudge(inputarray, part_num, recurse_with_smudge = False, lowerindex = -1, upperindex = -1, savedleft = -1):
    for subindex, subline in enumerate(inputarray, 1):
        if subindex >= len(inputarray): 
            return -1, inputarray[:]
        if lowerindex == -1:
            lowerindex = subindex - 1
        if upperindex == -1:
            upperindex = subindex

        print(f"lowerindex: {lowerindex}, upperindex: {upperindex}")
        diff = sum(inputarray[lowerindex][i] != inputarray[upperindex][i] for i in range(len(inputarray[upperindex])))

        if(inputarray[lowerindex] == inputarray[upperindex] or diff == 1):
            lowerindex_whiletrue = -1
            upperindex_whiletrue = -1
            while(upperindex < len(inputarray) and lowerindex >= 0):
                #time.sleep(0.1)
                print(f"IN WHILE: lowerindex: {lowerindex}, upperindex: {upperindex}")
                print(f"IN WHILE: lowerindex: {inputarray[lowerindex]}, upperindex: {inputarray[upperindex]}")
                diff = sum(inputarray[lowerindex][i] != inputarray[upperindex][i] for i in range(len(inputarray[upperindex])))
                if(part_num == "1" and diff == 1):
                    # part 1
                    recurse_with_smudge = False
                    break   

                # different, so look for smudge
                if(diff == 1 and recurse_with_smudge == False):
                    # part 2
                    indexdiff = [int(i) for i in range(len(inputarray[lowerindex])) if inputarray[lowerindex][i] != inputarray[upperindex][i]][0]
                    temp = inputarray[:]
                    if(inputarray[lowerindex][indexdiff] == "#"):
                        print(f"temp: changing # to . at index: [{lowerindex}][{indexdiff}]")
                        temp[lowerindex] = inputarray[lowerindex][:indexdiff] + "." + inputarray[lowerindex][indexdiff + 1:]
                    elif(inputarray[lowerindex][indexdiff] == "."):
                        print(f"temp: changing . to # at index: [{lowerindex}][{indexdiff}]")
                        temp[lowerindex] = inputarray[lowerindex][:indexdiff] + "#" + inputarray[lowerindex][indexdiff + 1:]
                    else:
                        print("WUT DONT BE HERE")

                    print("will recurse with:") 
                    [print(f"changed: {i}") for i in temp]

                    res, _arr = checksmudge(temp, part_num, True, lowerindex, upperindex, savedleft)
                    if(res != -1):
                        print("break here?")
                        return res, _arr

                    lowerindex += 1
                    upperindex += 1
                    print(f"GOING TO NEXT ROWS: lowerindex: {lowerindex} + upperindex: {upperindex}")
                elif diff == 0:
                    if (upperindex_whiletrue == -1):
                        upperindex_whiletrue = upperindex
                    if (lowerindex_whiletrue == -1):
                        lowerindex_whiletrue = lowerindex
                    if savedleft == -1:
                        savedleft = lowerindex + 1
                        print(f"savedleft: {savedleft} for lower: {lowerindex}")

                    print("EQUAL")
                    lowerindex -= 1
                    upperindex += 1
                    if((lowerindex < 0 or upperindex >= len(inputarray)) and recurse_with_smudge == False):
                        print("hard reset")
                        upperindex = upperindex_whiletrue + 1
                        lowerindex = lowerindex_whiletrue + 1

                elif diff > 1 and recurse_with_smudge == True:
                    print("too much diff, return")
                    return -1, inputarray
                else:
                    print("GO NEXT ROWS")
                    recurse_with_smudge = False
                    lowerindex += 1
                    upperindex += 1

            [print(f"out of while loop for: {i}") for i in inputarray]
            if(recurse_with_smudge):
                print(f"WOOO, returning: {savedleft}")
                return savedleft, inputarray[:]
            else: 
                return -1, inputarray
        else:
            lowerindex += 1
            upperindex += 1

start = time.time()
part("1")

start = time.time()
part("2")
# 21272 too low