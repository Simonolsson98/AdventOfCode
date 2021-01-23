import time

def main():
    input = open("day20_input.txt")
    i = input.readline()    
    substr = ""
    while i: # get input into a list of lists
        #i = i[:-1]
        substr = substr + i
        i = input.readline()
    grids = substr.split("\n\n")
    tiles = []
    top_row = []
    bottom_row = []
    right_col = []
    left_col = []
    indiv_grids = []
    for i in range(len(grids)):
        tiles.append(grids[i].split(":")[0].split(" ")[1])
        grids[i] = grids[i].split(":")[1]
        indiv_grids.append(grids[i].split("\n")[1:])

    for each_grid in indiv_grids: #adding each edge to lists for further checks
        top_row.append(each_grid[0])
        bottom_row.append(each_grid[-1])
        tempR = ""
        tempL = ""
        for row in each_grid:
            tempR = tempR + row[-1]
            tempL = tempL + row[0]
        right_col.append(tempR)
        left_col.append(tempL)

    print(right_col)
    all_edges = right_col + left_col + top_row + bottom_row

    #for each grid, check top and left edges if they have matching pairs...
    return


if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 