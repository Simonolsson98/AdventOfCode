import time

def main():
    input = open("day14_input.txt")
    i = input.readline()
    changed_vals = {}
    mask = ""
    while i:
        if i[0:4] == "mask":
            mask = i[7:]
            i = input.readline()
            continue
        
        index = i.split(" = ")[0][4:-1] #:-1 to ignore ]
        value = int(i.split(" = ")[1]) #:-1 to ignore newline
        value = bin(value) #get the binary value
        value = value[2:]

        while len(value) <= 35:
            value = '0' + value #extend to 35 bits
        result = ""
        for j in range(len(value)):
            if mask[j] != 'X': # mask has a value, so use this value
                result += mask[j]
            else: #mask == 'X' so take the value from the init program
                result += value[j]
        
        result = int("0b" + result, base = 0) #add 0b to be able to convert back to int, from binary
        changed_vals[index] = result

        i = input.readline()
    
    values = list(changed_vals.values()) #get all values that were changed
    sum = 0
    for value in values: #sum these values
        sum += int(value)
    return sum

if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 14925946402938