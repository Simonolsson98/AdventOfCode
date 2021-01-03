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
        
        index = int(i.split(" = ")[0][4:-1]) #:-1 to ignore ]
        address = int(i.split(" = ")[1]) #:-1 to ignore newline, value to be written to the addresses that we calculate later
        bin_value = bin(index) #get the binary value
        bin_value = bin_value[2:]

        while len(bin_value) <= 35:
            bin_value = '0' + bin_value #extend to 35 bits
        result = ""

        for j in range(len(bin_value)):
            if mask[j] == '0': # mask == 0 means overwrite bit to 0
                result += bin_value[j]
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
        temp_result = result #to use later to reset the binary value for the next permutation of X's

        for i in range(2 ** len(index_pos_list)):
            bin_index = bin(i)
            bin_index = bin_index[2:]

            while len(bin_index) < len(index_pos_list):
                bin_index = '0' + bin_index #extend to proper amount of bits
            
            for j in range(len(bin_index)):
                result = result[:index_pos_list[j]] + bin_index[j] + result[index_pos_list[j] + 1:]    
            
            result = int("0b" + result, base = 0) #add 0b to be able to convert back to int, from binary
            changed_vals[result] = address #write the proper value to the addresses
            result = temp_result #prepare for next permutation of X's to be changed

        i = input.readline()
    
    values = sum(list(changed_vals.values())) #get all values that were changed and sum these
    
    return values

if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 3706820676200