def init():
	input = open("day4_input.txt")
	lines = []
	i = input.readline()

	bingonums = i.split(",")
	# remove newline
	bingonums[-1] = bingonums[-1][:2]

	input.readline()
	i = input.readline()

	while(i):
		subrows = []
		for _ in range(5):
			num = i[:-1].split(" ")
			while(num.count("") > 0):
				num.remove("")
			subrows.append(num)
			i = input.readline()
		lines.append(subrows)
		i = input.readline()

	while(lines.count([]) > 0):
		lines.remove([])

	columns = []
	for i in range(0, len(lines)):
		subcols = []
		for j in range(5):
			subcols.append([lines[i][k][j] for k in range(5)])
		for l in range(5):
			lines[i].append(subcols[l])
	return lines, bingonums

def find_winning_board():
	drawn_numbers = []
	for i in range(len(bingonums)):
		drawn_numbers.append(bingonums[i])
		for j in range(len(lines)):
			for k in range(len(lines[j])):
				if(all(x in drawn_numbers for x in lines[j][k])):
					return lines[j], drawn_numbers

def find_unmarked_nums(input_list, drawn_numbers):
	for i in range(len(input_list)):
		for j in range(len(drawn_numbers)):
			if(input_list[i].count(drawn_numbers[j]) > 0):
				input_list[i].remove(drawn_numbers[j])
	for i in range(len(input_list)):
		for j in range(len(input_list[i])):
			unmarked_nums.add(int(input_list[i][j]))

def find_last_winning_boards():
	fixed_list = lines[:]
	drawn_numbers = []
	for i in range(len(bingonums)):
		drawn_numbers.append(bingonums[i])
		for j in range(len(lines)):
			for k in range(len(lines[j])):
				if(all(x in drawn_numbers for x in lines[j][k])):
					if(fixed_list.count(lines[j]) > 0):
						global last_board
						fixed_list.remove(lines[j])
						last_board = lines[j]
						last_board.remove(lines[j][k])
						break
		if(len(fixed_list) == 0):
			return last_board, drawn_numbers
					

lines, bingonums = init()

# part 1:
# find the winning board
winning_board, drawn_numbers = find_winning_board()

unmarked_nums = set()
# prepare to sum unmarked numbers
find_unmarked_nums(winning_board, drawn_numbers)

# unmarked nums * last drawn number
print("solution of part 1 is: " + str(sum(unmarked_nums) * int(drawn_numbers[-1])))

# part 2:
# find the board that wins last
last_board, drawn_numbers = find_last_winning_boards()

# find the unmarked numbers on this board
unmarked_nums = set()
find_unmarked_nums(last_board, drawn_numbers)

# unmarked nums * last drawn number
print("solution of part 2 is: " + str(sum(unmarked_nums) * int(drawn_numbers[-1])))