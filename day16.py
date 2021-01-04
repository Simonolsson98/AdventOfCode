import time

def main():
    input = open("day16_input.txt")
    lines = []
    i = input.readline()
    
    while i: #get input into a list of strings
        lines.append(int(i))
        i = input.readline()

    
if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 1373