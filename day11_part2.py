import time
import copy
def main():
    input = open("day11_input.txt")
    lines = []
    i = input.readline()
    while i: #get input into a list of strings
        lines.append(list(i))
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
                elif seat == '#' and neighbouring_seats.count('#') >= 5:
                    new_lines[i][j] = 'L' #seat gets freed
                else: #seat = '.' or neither of the above requirements were met
                    pass

        if lines == new_lines: #no change from the round that just executed, so we should stop
            result = 0
            for k in range(len(new_lines)):
                result += new_lines[k].count('#') #count occurrences of # in every line
            return result
        else: #prepare for next round
            lines = copy.deepcopy(new_lines) #deepcopy needed here, since lines is a list of lists


def get_occupied_seats(lines, row_index, col_index, neighbouring_seats): #function that returns a list of all occupied neighbouring seats
    #checks for all types of indices, also makes sure that for example the first element only has 3 neighbours, since L # gives ['#', '.', '#'] for L
    #                                                                                                                 . #   
    try: #left neighbour
        i = 1
        while(lines[row_index][col_index - i] == '.' and col_index - i > 0): # col_index - i > 0 to prevent "wrapping around" the list
            i += 1 
        if col_index > 0: #furthest left node cant have left neighbour
            neighbouring_seats.append(lines[row_index][col_index-i])
    except IndexError:
        pass

    try: #right neighbour
        i = 1
        while(lines[row_index][col_index + i] == '.'):
            i += 1 
        neighbouring_seats.append(lines[row_index][col_index+i])

    except IndexError:
        pass

    try: #bottom-left neighbour
        i = 1
        while(lines[row_index + i][col_index - i] == '.' and col_index - i > 0): # col_index - i > 0 to prevent "wrapping around" the list
            i += 1 
        if col_index > 0 and row_index < len(lines) - 1: #furthest left node cant have bottom-left neighbour
            neighbouring_seats.append(lines[row_index + i][col_index - i])
    except IndexError:
        pass
        
    try: #bottom-right neighbour
        i = 1
        while(lines[row_index + i][col_index + i] == '.'):
            i += 1 
        neighbouring_seats.append(lines[row_index+i][col_index+i])
    except IndexError:
        pass

    try: #bottom neighbour
        i = 1
        while(lines[row_index + i][col_index] == '.'):
            i += 1 
        neighbouring_seats.append(lines[row_index+i][col_index])
    except IndexError:
        pass

    try: #top-right neighbour
        i = 1
        while(lines[row_index - i][col_index + i] == '.' and row_index - i > 0): # row_index - i > 0 to prevent "wrapping around" the list
            i += 1 
        if row_index > 0: #node in top row (row_index == 0) cant have top-right neighbour
            neighbouring_seats.append(lines[row_index-i][col_index+i])
    except IndexError:
        pass

    try: #top-left neighbour
        i = 1
        while(lines[row_index - i][col_index - i] == '.' and row_index - i > 0 and col_index - i > 0):# row_index (and col_index) - i > 0 to prevent "wrapping around" the list
            i += 1 
        if col_index > 0 and row_index > 0: #node in left col cant have top-left neighbour / node in top row cant have top-left neighbour
            neighbouring_seats.append(lines[row_index-i][col_index-i])
    except IndexError:
        pass

    try: #top neighbour
        i = 1
        while(lines[row_index - i][col_index] == '.' and row_index - i > 0): 
            i += 1 
        if row_index > 0: #node in top row cant have top neighbour
            neighbouring_seats.append(lines[row_index-i][col_index])
    except IndexError:
        pass
    return neighbouring_seats

if __name__ == '__main__':
    times = []
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 2180
