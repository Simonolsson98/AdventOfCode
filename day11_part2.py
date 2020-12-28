import time
import copy
def main():
    input = open("day11_input.txt")
    lines = []
    i = input.readline()
    while i: #get input into a list of strings
        lines.append(list(i[:len(i)-1]))
        i = input.readline()

if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 2180