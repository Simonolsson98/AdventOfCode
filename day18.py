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
            print(substr)
            pares = ""
            while substr[0] == "(" and len(substr) != substr.count("("):
                pares += substr[0]
                substr = substr[1:]
            try:
                substr = str(eval(substr))
                substr = pares + substr
                print(substr)
            except SyntaxError:
                substr = pares + substr

        result += int(substr)
        print(f"row: {iter} for {int(substr)}")
        substr = ""
        i = input.readline()
        iter += 1

    return result



if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer 