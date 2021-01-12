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

            parentheses = ""
            while substr[0] == "(" and len(substr) != substr.count("("):
                parentheses += substr[0]
                substr = substr[1:]
            if substr.count(")") >= 1: #if unmatching parentheses'
                substr = parentheses + substr
                try:
                    index = 0
                    for k in range(len(substr)):
                        if substr[k] == "(": #get the inner parentheses index
                            index = k
                    substr = substr[:index] + str(eval(substr[index:])) #try to parse the expression inside the opening parentheses
                except SyntaxError:
                    substr = parentheses + substr
            else:
                try:
                    substr = str(eval(substr))
                    substr = parentheses + substr
                except SyntaxError:
                    substr = parentheses + substr
                    index = 0
                    for k in range(len(substr)):
                        if substr[k] == "(":
                            index = k
                    try:                   
                        substr = substr[:index+1] + str(eval(substr[index+1:]))
                    except SyntaxError:
                        pass

        result += int(eval(substr)) #add result from the row

        substr = "" #reset substring for next equation
        i = input.readline()
        iter += 1

    return result


if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 209335026987