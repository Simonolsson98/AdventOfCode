import time

def main():
    input = open("day9_input.txt")
    resulting_numbers = set()
    lines = []
    i = input.readline()
    
    while i: #get input into a list of strings
        lines.append(i)
        i = input.readline()
    
    for k in range(25, len(lines)): #checking each number from 25 and onwards
        for i in range(k - 25, k): 
            for j in range(k - 25, k):
                if(i != j): #dont allow the sum of two equal values
                    resulting_numbers.add(int(lines[i]) + int(lines[j])) #sum all previous 25 numbers and add them to a set
        
        if int(lines[k]) not in resulting_numbers: #if a number is not in this set, we have found the result
            return int(lines[k])
        resulting_numbers.clear() #else we reset and check next number (next iteration of k)
if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 556543474


