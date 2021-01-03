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
            print(mask)
            continue
        
        index = int(i.split(" = ")[0][4:-1]) #:-1 to ignore ]
        #value = int(i.split(" = ")[1]) #:-1 to ignore newline
        print(index)
        value = bin(index) #get the binary value
        print(value)
        value = value[2:]

        while len(value) <= 35:
            value = '0' + value #extend to 35 bits
        result = ""

        for j in range(len(value)):
            #print(mask[j])
            if mask[j] == '0': # mask == 0 means overwrite bit to 0
                result += value[j]
            elif mask[j] == '1' or mask[j] == 'X': #mask == 'X' or 1, so keep this bit as this value
                result += mask[j]

        index_pos_list = []
        index_pos = 0
        while True: 
            try: #find all occurrences of 'X', more specifically its indices
                index_pos = result.index('X', index_pos)
                index_pos_list.append(index_pos)
                index_pos += 1
            except ValueError as e:
                break
        
        result = result.replace('X', '0')
        temp_result = result

        print(f"len of X's: {len(index_pos_list)}")
        for i in range(2 ** len(index_pos_list)):
            bin_index = bin(i)
            bin_index = bin_index[2:]

            while len(bin_index) < len(index_pos_list):
                bin_index = '0' + bin_index #extend to proper amount of bits

            for j in range(len(bin_index)):
                result = result[:index_pos_list[j]] + bin_index[j] + result[index_pos_list[j] + 1:]    
            
            print(f"result after:  {result}")
            result = int("0b" + result, base = 0) #add 0b to be able to convert back to int, from binary
            changed_vals[index] = result

            result = temp_result #prepare for next permutation of X's to be changed

        i = input.readline()
    
    values = list(changed_vals.values()) #get all values that were changed
    print(values)
    sum = 0
    for value in values: #sum these values
        sum += int(value)
    return sum

if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 