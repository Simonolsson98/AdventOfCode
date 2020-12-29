import time
import copy
def main():
    input = open("day11_input.txt")
    lines = []
    i = input.readline()
    while i: #get input into a list of strings
        lines.append(list(i[:len(i)-1]))
        i = input.readline()

    #deepcopy needed here, since lines is a list of lists
    new_lines = copy.deepcopy(lines) #the list used to check if a round changed our starting list
    
    while True:
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                seat = lines[i][j]
                neighbouring_seats = get_occupied_seats(lines, i, j, []) #retrieve the neighbouring seats

                if seat == 'L' and '#' not in neighbouring_seats:
                    new_lines[i][j] = '#' #seat should be occupied
                elif seat == '#' and neighbouring_seats.count('#') >= 4:
                    new_lines[i][j] = 'L' #seat gets freed
                else: #seat = '.' or both of the above requirements were not met
                    pass

        if lines == new_lines: #no change from the round that just executed, so we should stop
            result = 0
            for k in range(len(new_lines)):
                result += new_lines[k].count('#') #count occurrences of # in every line
            return result
        else: #prepare for next round
            lines = copy.deepcopy(new_lines)#deepcopy needed here, since lines is a list of lists


def get_occupied_seats(lines, row_index, col_index, neighbouring_seats): #function that returns a list of all occupied neighbouring seats
    #checks for all types of indices, also makes sure that for example the first element only has 3 neighbours, since L # gives ['#', '.', '#'] for L
    #                                                                                                                 . #   
    
    if(col_index - 1 < 0):
        pass
    else:
        neighbouring_seats.append(lines[row_index][col_index-1])
    try:
        neighbouring_seats.append(lines[row_index][col_index+1])
    except IndexError:
        pass
    if(col_index - 1 < 0 or row_index + 1 > len(lines) - 1):
        pass
    else:
        neighbouring_seats.append(lines[row_index+1][col_index-1])
    try:
        neighbouring_seats.append(lines[row_index+1][col_index+1])
    except IndexError:
        pass
    try:
        neighbouring_seats.append(lines[row_index+1][col_index])
    except IndexError:
        pass

    if(row_index - 1 < 0 or col_index + 1 > len(lines[row_index - 1]) - 1):
        pass
    else:
        neighbouring_seats.append(lines[row_index-1][col_index+1])
    if(row_index - 1 < 0 or col_index - 1 < 0):
        pass
    else:
        neighbouring_seats.append(lines[row_index-1][col_index-1])
    if(row_index - 1 < 0):
        pass
    else: 
        neighbouring_seats.append(lines[row_index-1][col_index])

    return neighbouring_seats

if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 2489
