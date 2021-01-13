import time

def main():
    input = open("day18_input.txt")
    i = input.readline()    
    result = 0
    substr = ""
    iter = 1
    while i: # get input into a list of lists
        for j in range(len(i)):
            substr = substr + i[j]
    pares = substr.count("(")
    start_index = 0
    end_index = 0
    for i in range(len(pares)): #trying to evaluate each parentheses individually
        for j in range(len(substr)):
            if substr[j] == "(":
                start_index = j
            elif substr[j] == ")":
                end_index = j
                break
        for k in range(start_index, end_index):
            try: 
                eval(substr[:k])
            except SyntaxError:
                pass


    


if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 