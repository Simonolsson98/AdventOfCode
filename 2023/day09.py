import os
import time
start = time.time()

def EqualElementsInList(lst):
    ele = lst[0]
    for item in lst:
        if ele != item:
            return False
    return True

def part():
    result = 0
    part2result = 0
    with open(os.path.dirname(__file__)+"/day09_input.txt", 'r') as input_text:
        for line in input_text:
            last_values = []
            first_values = []
            history = list(map(int, line.rstrip("\n").split(" ")))
            last_values.append(history[-1])
            first_values.append(history[0])
            while not EqualElementsInList(history):
                temp = []
                for i in range(len(history) - 1):
                    diff = history[i+1] - history[i]
                    temp.append(diff)
                history = temp
                last_values.append(history[-1])
                first_values.append(history[0])
            
            first_values = first_values[::-1]
            while len(first_values) > 1:
                first_values[0] = first_values[1] - first_values[0]
                first_values.remove(first_values[1])

            result += sum(last_values)
            part2result += first_values[0]
    
    return result, part2result


result, part2result = part()
print(f"day9: Python solution for part 1: {result}, time: {round(time.time() - start, 5)} s")
print(f"day9: Python solution for part 2: {part2result}, time: {round(time.time() - start, 5)} s")