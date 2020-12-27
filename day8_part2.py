import sys
import time
import copy
def main():
    sys.setrecursionlimit(10**6)
    input = open("day8_input.txt")
    acc_value = 0
    instruction_pointer = 0 
    lines = []
    i = input.readline()
    
    while i: #get input into a list of strings
        lines.append([i, False])
        i = input.readline()

    return try_changes(lines)

def try_changes(orig_lines):
    already_checked = []
    instruction_pointer = 0
    acc_value = 0
    index_to_change = 0
    while True:
        lines = copy.deepcopy(orig_lines) #memory heavy but needed I believe
        instr = lines[index_to_change][0][:3]
        while(instr in already_checked or instr == "acc"):
            index_to_change += 1
            instr = lines[index_to_change][0][:3]
        if instr == "jmp":
            lines[index_to_change][0] = "nop" + lines[index_to_change][0][3:]
            already_checked.append(lines[index_to_change][0])
            index_to_change += 1
        else: #instr == "nop"
            lines[index_to_change][0] = "jmp" + lines[index_to_change][0][3:]
            already_checked.append(lines[index_to_change][0])
            index_to_change += 1
        while True:
            try:
                instruction = lines[instruction_pointer][0][:3]
            except IndexError: #if we get here, 
                return acc_value
            if(lines[instruction_pointer][1] == True):
                acc_value = 0
                instruction_pointer = 0
                for j in range(len(lines)):
                    lines[j][1] = False
                break
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
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 892
