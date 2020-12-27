import time

def main():
    input = open("day10_input.txt")
    lines = []
    i = input.readline()
    
    while i: #get input into a list of strings
        lines.append(int(i))
        i = input.readline()

    global one_jolt_diff #keep track of 1-jolt differences
    global three_jolt_diff #keep track of 3-jolt differences
    one_jolt_diff = 0
    three_jolt_diff = 0
    used_adapters = [] #keep track of how many adapters in our bag that we've used
    find_joltage(0, lines, used_adapters) #starting joltage is 0 (1st arg)
    return one_jolt_diff * three_jolt_diff #value we are looking for is |3-diff's| *|1-diff's|

def find_joltage(index, lines, used_adapters):
    global one_jolt_diff 
    global three_jolt_diff
    if(index == max(lines) and len(used_adapters) == len(lines)):
        three_jolt_diff += 1 #increment counter for 3-jolt diff
        return
    if(index + 1 in lines): #go to adapter with 1 more jolt if possible
        used_adapters.append(index + 1)
        one_jolt_diff += 1 #increment counter for 1-jolt diff
        index += 1
        find_joltage(index, lines, used_adapters)
    elif(index + 2 in lines): #otherwise take adapter with +2 jolt
        used_adapters.append(index + 2)
        index += 2
        find_joltage(index, lines, used_adapters)
    elif(index + 3 in lines): #otherwise take adapter with +3 jolt
        used_adapters.append(index + 3)
        index += 3
        three_jolt_diff += 1 #increment counter for 3-jolt diff
        find_joltage(index, lines, used_adapters)
    return 

if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 1856


