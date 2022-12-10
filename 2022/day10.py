import math

input = open("day10_input.txt")
i = input.readline()[:-1]

register = 1
cycle = 1
strength = 0

def CheckCycle(cycle, strength, register):
	if(cycle == 20 or (cycle + 20) % 40 == 0):
		strength += (cycle * register)
	return strength

while i:
	instr = i.split(" ")
	if(len(instr) == 1):
		cycle += 1
		strength = CheckCycle(cycle, strength, register)
	else:
		cycle += 1
		strength = CheckCycle(cycle, strength, register)
		cycle += 1
		register += int(instr[1])
		strength = CheckCycle(cycle, strength, register)

	i = input.readline()[:-1]

# part 1: 
print("day10: solution for part 1: " + str(strength))

input = open("day10_input.txt")
i = input.readline()[:-1]

register = 1
cycle = 0
strength = 0

height = 6
width = 40
grid = [["........................................"] for _ in range(height) ]

def CheckIfDrawn(register, cycle):
	drawn_row = math.floor((cycle - 1) / width)
	drawn_col = (cycle - 1) % width 

	pixel = drawn_row * width + drawn_col
	pixel_ignoring_height = (pixel - (width * drawn_row))
	
	if(abs(register - pixel_ignoring_height) < 2):
		grid[drawn_row][0] = grid[drawn_row][0][:drawn_col] + "#" + grid[drawn_row][0][drawn_col + 1:]

while i:
	instr = i.split(" ")
	if(len(instr) == 1):
		cycle += 1
		CheckIfDrawn(register, cycle)
	else:
		cycle += 1
		CheckIfDrawn(register, cycle)
		cycle += 1
		CheckIfDrawn(register, cycle)
		register += int(instr[1])

	i = input.readline()[:-1]

# part 2:  
print("day10: solution for part 2: ")
for row in grid:
	print(row)