import time

def main():
    input = open("day18_input.txt")
    i = input.readline()    
    result = 0
    while i: # get input into a list of lists
        subresult = 0
        for j in range(len(i)):
            index = j
            substr = ""
            left_par = 1
            if i[index] == "(":
                while i[index] != ")" or left_par == 1:
                    if i[index] == "(":
                        left_par += 1
                    substr += i[index]
                    index += 1
                    left_par -= 1
                substr += i[index] #add closing parenthesis too
                opening_inner_par = 0
                closing_inner_par = 0
                iter = 0
                while substr.count("(") > 0:
                    print(f"substr: {substr} for iter: {iter}")
                    if substr[iter] == "(":
                        opening_inner_par = iter
                    if substr[iter] == ")":
                        closing_inner_par = iter
                        print(substr)
                        print(f"open: {opening_inner_par}, closing: {closing_inner_par}")
                        print(str(eval(substr[opening_inner_par:closing_inner_par+1])))
                        substr = substr[:opening_inner_par] + str(eval(substr[opening_inner_par:closing_inner_par+1])) + substr[closing_inner_par+1:]
                        print(substr)
                        iter = 0
                        continue
                    
                    iter += 1
                
                #print(eval(substr))
                print(i)
                i = i[:j] + str(eval(substr[1:])) + i[index+1:]
                print(i)
                return

        
        i = input.readline()
    



if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer 