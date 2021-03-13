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
    indiv_grids = []
    for i in range(len(grids)):
        tiles.append(grids[i].split(":")[0].split(" ")[1])
        grids[i] = grids[i].split(":")[1]
        indiv_grids.append(grids[i].split("\n")[1:])

    
    return None

if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 
