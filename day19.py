import time

def main():
    input = open("day19_input.txt")
    i = input.readline()   
    lines = []
    while i:
        lines.append(i)
        i = input.readline()
    
    rules = lines.split("\n\n")[0]
    messages = lines.split("\n\n")[1]


if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer =