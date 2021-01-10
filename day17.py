from os import remove
import time

def main():
    input = open("day17_input.txt")
    lines = []
    i = input.readline()
    
    while i: # get input into a list of lists
        lines.append([i[:-1]])
        i = input.readline()

    print(lines)    


if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer 