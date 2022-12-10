input = open("day10_input.txt")
i = input.readline()[:-1]

register = 1
cycle = 1
strength = 0

while i:
	instr = i.split(" ")
	if(len(instr) == 1):
		cycle += 1
		if(cycle == 20 or (cycle + 20) % 40 == 0):
			strength += (cycle * register)
	else:
		cycle += 1
		if(cycle == 20 or (cycle + 20) % 40 == 0):
			strength += (cycle * register)
		cycle += 1
		register += int(instr[1])
		if(cycle == 20 or (cycle + 20) % 40 == 0):
			strength += (cycle * register)

	i = input.readline()[:-1]


# part 1: 
print("day10: solution for part 1: " + str(strength))

# part 2:  
print("day10: solution for part 2: " + str())