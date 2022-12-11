import math


def Round(i, round_num, starting_items):
	while i:
		monkey = int(i.split(" ")[1][:-1])
		
		if(round_num == 0):
			starting_items[monkey] = input.readline()[:-1].split(": ")[1].split(", ") + starting_items[monkey]
		else:
			input.readline()[:-1]
		
		starting_ints = [eval(num) for num in starting_items[monkey]]

		inspect_count[monkey] += len(starting_ints)

		operation = input.readline()[:-1].split(": ")[1]
		op = operation.split("old ")[1]
		operator = op[0]
		term = op[2:]

		new_ints = []
		match operator:
			case "+":
				for item in starting_ints:
					if(term == "old"):
						item += item
					else:
						item += int(term)
					new_ints.append(math.floor(item / 3))
			case "*":
				for item in starting_ints:
					if(term == "old"):
						item *= item
					else:
						item *= int(term)
					new_ints.append(math.floor(item / 3))

		test = int(input.readline()[:-1].split(" ")[-1])
		true_test = int(input.readline()[:-1].split(": ")[1][-1])
		false_test = int(input.readline()[:-1].split(": ")[1][-1])

		for item in new_ints:
			if(item % test == 0):
				starting_items[true_test].append(str(item))
			else:
				starting_items[false_test].append(str(item))

			starting_items[monkey] = []

		#empty line
		input.readline()[:-1]

		i = input.readline()[:-1]
	return starting_items


inspect_count = [0, 0, 0, 0, 0, 0, 0, 0]
starting_items = [[], [], [], [], [], [], [], []]

input = open("day11_input.txt")

for round_num in range(20):
	input = open("day11_input.txt")
	i = input.readline()[:-1]
	starting_items = Round(i, round_num, starting_items)

max_two = sorted(inspect_count, reverse=True)[0:2]
# part 1: 
print("day11: solution for part 1: " + str(max_two[0] * max_two[1]))

# part 2:  
print("day11: solution for part 2: " + str())
