import time

def main():
    input = open("day20_input.txt")
    i = input.readline()    
    substr = ""
    while i: # get input into a list of lists
        substr = substr + i
    grids = substr.split("\n")
    



if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 