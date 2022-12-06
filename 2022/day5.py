input = open("day5_input.txt")

i = input.readline()
if(i[:-1] == "\n"):
	i = i[:-1]

stack11 = ['W', 'B', 'D', 'N', 'C', 'F', 'J']
stack12 = ['P', 'Z', 'V', 'Q', 'L', 'S', 'T']
stack13 = ['P', 'Z', 'B', 'G', 'J', 'T']
stack14 = ['D', 'T', 'L', 'J', 'Z', 'B', 'H', 'C']
stack15 = ['G', 'V', 'B', 'J', 'S']
stack16 = ['P', 'S', 'Q']
stack17 = ['B', 'V', 'D', 'F', 'L', 'M', 'P', 'N']
stack18 = ['P', 'S', 'M', 'F', 'B', 'D', 'L', 'R']
stack19 = ['V', 'D', 'T', 'R']

stack21 = ['W', 'B', 'D', 'N', 'C', 'F', 'J']
stack22 = ['P', 'Z', 'V', 'Q', 'L', 'S', 'T']
stack23 = ['P', 'Z', 'B', 'G', 'J', 'T']
stack24 = ['D', 'T', 'L', 'J', 'Z', 'B', 'H', 'C']
stack25 = ['G', 'V', 'B', 'J', 'S']
stack26 = ['P', 'S', 'Q']
stack27 = ['B', 'V', 'D', 'F', 'L', 'M', 'P', 'N']
stack28 = ['P', 'S', 'M', 'F', 'B', 'D', 'L', 'R']
stack29 = ['V', 'D', 'T', 'R']

part1_stacks = [stack11, stack12, stack13, stack14, stack15, stack16, stack17, stack18, stack19]
part2_stacks = [stack21, stack22, stack23, stack24, stack25, stack26, stack27, stack28, stack29]

while i:
	substring = i.split(" ")

	move_box = substring[1]
	from_stack = substring[3]
	to_stack = substring[5]

	popped_list = []
	for i in range(int(move_box)):
		popped = part1_stacks[int(from_stack) - 1].pop()
		part1_stacks[int(to_stack) - 1].append(popped)

		popped = part2_stacks[int(from_stack) - 1].pop()
		popped_list.append(popped)

	popped_list.reverse()
	part2_stacks[int(to_stack) - 1] += popped_list

	
	i = input.readline()
	if(i[:-1] == "\n"):
		i = i[:-1]

message = ''
for stack in part1_stacks:
	message += stack[len(stack) - 1]

# part 1: 
print("day5: solution for part 1: " + str(message))

message = ''
for stack in part2_stacks:
	message += stack[len(stack) - 1]

# part 2:  
print("day5: solution for part 2: " + str(message))