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
    
    all_edges = right_col + left_col + top_row + bottom_row

    top_left_index = 0
    top_right_index = 0
    bottom_right_index = 0
    bottom_left_index = 0
    for each_grid in indiv_grids: #adding each edge to lists for further checks
        left_col_check = ""
        right_col_check = ""
        top_row = each_grid[0]
        bottom_row = each_grid[-1]
        for row in each_grid:
            left_col_check = left_col_check + row[0]
            right_col_check = right_col_check + row[-1]

        if all_edges.count(top_row) == 1 and all_edges.count(left_col_check):
            top_left_index = indiv_grids.index(each_grid)
        elif all_edges.count(top_row) == 1 and all_edges.count(right_col_check):
            top_right_index = indiv_grids.index(each_grid)
        elif all_edges.count(bottom_row) == 1 and all_edges.count(right_col_check):
            bottom_right_index = indiv_grids.index(each_grid)
        elif all_edges.count(bottom_row) == 1 and all_edges.count(left_col_check):
            bottom_left_index = indiv_grids.index(each_grid)
        
    return


if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 