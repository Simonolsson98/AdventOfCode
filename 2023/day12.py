import os
import math
import time

def part(part_num):
    with open(os.path.dirname(__file__)+"/day12_input.txt", 'r') as input_text:
        result = 0
        for line in input_text:
            operational_broken, listofrecords = line.split(" ")
            listofrecords = listofrecords.rstrip("\n")
            trimmed = [x for x in operational_broken.split(".") if x]
            split_records = listofrecords.split(",")
            print(trimmed)
            print(split_records)

            result += findarrangements(trimmed,split_records, 0, 0, 0)

    if part_num == "1":
        print(f"day12: Python solution for part 1: {result}, time: {round(time.time() - start, 3)} s")
    elif part_num == "2":
        print(f"day12: Python solution for part 2: {result}, time: {round(time.time() - start, 3)} s")

def findarrangements(trimmed, split_records, i, j, arrangements):
    print(f"orig trim:{trimmed}")
    while(i < len(trimmed)):
        while(j < len(split_records)):
            try:
                rec = trimmed[i]
                entry = int(split_records[j])
            except:
                return arrangements

            print(f"rec: {rec}, entry: {entry}")
            if(len(rec) == entry):
                unknown = int(entry) - rec.count("#")
                total = rec.count("?")
                print(f"trimmed: {trimmed}, split_records: {split_records}")
                j += 1
                i += 1
            else:
                unknown = int(entry)
                if(unknown > len([asd for asd in rec if asd != "x"])):
                    if(i + 1 > len(trimmed)):
                        print("TOO FAR")
                        return arrangements
                    print(f"GO NEXT TECKEN: {i + 1}")
                    return findarrangements(trimmed, split_records, i + 1, j, arrangements)

                indices = [i for i, x in enumerate(rec) if x == "?" or x == "#"]
                brokenindices = [i for i, x in enumerate(rec) if x == "#"]
                predefgroup = [x for x in trimmed if all(y == "#" for y in x)]
                predefidk = "".join([x for x in rec.split("?") if x])
                print(f"unknown: {unknown} indices: {indices}, brokenindices: {brokenindices}")
                print(f"predefgroup: {predefgroup}")
                print(f"predefidk: {predefidk}")

                for start in indices:
                    print(f"start: {start}")
                    ffs = "fuck you"
                    try:
                        ffs = len(predefgroup[j])
                    except:
                        ffs = len(predefidk)
                    try:
                        if(unknown == ffs):
                            copy = trimmed[i]
                            tryfind = "#" * unknown
                            replace = "x" * unknown
                            yeah = copy.find(tryfind)
                            print(f"yeah:{yeah + unknown}")

                            copy = "x" * yeah + replace + copy[yeah + unknown:]
                            print(f"after early stage for copy: {copy}")

                            return findarrangements([copy], split_records, i, j + 1, arrangements)
                    except:
                        pass

                    copy = rec
                    print(f"copy: {copy}, start: {start}, entry: {entry}")

                    print(f"copy before: {copy}")
                    
                    if(start + unknown == len(copy)):
                        print("NONONO")
                        return arrangements
                    if(start == 0):
                        copy = copy[:start] + "#" * unknown + copy[start + unknown:]
                    else:
                        copy = copy[:start + 1] + "#" * unknown + copy[start + unknown + 1:]

                    print(f"copy after:  {copy}")
                    time.sleep(0.1)
                    tryfind = "#" * entry
                    print(f"tryfind: {tryfind} for i: {i} and len(split_records): {len(split_records)}")
                    if(tryfind in copy and j == len(split_records) - 1):
                        final_arrangements = copy.count("#")
                        print(f"\nINCREASING HERE FROM {arrangements} TO {arrangements + final_arrangements}\n")
                        arrangements += final_arrangements
                        if(copy[-1] == "#"):
                            print(f"LAST{copy[-1]}")
                            return arrangements
                    elif(tryfind in copy):
                        print(f"found - recursion inc: {tryfind}")
                        copy = "x" * (unknown + start + 1) + copy[start + unknown + 1:]
                        print(f"copy after fucku: {copy}")
                        print(f"go to number: {split_records[j + 1]} of stuff - trimmed: {trimmed[:i] + [copy] + trimmed[i+1:]}, split_records: {split_records}, i: {i}, j: {j + 1}")

                        start += unknown + 1
                        print(f"start after: {start}")
                        arrangements = findarrangements(trimmed[:i] + [copy] + trimmed[i+1:], split_records, i, j + 1, arrangements)
                    else:
                        print(f"no match, return: {arrangements}")
                        return arrangements
            i += 1
    return arrangements

start = time.time()
part("1")
#start = time.time()
#part("2")