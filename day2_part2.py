def main():
    f = open("day2_input.txt")
    line = f.readline()
    validPass = 0
    while line:
        splits = line.split(" ")
        index_ranges = splits[0]
        letter = splits[1][0]
        possible_passwords = splits[2]

        pos1 = index_ranges.split("-")[0]
        pos2 = index_ranges.split("-")[1]
		
        first_occurrence  = possible_passwords[int(pos1) - 1]
        second_occurrence = possible_passwords[int(pos2) - 1]
        if first_occurrence == letter and second_occurrence == letter: #both -> not valid
            validPass += 0
        elif first_occurrence == letter or second_occurrence == letter: #exactly one -> valid
            validPass += 1

        line = f.readline()
    return validPass	
	
if __name__ == '__main__':
	returnVal = main()
	print(returnVal)