import time

def main():
    input = open("day18_input.txt")
    i = input.readline()    
    result = 0
    substr = ""
    while i: # get input into a list of lists
        for j in range(len(i)):
            substr = substr + i[j]
            #print(substr)
            try:
                substr = str(eval(substr))
                #print(eval(substr))
            except SyntaxError:
                pass
        result += int(substr)
        #print(int(substr))
        substr = ""
        i = input.readline()

    return result



if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer 