input_str = open("day06_input.txt").read()

def FindSolution(marker_length):
	recent = []
	for i in range(marker_length):
		recent.append(input_str[i])
	
	for count, char in enumerate(input_str[(marker_length - 1):]):
		for x in range(marker_length - 1):
			recent[x] = recent[x + 1]

		recent[marker_length - 1] = char

		if(len(set(recent)) == len(recent)):
			return count + marker_length

# part 1: 
print("day6: solution for part 1: " + str(FindSolution(4)))

# part 2:  
print("day6: solution for part 2: " + str(FindSolution(14)))