import time
import copy
def main():
    input = open("day11_input.txt")
    lines = []
    i = input.readline()
    while i: #get input into a list of strings
        lines.append(list(i[:len(i)-1]))
        i = input.readline()

    new_lines = copy.deepcopy(lines) #the list used to check if a round changed our starting list
    stopped_changing_or_not = 0
    while True:
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                seat = lines[i][j]
                occupied_seats = get_occupied_seats(lines, i, j, [], stopped_changing_or_not)

                if seat == 'L' and '#' not in occupied_seats:
                    stopped_changing_or_not = 0
                    new_lines[i][j] = '#'
                elif seat == '#' and occupied_seats.count('#') >= 4:
                    stopped_changing_or_not = 0
                    new_lines[i][j] = 'L'
                else: #seat = '.' 
                    stopped_changing_or_not += 1
                    continue
                occupied_seats.clear()
        if lines == new_lines: #no change from 1 round, so we should stop
            result = 0
            for k in range(len(new_lines)):
                result += new_lines[k].count('#') #count occurrences of # in every line
            return result
        else: #prepare for next round
            lines = copy.deepcopy(new_lines)


def get_occupied_seats(lines, rowindex, colindex, occupied_seats, stop):
    #print(stop)
    if(colindex - 1 < 0):
        pass
    else:
        occupied_seats.append(lines[rowindex][colindex-1])

    if colindex + 1 > len(lines[rowindex]) - 1:
        pass
    else:
        occupied_seats.append(lines[rowindex][colindex+1])

    if(colindex - 1 < 0 or rowindex + 1 > len(lines) - 1):
        pass
    else:
        occupied_seats.append(lines[rowindex+1][colindex-1])
            
    if(rowindex + 1 > len(lines) - 1 or colindex + 1 > len(lines[rowindex + 1]) - 1):
        pass
    else:
        occupied_seats.append(lines[rowindex+1][colindex+1])

    if(rowindex + 1 > len(lines) - 1 or colindex > len(lines[rowindex + 1]) - 1):
        pass
    else:
        occupied_seats.append(lines[rowindex+1][colindex])

    if(rowindex - 1 < 0 or colindex + 1 > len(lines[rowindex - 1]) - 1):
        pass
    else:
        occupied_seats.append(lines[rowindex-1][colindex+1])

    if(rowindex - 1 < 0 or colindex - 1 < 0):
        pass
    else:
        occupied_seats.append(lines[rowindex-1][colindex-1])

    if(rowindex - 1 < 0):
        pass
    else: 
        occupied_seats.append(lines[rowindex-1][colindex])

    return occupied_seats

if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 2489


