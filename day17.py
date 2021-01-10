from os import remove
import time

def main():
    input = open("day17_input.txt")
    lines = []
    i = input.readline()
    
    while i: # get input into a list of lists
        if(i[-1] == "\n"):
            lines.append([i[:-1]])
        else:
            lines.append([i])
        i = input.readline()
    behind = []
    infront = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            infront.append(["........"])
            behind.append(["........"])

    new_behind = []
    new_infront = []

    active_neighbours = 0
    for _ in range(6): #6 rounds
        

if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer 