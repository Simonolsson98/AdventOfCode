import math

input = open("day11_input.txt")
i = input.readline()[:-1]

inspect_count = [0, 0, 0, 0, 0, 0, 0, 0]
starting_items = [[], [], [], [], [], [], [], []]
print(inspect_count)
print(starting_items)


while i:
	monkey = int(i.split(" ")[1][:-1])
	print(f"MONKEY NUMBER : {monkey}")
	
	print(f"initial items for monkey: {monkey}:  {starting_items[monkey]}")
	starting_items[monkey] = input.readline()[:-1].split(": ")[1].split(", ") + starting_items[monkey]
	print(starting_items[monkey])
	
	starting_ints = [eval(num) for num in starting_items[monkey]]
	print(f"starting ints: {starting_ints}")

	inspect_count[monkey] += len(starting_ints)

	operation = input.readline()[:-1].split(": ")[1]
	print(op := operation.split("old ")[1])
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

	print(f"new_ints: {new_ints}")

	test = int(input.readline()[:-1].split(": ")[1][-1])
	print(f"divisible by: {test}")

	true_test = int(input.readline()[:-1].split(": ")[1][-1])
	false_test = int(input.readline()[:-1].split(": ")[1][-1])

	for item in new_ints:
		if(item % test == 0):
			print(f"throw to monkey: {true_test} and add {item} to its list")
			starting_items[true_test].append(str(item))
		else:
			print(f"throw to monkey: {false_test} and add {item} to its list")
			starting_items[false_test].append(str(item))

		starting_items[monkey] = []

	#empty line
	input.readline()[:-1]

	i = input.readline()[:-1]
	#monkey i
	print(i)

max_two = sorted(inspect_count, reverse=True)[0:2]
# part 1: 
print("day11: solution for part 1: " + str(max_two[0] * max_two[1]))

# part 2:  
print("day11: solution for part 2: " + str())
