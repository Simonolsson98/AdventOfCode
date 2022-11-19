
input = open("day2_input.txt")
lines = []
i = input.readline()
while i:
	lines.append(i)
	i = input.readline()

xdir = 0
ydir = 0

for i in range(len(lines)):
	# forward = plus in x-direction
	if(lines[i][0] == "f"):
		xdir += int(lines[i][-2])
	# up = minus in y-direction
	elif(lines[i][0] == "u"):
		ydir -= int(lines[i][-2])
	# down = plus in y-direction
	else:
		ydir += int(lines[i][-2])

print("solution for part 1: " + str(xdir * ydir))

xdir = 0
ydir = 0
aim = 0

for i in range(len(lines)):
	# forward = plus in x-direction and plus with aim * X
	if(lines[i][0] == "f"):
		xdir += int(lines[i][-2])
		ydir += aim * int(lines[i][-2])
	# up = aim decreases
	elif(lines[i][0] == "u"):
		aim -= int(lines[i][-2])
	# down = aim increases
	else:
		aim += int(lines[i][-2])

print("solution for part 2: " + str(xdir * ydir))