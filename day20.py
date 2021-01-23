import time

def main():
    input = open("day20_input.txt")
    i = input.readline()    
    substr = ""
    while i: # get input into a list of lists
        substr = substr + i
        i = input.readline()
    grids = substr.split("\n\n")
    tiles = []
    for grid in grids:
        tiles.append(grid.split(":")[0].split(" ")[1])

    print(grids)
    print(tiles)



if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 