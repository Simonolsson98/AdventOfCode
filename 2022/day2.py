input = open("day2_input.txt")
i = input.readline()
part1_total = 0
part2_total = 0

def defineWinOrLoss(opponent, myself):
	if(opponent == 'A'):
		if (myself == 'X'):
			return 4
		elif(myself == 'Y'):
			return 8
		else:
			return 3
	elif (opponent == 'B'):
		if (myself == 'X'):
			return 1
		elif(myself == 'Y'):
			return 5
		else:
			return 9
	else:
		if (myself == 'X'):
			return 7
		elif(myself == 'Y'):
			return 2
		else:
			return 6

def decideWinOrLoss(opponent, myself):
	if(opponent == 'A'):
		if (myself == 'X'):
			return 3
		elif(myself == 'Y'):
			return 4
		else:
			return 8
	elif (opponent == 'B'):
		if (myself == 'X'):
			return 1
		elif(myself == 'Y'):
			return 5
		else:
			return 9
	else:
		if (myself == 'X'):
			return 2
		elif(myself == 'Y'):
			return 6
		else:
			return 7

while i:
	part1_total += defineWinOrLoss(i[0], i[2])
	part2_total += decideWinOrLoss(i[0], i[2])
	i = input.readline()

# part 1: 
print("solution for part 1: " + str(part1_total))

# part 2:  
print("solution for part 2: " + str(part2_total))