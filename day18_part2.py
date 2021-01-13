import time

def main():
    input = open("day18_input.txt")
    i = input.readline()    
    result = 0
    substr = ""

    while i: # get input into a list of lists
        for j in range(len(i)):
            substr = substr + i[j]
        if substr[-1] == '\n':
            substr = substr[:-1]
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
            sub_eval = ""
            for expr in split_on_plus:
                try:
                    sub_eval += str(eval(expr))
                except SyntaxError:
                    pass
                sub_eval += " * "
            sub_eval = sub_eval[:-3] #remove the last multiplication operator, ugly but works..
            substr = substr[:start_index] + str(eval(sub_eval)) + substr[end_index+1:]
        #we reach a state where we dont have any parentheses left (hopefully), so just split on * again and eval
        #print(f"PLS: {substr}")

        split_on_plus = substr.split(" * ")
        sub_eval = 1
        for expr in split_on_plus:
            try:
                sub_eval *= eval(expr)
            except SyntaxError:
                pass
        result += sub_eval
        split_on_plus = []
        i = input.readline()

    return result

    


if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 