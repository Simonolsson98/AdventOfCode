import math
def main():
    sum_of_questions = 0
    set_of_values = set()
    input = open("day6_input.txt")
    string_to_use = ""
    lines = []
    i = input.readline()
    while i: #get input into a list of strings
        lines.append(i)
        i = input.readline()
    for s in lines:
        string_to_use += s
    split_string = string_to_use.split("\n\n")
    
    for each_string in split_string:
        each_string = each_string.replace("\n", "") #put all strings from the same group in one long string
        for c in each_string:
            set_of_values.add(c) #add each (unique) character to a set
        
        sum_of_questions += len(set_of_values) #length of the set = amount of unique yes answers
        set_of_values.clear()

    return sum_of_questions

if __name__ == '__main__':
	returnVal = main()
	print(returnVal) #answer = 6273