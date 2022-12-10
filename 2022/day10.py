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

# part 2:  
print("day10: solution for part 2: " + str())