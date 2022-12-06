input_str = open("day6_input.txt").read()
recent_part1 = [None, input_str[0], input_str[1], input_str[2]]
recent_part2 = [None, input_str[0], input_str[1], input_str[2], input_str[3], input_str[4], input_str[5], input_str[6], input_str[7], input_str[8], input_str[9], input_str[10], input_str[11], input_str[12]]
result = 0

def FindSolution(i, recent):
	for count, char in enumerate(input_str[(i-1):]):
		for x in range(i-1):
			recent[x] = recent[x + 1]

		recent[i-1] = char

		if(len(set(recent)) == len(recent)):
			return count + i

# part 1: 
print("day6: solution for part 1: " + str(FindSolution(4, recent_part1)))

# part 2:  
print("day6: solution for part 2: " + str(FindSolution(14, recent_part2)))