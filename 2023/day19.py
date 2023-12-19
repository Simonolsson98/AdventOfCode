import os
import time
import math

result = 0
def part(part_num, start):
    with open(os.path.dirname(__file__)+"/day19_input.txt", 'r') as input_text:
        line = input_text.readline().rstrip()
        workflowdict = {}
        while line != "":
            removebraces = line[:-1].split("{")
            print(f"removebraces: {removebraces}")
            
            workflowdict[removebraces[0]] = removebraces[1].split(",")
            
            line = input_text.readline().rstrip()

        parts = input_text.readline().rstrip()
        while parts != "":
            removebraces = "".join(parts[:-1].split("{"))
            values = removebraces.split(",")
            for i in range(len(values)):
                values[i] = values[i][2:]

            #print(values)

            #print(workflowdict)
            currentdict = workflowdict["in"]
            while(True):
                for workflow in currentdict:
                    print(workflow)
                    # real rule
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
                        print(f"workflow: {workflow}")
                        valid = eval(workflow)

                        #print(f"valid: {valid}")
                        if(valid):
                            currentdict = workflowdict[asd[1]]
                            #print(currentdict)
                            break
                        else:
                            #currentdict = workflowdict




            parts = input_text.readline().rstrip()

        return result

start = time.time()
result = part("1", start)
print(f"day19: Python solution for part 1: {result}, time: {round(time.time() - start, 5)} s")
#print(f"day19: Python solution for part 2: {part2res}, time: {round(time.time() - start, 5)} s")