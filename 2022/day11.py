import math

moduloOfAllDivisors = 3 * 5 * 2 * 13 * 11 * 17 * 19 * 7

def Round(i, part, round_num, starting_items):
	while i:
		monkey = int(i.split(" ")[1][:-1])
		
		if(round_num == 0):
			starting_items[monkey] = input.readline()[:-1].split(": ")[1].split(", ") + starting_items[monkey]
		else:
			input.readline()[:-1]
		
		starting_ints = [eval(num) for num in starting_items[monkey]]
		inspect_count[monkey] += len(starting_ints)
		
		op = input.readline()[:-1].split(": ")[1].split("old ")[1]

		operator = op[0]
		term = op[2:]

		new_ints = []
		if(operator == "+"):
			for item in starting_ints:
				if(term == "old"):
					item += item
				else:
					item += int(term)

				if(part == 1):
					item = item // 3
				else:
					item = item % moduloOfAllDivisors

				new_ints.append(item)
		else:
			for item in starting_ints:
				if(term == "old"):
					item *= item
				else:
					item *= int(term)

				if(part == 1):
					item = item // 3
				else:
					item = item % moduloOfAllDivisors

				new_ints.append(item)

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
rounds = 20
for round_num in range(rounds):
	input = open("day11_input.txt")
	i = input.readline()[:-1]
	starting_items = Round(i, 1, round_num, starting_items)

max_two = sorted(inspect_count, reverse=True)[0:2]
# part 1: 
print("day11: solution for part 1: " + str(max_two[0] * max_two[1]))

inspect_count = [0, 0, 0, 0, 0, 0, 0, 0]
starting_items = [[], [], [], [], [], [], [], []]
rounds = 10000
for round_num in range(rounds):
	input = open("day11_input.txt")
	i = input.readline()[:-1]
	starting_items = Round(i, 2, round_num, starting_items)

max_two = sorted(inspect_count, reverse=True)[0:2]
# part 2:  
print("day11: solution for part 2: " + str(max_two[0] * max_two[1]))
