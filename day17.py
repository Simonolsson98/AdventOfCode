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

    neighbours = []
    
    for _ in range(6): #6 rounds
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                try:
                    cube_to_check = lines[i][j]
                    neighbours.append(lines[i][j+1][j+1])
                    neighbours.append(lines[i][j-1][j-1])
                    
                    neighbours.append(lines[i+1][j+1])
                    neighbours.append(lines[i+1][j])
                    neighbours.append(lines[i+1][j-1])

                    neighbours.append(lines[i-1][j+1])
                    neighbours.append(lines[i-1][j])    
                    neighbours.append(lines[i-1][j-1])

                    neighbours.append(infront[i][j+1])
                    neighbours.append(infront[i][j])
                    neighbours.append(infront[i][j-1])
                    neighbours.append(infront[i+1][j+1])
                    neighbours.append(infront[i+1][j])
                    neighbours.append(infront[i+1][j-1])
                    neighbours.append(infront[i-1][j+1])
                    neighbours.append(infront[i-1][j])
                    neighbours.append(infront[i-1][j-1])

                    neighbours.append(behind[i][j+1])
                    neighbours.append(behind[i][j])
                    neighbours.append(behind[i][j-1])
                    neighbours.append(behind[i+1][j+1])
                    neighbours.append(behind[i+1][j])
                    neighbours.append(behind[i+1][j-1])
                    neighbours.append(behind[i-1][j+1])
                    neighbours.append(behind[i-1][j])
                    neighbours.append(behind[i-1][j-1])
                except IndexError:
                    pass
                print(neighbours)

                print(neighbours.count("#"))



if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer 