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
            infront.append(['........'])
            behind.append(['........'])

    print(f"LINES: {lines}")
    print(f"INFRONT: {infront}")
    print(f"BEHIND: {behind}")
    #return
    new_behind = behind
    new_infront = infront
    new_lines = lines
    cube_to_check = None
    neighbours = []
    for _ in range(6): #6 rounds
        for i in range(len(lines)):
            print(len(lines[i]))
            for j in range(8):
                print(f"i: {i}, j: {j}")
                try:
                    cube_to_check = lines[i][0][j]
                except IndexError:
                    pass
                try:
                    neighbours.append(lines[i][0][j+1])
                except IndexError:
                    pass                
                try:
                    if j-1 > 0:
                        neighbours.append(lines[i][0][j-1])    
                except IndexError:
                    pass
                try:
                    neighbours.append(lines[i+1][0][j+1])
                except IndexError:
                    pass
                try:
                    neighbours.append(lines[i+1][0][j])
                except IndexError:
                    pass
                try:
                    if j-1 > 0:
                        neighbours.append(lines[i+1][0][j-1])
                except IndexError:
                    pass
                try:
                    if i-1 >= 0:
                        neighbours.append(lines[i-1][0][j+1])
                except IndexError:
                    pass
                try:
                    if i-1 >= 0:
                        neighbours.append(lines[i-1][0][j])    
                except IndexError:
                    pass
                try:
                    if j-1 > 0 and i-1 >= 0:
                        neighbours.append(lines[i-1][0][j-1])
                except IndexError:
                    pass
                try:
                    neighbours.append(infront[i][0][j+1])
                except IndexError:
                    pass
                try:
                    neighbours.append(infront[i][0][j])
                except IndexError:
                    pass
                try:
                    if j-1 > 0:
                        neighbours.append(infront[i][0][j-1])
                except IndexError:
                    pass
                try:
                    neighbours.append(infront[i+1][0][j+1])
                except IndexError:
                    pass
                try:
                    neighbours.append(infront[i+1][0][j])
                except IndexError:
                    pass
                try:
                    if j-1 > 0 and i-1 >= 0:
                        neighbours.append(infront[i+1][0][j-1])
                except IndexError:
                    pass
                try:
                    if i-1 >= 0:
                        neighbours.append(infront[i-1][0][j+1])
                except IndexError:
                    pass
                try:
                    if i-1 >= 0:
                        neighbours.append(infront[i-1][0][j])
                except IndexError:
                    pass
                try:
                    if j-1 >= 0 and i-1 >= 0:
                        neighbours.append(infront[i-1][0][j-1])
                except IndexError:
                    pass
                try:
                    neighbours.append(behind[i][0][j+1])
                except IndexError:
                    pass
                try:
                    neighbours.append(behind[i][0][j])
                except IndexError:
                    pass
                try:
                    if j-1 >= 0:
                        neighbours.append(behind[i][0][j-1])
                except IndexError:
                    pass
                try:
                    neighbours.append(behind[i+1][0][j+1])
                except IndexError:
                    pass
                try:
                    neighbours.append(behind[i+1][0][j])
                except IndexError:
                    pass
                try:
                    if j-1 >= 0:
                        neighbours.append(behind[i+1][0][j-1])
                except IndexError:
                    pass
                try:
                    if i-1 >= 0:
                        neighbours.append(behind[i-1][0][j+1])
                except IndexError:
                    pass
                try:
                    if i-1 >= 0:
                        neighbours.append(behind[i-1][0][j])
                except IndexError:
                    pass
                try:
                    if j-1 >= 0 and i-1 >= 0:
                        neighbours.append(behind[i-1][0][j-1])
                except IndexError:
                    pass

                print(f"NEIGHBOURCOUNT: {neighbours.count('#')} and number of neighbours: {len(neighbours)} ")
                print(neighbours)
                print(behind)
                if(cube_to_check == "#" and neighbours.count("#") == 2 or neighbours.count("#") == 3):
                    print("DID NUFFIN")
                elif(cube_to_check == "." and neighbours.count("#") == 3):
                    print("GOT INACTIVE")
                    new_lines[i][j][j] = "."
                neighbours = [] #reset for next cube

                cube_to_check = behind[i][0][j]
                try:
                    if j-1 >= 0:
                        neighbours.append(behind[i][0][j-1])
                except IndexError:
                    pass
                try:    
                    neighbours.append(behind[i][0][j+1])
                except IndexError:
                    pass
                try:
                    if j-1 >= 0 and i-1 >= 0:
                        neighbours.append(behind[i-1][0][j-1])
                except IndexError:
                    pass
                try:    
                    if i-1 >= 0:
                        neighbours.append(behind[i-1][0][j+1])
                except IndexError:
                    pass
                try:    
                    if i-1 >= 0:
                        neighbours.append(behind[i-1][0][j])
                except IndexError:
                    pass
                try:
                    if j-1 >= 0:
                        neighbours.append(behind[i+1][0][j-1])
                except IndexError:
                    pass
                try:    
                    neighbours.append(behind[i+1][0][j+1])
                except IndexError:
                    pass
                try:    
                    neighbours.append(behind[i+1][0][j])
                except IndexError:
                    pass
                try:
                    neighbours.append(lines[i][0][j+1])
                except IndexError:
                    pass  
                try:
                    neighbours.append(lines[i][0][j])
                except IndexError:
                    pass                
                try:
                    if j-1 > 0:
                        neighbours.append(lines[i][0][j-1])    
                except IndexError:
                    pass
                try:
                    neighbours.append(lines[i+1][0][j+1])
                except IndexError:
                    pass
                try:
                    neighbours.append(lines[i+1][0][j])
                except IndexError:
                    pass
                try:
                    if j-1 > 0:
                        neighbours.append(lines[i+1][0][j-1])
                except IndexError:
                    pass
                try:
                    if i-1 >= 0:
                        neighbours.append(lines[i-1][0][j+1])
                except IndexError:
                    pass
                try:
                    if i-1 >= 0:
                        neighbours.append(lines[i-1][0][j])    
                except IndexError:
                    pass
                try:
                    if j-1 > 0 and i-1 >= 0:
                        neighbours.append(lines[i-1][0][j-1])
                except IndexError:
                    pass

                #print(f"NEIGHBOURCOUNT: {neighbours.count('#')} and number of neighbours: {len(neighbours)} ")
                #print(neighbours)
                if(cube_to_check == "#" and neighbours.count("#") == 2 or neighbours.count("#") == 3):
                    print("DID NUFFIN")
                elif(cube_to_check == "." and neighbours.count("#") == 3):
                    print("GOT INACTIVE")
                    new_behind[i][j][j] = "."
                neighbours = []

                cube_to_check = str(infront[i][0])[j]
                try:
                    if j-1 >= 0:
                        neighbours.append(infront[i][0][j-1])
                except IndexError:
                    pass
                try:    
                    neighbours.append(infront[i][0][j+1])
                except IndexError:
                    pass
                try:
                    if j-1 >= 0 and i-1 >= 0:
                        neighbours.append(infront[i-1][0][j-1])
                except IndexError:
                    pass
                try:    
                    if i-1 >= 0:
                        neighbours.append(infront[i-1][0][j+1])
                except IndexError:
                    pass
                try:    
                    if i-1 >= 0:
                        neighbours.append(infront[i-1][0][j])
                except IndexError:
                    pass
                try:
                    if j-1 >= 0:
                        neighbours.append(infront[i+1][0][j-1])
                except IndexError:
                    pass
                try:    
                    neighbours.append(infront[i+1][0][j+1])
                except IndexError:
                    pass
                try:    
                    neighbours.append(infront[i+1][0][j])
                except IndexError:
                    pass
                try:
                    neighbours.append(lines[i][0][j+1])
                except IndexError:
                    pass  
                try:
                    neighbours.append(lines[i][0][j])
                except IndexError:
                    pass                
                try:
                    if j-1 > 0:
                        neighbours.append(lines[i][0][j-1])    
                except IndexError:
                    pass
                try:
                    neighbours.append(lines[i+1][0][j+1])
                except IndexError:
                    pass
                try:
                    neighbours.append(lines[i+1][0][j])
                except IndexError:
                    pass
                try:
                    if j-1 > 0:
                        neighbours.append(lines[i+1][0][j-1])
                except IndexError:
                    pass
                try:
                    if i-1 >= 0:
                        neighbours.append(lines[i-1][0][j+1])
                except IndexError:
                    pass
                try:
                    if i-1 >= 0:
                        neighbours.append(lines[i-1][0][j])    
                except IndexError:
                    pass
                try:
                    if j-1 > 0 and i-1 >= 0:
                        neighbours.append(lines[i-1][0][j-1])
                except IndexError:
                    pass
                
                #print(f"NEIGHBOURCOUNT: {neighbours.count('#')} and number of neighbours: {len(neighbours)} ")
                #print(neighbours)
                if(cube_to_check == "#" and neighbours.count("#") == 2 or neighbours.count("#") == 3):
                    print("DID NUFFIN")
                elif(cube_to_check == "." and neighbours.count("#") == 3):
                    print("GOT INACTIVE")
                    new_infront[i][j][j] = "."
                neighbours = []

                lines = new_lines
                behind = new_behind
                infront = new_infront

    count = 0
    for i in range(len(lines)):
        count += lines[i].count("#")
    
    print(lines)
    return count

if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer 