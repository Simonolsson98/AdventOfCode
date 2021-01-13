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
        for i in range(pares): #trying to evaluate each parentheses individually
            for j in range(len(substr)):
                if substr[j] == "(":
                    start_index = j
                elif substr[j] == ")":
                    end_index = j
                    break
            split_on_plus = substr[start_index+1:end_index].split(" * ")
            print(substr)
            print(split_on_plus)
            result = ""
            for expr in split_on_plus:
                try:
                    result += str(eval(expr))
                except SyntaxError:
                    pass
                result += " * "
            result = result[:-3] #remove the last multiplication operator, ugly but works..
            print(result)
            substr = substr[:start_index-1] + str(eval(result)) + substr[end_index+1:]
            print(substr)
            for k in range(start_index, end_index):
                
                try: 
                    eval(substr[:k])
                except SyntaxError:
                    pass
        print(eval(substr))
        i = input.readline()


    


if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 