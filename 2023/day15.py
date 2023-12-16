import os
import time

def part(part_num):
    result = 0
    with open(os.path.dirname(__file__)+"/day15_input.txt", 'r') as input_text:
        for index, line in enumerate(input_text):
            hashes = line.split(",")
            if(part_num == "1"):
                for hashh in hashes:
                    result += run_hash(hashh)
            else:
                hashlist = [[]] * 256
                for hashh in hashes:
                    if("=" in hashh):
                        splitchar = "="
                    else:
                        splitchar = "-"
                    
                    split = hashh.split(splitchar)
                    hash_input = split[0]
                    focalval = split[1]
                    index = run_hash(hash_input)
                    if splitchar == "-":
                        if hashlist[index] == []:
                            continue
                        else:
                            breakouter = False
                            for i, l in enumerate(hashlist[index]):
                                if hash_input == l[:-1]:
                                    replaceindex = hashlist[index].index(l)
                                    hashlist[index] = hashlist[index][:replaceindex] + hashlist[index][replaceindex + 1:]
                                    break
                                if breakouter:
                                    break
                    else: # "="
                        if hashlist[index] == []:
                            hashlist[index] = [hash_input + focalval]
                        else:
                            breakouter = False
                            for i, l in enumerate(hashlist[index]):
                                if hash_input == l[:-1]:
                                    replaceindex = hashlist[index].index(l)
                                    newele = hash_input + focalval
                                    hashlist[index] = hashlist[index][:replaceindex] + [newele] + hashlist[index][replaceindex + 1:]
                                    
                                    breakouter = True
                                    break
                            
                                if breakouter:
                                    break
                            
                            if not breakouter:
                                hashlist[index] += [hash_input + focalval]
                        
                for boxindex, box in enumerate(hashlist):
                    subres = 0
                    for eleindex, ele in enumerate(box, 1):
                        val = boxindex + 1
                        val *= (eleindex)
                        val *= int(ele[-1])
                        subres += val
                    result += subres

    if part_num == "1":
        print(f"day15: Python solution for part 1: {result}, time: {round(time.time() - start, 4)} s")
    elif part_num == "2":
        print(f"day15: Python solution for part 2: {result}, time: {round(time.time() - start, 4)} s")

def run_hash(hashh: str):
    val = 0
    for char in hashh:
        val += ord(char)
        val *= 17
        val %= 256
    
    return val

start = time.time()
part("1")
start = time.time()
part("2")