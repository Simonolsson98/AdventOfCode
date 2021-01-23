import time

def main():
    input = open("day20_input.txt")
    i = input.readline()    
    result = 0
    substr = ""
    iter = 1
    while i: # get input into a list of lists
        for j in range(len(i)):
            substr = substr + i[j]



if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 