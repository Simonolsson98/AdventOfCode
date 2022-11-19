import sys
import time

def main():
    input = open("day8_input.txt")
    acc_value = 0
    instruction_pointer = 0 
    lines = []
    i = input.readline()
    
    while i: #get input into a list of strings
        lines.append([i, False])
        i = input.readline()

    while True:
        instruction = lines[instruction_pointer][0][:3] 
        if(lines[instruction_pointer][1] == True):
            return acc_value
        if instruction == "acc":
            lines[instruction_pointer][1] = True
            acc_value += int(lines[instruction_pointer][0][4:])
            instruction_pointer += 1

        elif instruction == "jmp":
            lines[instruction_pointer][1] = True 

            instruction_pointer += int(lines[instruction_pointer][0][4:])
        
        else: #nop
            lines[instruction_pointer][1] = True
            instruction_pointer += 1

if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 1671
