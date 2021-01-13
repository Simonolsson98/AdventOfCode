import time

def main():
    input = open("day19_input.txt")
    i = input.readline()   
    while i:

        i = input.readline()


if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer =