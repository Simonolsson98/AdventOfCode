import os
import time
import math

result = 0
def part(part_num):
    with open(os.path.dirname(__file__)+"/day19_input.txt", 'r') as input_text:
        line = input_text.readline().rstrip()
        workflowdict = {}
        while line != "":
            removebraces = line[:-1].split("{")
            workflowdict[removebraces[0]] = removebraces[1].split(",")
            line = input_text.readline().rstrip()

        if(part_num == "1"):
            parts = input_text.readline().rstrip()
            winning = []
            while parts != "":
                removebraces = "".join(parts[:-1].split("{"))
                values = removebraces.split(",")
                for i in range(len(values)):
                    values[i] = values[i][2:]

                currentdict = workflowdict["in"]
                breakouter = False
                i = 0
                while(True):
                    workflow = currentdict[i]

                    if('<' in workflow or '>' in workflow or '=' in workflow):
                        if(workflow[0] == 'x'):
                            check = values[0]
                        elif(workflow[0] == 'm'):
                            check = values[1]
                        elif(workflow[0] == 'a'):
                            check = values[2]
                        elif(workflow[0] == 's'):
                            check = values[3]

                        asd = workflow.split(":")
                        workflow = check + asd[0][1:]
                        valid = eval(workflow)
                        if(valid):
                            if(asd[1] == "A"):
                                winning.append(sum([int(x) for x in values]))
                                break
                            elif(asd[1] == "R"):
                                break
                            else:
                                currentdict = workflowdict[asd[1]]
                                i = 0
                            
                        else:
                            i += 1
                    else:
                        if(workflow == "A"):
                            winning.append(sum([int(x) for x in values]))
                            break
                        elif(workflow == "R"):
                            break
                        else:
                            currentdict = workflowdict[workflow]
                            i = 0

                parts = input_text.readline().rstrip()

        return sum(winning)

start = time.time()
print(f"day19: Python solution for part 1: {part('1')}, time: {round(time.time() - start, 5)} s")
start = time.time()
#print(f"day19: Python solution for part 2: {part('2')}, time: {round(time.time() - start, 5)} s")