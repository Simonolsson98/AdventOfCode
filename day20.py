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
        top_row.append(each_grid[0][::-1])
        bottom_row.append(each_grid[-1])
        bottom_row.append(each_grid[-1][::-1])
        tempR = ""
        tempL = ""
        for row in each_grid:
            tempR = tempR + row[-1]
            tempL = tempL + row[0]
        right_col.append(tempR)
        right_col.append(tempR[::-1])
        left_col.append(tempL)
        left_col.append(tempL[::-1])
    
    all_edges = right_col + left_col + top_row + bottom_row
    indices = []

    for each_grid in indiv_grids: #adding each edge to lists for further checks
        left_col_check = ""
        right_col_check = ""
        top_row = each_grid[0]
        bottom_row = each_grid[-1]
        for row in each_grid:
            right_col_check = right_col_check + row[-1]
            left_col_check = left_col_check + row[0]
        
        if all_edges.count(top_row) == 1:
            if all_edges.count(right_col_check) == 1 or all_edges.count(left_col_check) == 1:
                indices.append(indiv_grids.index(each_grid))
        
        elif all_edges.count(top_row[::-1]):
            if all_edges.count(right_col_check) == 1 or all_edges.count(left_col_check) == 1:
                indices.append(indiv_grids.index(each_grid))

        elif all_edges.count(right_col_check) == 1:
            if all_edges.count(top_row) == 1 or all_edges.count(bottom_row) == 1:
                indices.append(indiv_grids.index(each_grid))
        
        elif all_edges.count(right_col_check[::-1]) == 1:
            if all_edges.count(top_row) == 1 or all_edges.count(bottom_row) == 1:
                indices.append(indiv_grids.index(each_grid))
        
        elif all_edges.count(left_col_check) == 1:
            if all_edges.count(top_row) == 1 or all_edges.count(bottom_row) == 1:
                indices.append(indiv_grids.index(each_grid))
        
        elif all_edges.count(left_col_check[::-1]) == 1:
            if all_edges.count(top_row) == 1 or all_edges.count(bottom_row) == 1:
                indices.append(indiv_grids.index(each_grid))
        
        elif all_edges.count(bottom_row) == 1:
            if all_edges.count(left_col_check) == 1 or all_edges.count(right_col_check) == 1:
                indices.append(indiv_grids.index(each_grid))
        
        elif all_edges.count(bottom_row[::-1]) == 1:
            if all_edges.count(left_col_check) == 1 or all_edges.count(right_col_check) == 1:
                indices.append(indiv_grids.index(each_grid))

    print(indices)
    print(tiles[indices[0]])
    print(tiles[indices[1]])
    print(tiles[indices[2]])
    print(tiles[indices[3]])
    return int(tiles[indices[0]]) * int(tiles[indices[1]]) * int(tiles[indices[2]]) * int(tiles[indices[3]])


if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer < 24552019533359 