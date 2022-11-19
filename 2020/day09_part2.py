import time

def main():
    input = open("day9_input.txt")
    resulting_numbers = set()
    lines = []
    i = input.readline()
    result_val = 0
    while i: #get input into a list of strings
        lines.append(i)
        i = input.readline()
    
    for k in range(25, len(lines)): #checking each number from 25 and onwards
        for i in range(k - 25, k): 
            for j in range(k - 25, k):
                if(i != j):
                    resulting_numbers.add(int(lines[i]) + int(lines[j])) #sum all previous 25 numbers and add them to a set
        if int(lines[k]) not in resulting_numbers: #if a number is not in this set, we have found the result
            result_val = int(lines[k])
        resulting_numbers.clear() #else we reset and check next number (next iteration of k)

    for i in range(len(lines)):
        index = i #index to be used to sum all values lines[i] + lines[i+1] + ...
        check = 0 #reset value for each iteration
        numbers_to_be_added = []
        while check < result_val:
            check += int(lines[index]) 
            numbers_to_be_added.append(int(lines[index])) #to be able to find the minimum and maximum values below
            index += 1 #increase index
            if check == result_val: #if the sum is correct...
                return max(numbers_to_be_added) + min(numbers_to_be_added) #... just sum minimum and maximum value and we are done


if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 76096372

