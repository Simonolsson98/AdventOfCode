import os

def part(part_num):
    with open(os.path.dirname(__file__)+"/day05_input.txt", 'r') as input_text:
        values = [int(x) for x in input_text.readline().split(":")[1].strip().split(" ")]
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

            for value in values:
                for stsmap in value_map_tuple:
                    dest = int(stsmap[0])
                    src = int(stsmap[1])
                    rnglen = int(stsmap[2])
                    if src <= value and src + rnglen >= value:
                        current_map = (value - src) + dest
                        break
                    else: 
                        current_map = value
                values[values.index(value)] = current_map # update values for next map

    if part_num == "1":
        print(f"day5: Python solution for part 1: {min(values)}")
    elif part_num == "2":
        print(f"day5: Python solution for part 2: {values}")

part("1")
#part("2")