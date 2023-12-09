import os
import time

def part(part_num):
    with open(os.path.dirname(__file__)+"/day05_input.txt", 'r') as input_text:
        if(part_num == "1"):
            values = [int(x) for x in input_text.readline().split(":")[1].strip().split(" ")]
        else:
            values = [int(x) for x in input_text.readline().split(":")[1].strip().split(" ")]
            paired_values=[]
            for i in range(len(values)//2):
                paired_values.append((values[2*i], values[2*i+1]))
        print(f"paired_values: {paired_values}")
        input_text.readline() # skip newline in input
        for i in range(7):        
            name = input_text.readline()
            data = input_text.readline()
            value_map_tuple = []
            while data.strip():
                value_map = data.split(" ")
                dest_range=int(value_map[0])
                src_range=int(value_map[1])
                range_length=int(value_map[2])

                value_map_tuple.append((dest_range, src_range, range_length))
                data = input_text.readline()

            if(part_num == "2"):
                for i, (src, src_range) in enumerate(paired_values):
                    for xdest, xsrc, xsrc_range in value_map_tuple:
                        if src < xsrc and src + src_range < xsrc:
                            print(f"left of range")
                            break
                        elif src < xsrc and src + src_range == xsrc:
                            print(f"touching left of range")
                            paired_values[paired_values.index((src, src_range))]=((xdest, src_range - (xsrc - src)))
                            paired_values.append((src, xsrc - src))
                            break
                        elif src > xsrc + xsrc_range:
                            print(f"right of range")
                            break
                        elif src < xsrc and src + src_range > xsrc + xsrc_range:
                            print(f"overloaded coverage")
                            paired_values[paired_values.index((src, src_range))]=((xdest, xsrc_range))
                            paired_values.append((src, xsrc - src))
                            paired_values.append((xsrc + xsrc_range, src_range - (xsrc - src) - xdest))
                            break
                        elif src < xsrc and src + src_range > xsrc: # but src + src_range <= xsrc + xsrc_range
                            print(f"end coverage")
                            paired_values[paired_values.index((src, src_range))]=((xdest, src_range - (xsrc - src)))
                            paired_values.append((src, xsrc - src))
                            break
                        elif src >= xsrc and src + src_range < xsrc + xsrc_range:
                            print(f"total coverage")
                            paired_values[paired_values.index((src, src_range))]=(xdest + (xsrc - src), src_range)
                            break
                        elif src >= xsrc and src + src_range > xsrc + xsrc_range and src > xsrc + xsrc_range:
                            print(f"start coverage")
                            print(src)
                            print(src_range)
                            print(xsrc)
                            print(xsrc_range)
                            print((xdest + (src - xsrc), (xsrc + xsrc_range) - src))
                            print((src + (xsrc + xsrc_range) - src, src_range - (xsrc + xsrc_range - src)))
                            paired_values[paired_values.index((src, src_range))]=(xdest + (src - xsrc), (xsrc + xsrc_range) - src)
                            paired_values.append((src + (xsrc + xsrc_range) - src, src_range - (xsrc + xsrc_range - src)))
                            if(xsrc_range - src_range < 0):
                                print(src_range - (xsrc + xsrc_range - src))
                                print(src)
                                print(src_range)
                                print(xsrc)
                                print(xsrc_range)
                            break
                        else: 
                            print(f"PLEASE NO")
                            print(f"src: {src}, src_range: {src_range}")
                            print(f"xdest: {xdest}, xsrc: {xsrc}, xsrc_range: {xsrc_range}")
                            break
        print(value_map_tuple)
    if part_num == "1":
        print(f"day5: Python solution for part 1: {paired_values}, time: {time.time() - start} s")
    elif part_num == "2":
        print(f"day5: Python solution for part 2: {paired_values}, time: {time.time() - start} s")

start = time.time()
part("1")
start = time.time()
#part("2")
#10114991
