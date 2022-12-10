input = open("day9_input.txt")
i = input.readline()[:-1]

grid = [ ["................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................"] for i in range(800)]

def DetermineTailMovement(head_y, head_x, tail_y, tail_x):
	y_gap = head_y - tail_y
	if(y_gap < -1):
		tail_y -= 1
		if(head_x < tail_x):
			tail_x -= 1
		elif(head_x > tail_x):
			tail_x += 1
	elif(y_gap > 1):
		tail_y += 1
		if(head_x < tail_x):
			tail_x -= 1
		elif(head_x > tail_x):
			tail_x += 1
	
	x_gap = head_x - tail_x
	if(x_gap < -1):
		tail_x -= 1
		if(head_y < tail_y):
			tail_y -= 1
		elif(head_y > tail_y):
			tail_y += 1
	elif(x_gap > 1):
		tail_x += 1
		if(head_y < tail_y):
			tail_y -= 1
		elif(head_y > tail_y):
			tail_y += 1
	return (head_y, head_x, tail_y, tail_x)

def CheckIfSkip(head_y, head_x, tail_y, tail_x):
	if(abs(head_y - tail_y) <= 1 and abs(head_x - tail_x) <= 1):
		return True
	return False

def OneStep(direc, j, head_y, head_x, tail_y, tail_x):
	match direc:
		case "U":
			head_y -= 1
			if(CheckIfSkip(head_y, head_x, tail_y, tail_x)):
				return (head_y, head_x, tail_y, tail_x)

			(head_y, head_x, tail_y, tail_x) = DetermineTailMovement(head_y, head_x, tail_y, tail_x)

			grid[tail_y][0] = grid[tail_y][0][:tail_x] + "#" + grid[tail_y][0][tail_x + 1:]

		case "D":
			head_y += 1
			if(CheckIfSkip(head_y, head_x, tail_y, tail_x)):
				return (head_y, head_x, tail_y, tail_x)
			
			(head_y, head_x, tail_y, tail_x) = DetermineTailMovement(head_y, head_x, tail_y, tail_x)

			grid[tail_y][0] = grid[tail_y][0][:tail_x] + "#" + grid[tail_y][0][tail_x + 1:]

		case "L":
			head_x -= 1
			if(CheckIfSkip(head_y, head_x, tail_y, tail_x)):
				return (head_y, head_x, tail_y, tail_x)

			(head_y, head_x, tail_y, tail_x) = DetermineTailMovement(head_y, head_x, tail_y, tail_x)

			grid[tail_y][0] = grid[tail_y][0][:tail_x] + "#" + grid[tail_y][0][tail_x + 1:]

		case "R":
			head_x += 1
			if(CheckIfSkip(head_y, head_x, tail_y, tail_x)):
				return (head_y, head_x, tail_y, tail_x)

			(head_y, head_x, tail_y, tail_x) = DetermineTailMovement(head_y, head_x, tail_y, tail_x)

			grid[tail_y][0] = grid[tail_y][0][:tail_x] + "#" + grid[tail_y][0][tail_x + 1:]

	return (head_y, head_x, tail_y, tail_x)

head_x = 500
head_y = 500
tail_x = 500
tail_y = 500

while i:
	instruction = i.split(" ")
	direction = instruction[0]
	amount = instruction[1]
	
	for _ in range(int(amount)):
		(hy, hx, ty, tx) = OneStep(direction, -1, head_y, head_x, tail_y, tail_x)
		(head_y, head_x, tail_y, tail_x) = (hy, hx, ty, tx)
	
	i = input.readline()[:-1]

result = sum([row[0].count('#') for row in grid])

# part 1: 
print("day9: solution for part 1: " + str(result))

#--------------------------------------------------------------------------------------------------------------

input = open("day9_input.txt")
i = input.readline()[:-1]

grid = [ [".........................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................."] for i in range(2000)]

def SecondStep(direc, j, head_y, head_x, tail_y, tail_x):
	match direc:
		case "U":
			if(CheckIfSkip(head_y, head_x, tail_y, tail_x)):
				return (head_y, head_x, tail_y, tail_x)
			(head_y, head_x, tail_y, tail_x) = DetermineTailMovement(head_y, head_x, tail_y, tail_x)		
			if(j == 8):
				grid[tail_y][0] = grid[tail_y][0][:tail_x] + "#" + grid[tail_y][0][tail_x + 1:]

		case "D":
			if(CheckIfSkip(head_y, head_x, tail_y, tail_x)):
				return (head_y, head_x, tail_y, tail_x)

			(head_y, head_x, tail_y, tail_x) = DetermineTailMovement(head_y, head_x, tail_y, tail_x)
			if(j == 8):
				grid[tail_y][0] = grid[tail_y][0][:tail_x] + "#" + grid[tail_y][0][tail_x + 1:]

		case "L":
			if(CheckIfSkip(head_y, head_x, tail_y, tail_x)):
				return (head_y, head_x, tail_y, tail_x)

			(head_y, head_x, tail_y, tail_x) = DetermineTailMovement(head_y, head_x, tail_y, tail_x)
			if(j == 8):
				grid[tail_y][0] = grid[tail_y][0][:tail_x] + "#" + grid[tail_y][0][tail_x + 1:]

		case "R":
			if(CheckIfSkip(head_y, head_x, tail_y, tail_x)):
				return (head_y, head_x, tail_y, tail_x)
			
			(head_y, head_x, tail_y, tail_x) = DetermineTailMovement(head_y, head_x, tail_y, tail_x)
			if(j == 8):
				grid[tail_y][0] = grid[tail_y][0][:tail_x] + "#" + grid[tail_y][0][tail_x + 1:]

	return (head_y, head_x, tail_y, tail_x)

def MoveHead(direc, head_y, head_x):
	match direc:
		case "U":
			head_y -= 1
		case "D":
			head_y += 1
		case "L":
			head_x -= 1
		case "R":
			head_x += 1
	return (head_y, head_x)

knots_x = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500]
knots_y = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500]

while i:
	instruction = i.split(" ")
	direction = instruction[0]
	amount = instruction[1]
	for _ in range(int(amount)):
		(knots_y[0], knots_x[0]) = MoveHead(direction, knots_y[0], knots_x[0])
		for j in range(9):
			(knots_y[j], knots_x[j], knots_y[j + 1], knots_x[j + 1]) = SecondStep(direction, j, knots_y[j], knots_x[j], knots_y[j + 1], knots_x[j + 1])
	
	i = input.readline()[:-1]

result2 = sum([row[0].count('#') for row in grid])

# part 2:  
print("day9: solution for part 2: " + str(result2))