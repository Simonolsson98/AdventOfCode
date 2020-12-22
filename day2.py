def main():
	f = open("day2_input.txt")
	line = f.readline()
	validPass = 0
	while line:
		splits = line.split(" ")
		amount = splits[0]
		letter = splits[1][0]
		password = splits[2]

		min = amount.split("-")[0]
		max = amount.split("-")[1]
		
		occurrences = 0
		for i in range(len(password)):
			if password[i] == letter:
				occurrences += 1
		if(occurrences >= int(min) and occurrences <= int(max)):
			validPass += 1
			
		line = f.readline()
	return validPass	
	
if __name__ == '__main__':
	returnVal = main()
	print(returnVal)