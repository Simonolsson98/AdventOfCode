import time

def main():
    input = open("day14_input.txt")
    i = input.readline()
    changed_vals = {}
    mask = ""
    while i:
        if i[0:4] == "mask":
            mask = mask[7:]
            i = input.readline()
            continue
        index = i.split(" = ")[0][4:-1] #:-1 to ignore ]
        value = i.split(" = ")[1][:-1] #:-1 to ignore newline
        print(index)
        print(value)
        result = 0
        for j in range(len(value)):
            if mask[j] != 'X':
                result.append(mask[j])
            else: #mask == 'X'
                result.append(value[j])


        i = input.readline()

if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 836024966345345