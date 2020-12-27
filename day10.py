import time

def main():
    input = open("day10_input.txt")
    lines = []
    i = input.readline()
    
    while i: #get input into a list of strings
        lines.append(int(i))
        i = input.readline()

    global return_val
    global one_jolt_diff
    global three_jolt_diff
    return_val = 0
    one_jolt_diff = 0
    three_jolt_diff = 0
    used_adapters = []
    find_joltage(0, lines, used_adapters)
    return one_jolt_diff * three_jolt_diff

def find_joltage(index, lines, used_adapters):
    global return_val
    global one_jolt_diff
    global three_jolt_diff
    if(index == max(lines) and len(used_adapters) == len(lines)):
        three_jolt_diff += 1
        return
    if(index + 1 in lines):
        used_adapters.append(index + 1)
        one_jolt_diff += 1
        index += 1
        find_joltage(index, lines, used_adapters)
    elif(index + 2 in lines):
        used_adapters.append(index + 2)
        index += 2
        return find_joltage(index, lines, used_adapters)
    elif(index + 3 in lines):
        used_adapters.append(index + 3)
        index += 3
        three_jolt_diff += 1
        return find_joltage(index, lines, used_adapters)
    return 

if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 556543474


