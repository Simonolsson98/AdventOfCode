import math
def main():
    input = open("day5_input.txt")
    row_num = -1
    col_num = -1
    seat_ids = [] #list to store busy seat ids

    line = input.readline()
    while line:
        row_max = 127
        col_max = 7
        row_min = 0
        col_min = 0

        rowRange = range(row_min, row_max)
        colRange = range(col_min, col_max)
        
        while line:
            character = line[0] #first character
            line = line[1:] #"pop" first character from the next string, for example BFBFBFBRLR -> FBFBFBRLR
            if character == 'B': #if B, example: 0-127 -> 64-127
                row_min = math.ceil((row_max - row_min)/2) + row_min
                rowRange = range(row_min, row_max)
            elif character == 'F': #if F, example: 0-127 -> 0-63
                row_max = math.floor((row_max - row_min)/2) + row_min
                rowRange = range(row_min, row_max)      
            elif character == 'L': #if L, example: 0-7 -> 0-3
                col_max = math.floor((col_max - col_min)/2) + col_min
                colRange = range(col_min, col_max)
            elif character == 'R': #if R, example: 0-7 -> 4-7
                col_min = math.ceil((col_max - col_min)/2) + col_min
                colRange = range(col_min, col_max)

        if(len(rowRange) == 0):
            row_num = row_max #row_max == row_min so either is fine
        if(len(colRange) == 0):
            col_num = col_max #col_max == col_min so either is fine 

        seat_ids.append(row_num * 8 + col_num) #store busy seat ids in a list
        line = input.readline()
    
    for i in range(0, len(seat_ids)-1):
        if i not in seat_ids:
            if i+1 not in seat_ids or i-1 not in seat_ids: #according to spec, filters out the empty seats at the front/back
                continue
            else:
                return i # answer = 741

    return -1 #all seats busy if we end up here


if __name__ == '__main__':
    returnVal = main()
    print(returnVal)