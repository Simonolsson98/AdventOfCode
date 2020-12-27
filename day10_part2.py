import time

def main():
    input = open("day10_input.txt")
    lines = []
    i = input.readline()
    
    while i: #get input into a list of strings
        lines.append(int(i))
        i = input.readline()

    lines.sort()
    global possible_arrangements # keep track of possible arrangements
    
    possible_arrangements = 0
    print(lines)
    used_adapters = [] #keep track of how many adapters in our bag that we've used
    find_joltage(0, lines, used_adapters) #starting joltage is 0 (1st arg)
    return possible_arrangements 

def find_joltage(index, lines, used_adapters): #this is waaaaaaaaaaay too slow, unlucky so rip
    global possible_arrangements
    if(index == max(lines) and len(used_adapters) == len(lines)):
        possible_arrangements += 1
        return 
    if(index + 1 in lines): #go to adapter with 1 more jolt if possible
        used_adapters.append(index + 1)
        index += 1
        find_joltage(index, lines, used_adapters)
    if(index + 2 in lines): #otherwise take adapter with +2 jolt
        used_adapters.append(index + 2)
        index += 2
        find_joltage(index, lines, used_adapters)
    if(index + 3 in lines): #otherwise take adapter with +3 jolt
        used_adapters.append(index + 3)
        index += 3
        find_joltage(index, lines, used_adapters)
    return 

if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #



