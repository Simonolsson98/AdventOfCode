import os
import time
import math

result = 0
def part(part_num):
    with open(os.path.dirname(__file__)+"/day19_input.txt", 'r') as input_text:
        line = input_text.readline().rstrip()
        global workflowdict
        workflowdict = {}
        while line != "":
            removebraces = line[:-1].split("{")
            workflowdict[removebraces[0]] = removebraces[1].split(",")
            line = input_text.readline().rstrip()

        if part_num == "2":
            currentdict = workflowdict["in"]
            checkworkflow(currentdict, [])

        elif(part_num == "1"):
            parts = input_text.readline().rstrip()
            winning = [(0, 0), (0, 0), (0, 0), (0, 0)]
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

def checkworkflow(workflowline, winning):
    for workflow in workflowline:
        if('<' in workflow or '>' in workflow or '=' in workflow):
            split = workflow.split(":")
            newrange = split[0][1:]
            if(split[1] == "A")
                if(split[0][0] == 'x'):
                    if '<' in split[0] and newrange < winning[0][1]:
                        winning[0][1] = newrange
                    elif '>' in split[0] and newrange > winning[0][0]:
                        winning[0][0] = newrange:
                    else: #"=" in split[0] 
                        pass
                elif(split[0][0] == 'm'):
                    if '<' in split[0] and newrange < winning[1][1]:
                        winning[1][1] = newrange
                    elif '>' in split[0] and newrange > winning[1][0]:
                        winning[1][0] = newrange:
                    else: #"=" in split[0] 
                        pass
                elif(split[0][0] == 'a'):
                    if '<' in split[0] and newrange < winning[2][1]:
                        winning[2][1] = newrange
                    elif '>' in split[0] and newrange > winning[2][0]:
                        winning[2][0] = newrange:
                    else: #"=" in split[0] 
                        pass
                elif(split[0][0] == 's'):
                    if '<' in split[0] and newrange < winning[3][1]:
                        winning[3][1] = newrange
                    elif '>' in split[0] and newrange > winning[3][0]:
                        winning[3][0] = newrange:
                    else: #"=" in split[0] 
                        pass
            elif(split[1] == "R")
                pass
            else:
                checkworkflow(workflowdict[split[1]])


#start = time.time()
#print(f"day19: Python solution for part 1: {part('1')}, time: {round(time.time() - start, 5)} s")
start = time.time()
print(f"day19: Python solution for part 2: {part('2')}, time: {round(time.time() - start, 5)} s")