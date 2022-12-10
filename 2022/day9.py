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

def MoveTail(direc, j, head_y, head_x, tail_y, tail_x):
	(head_y, head_x, tail_y, tail_x) = DetermineTailMovement(head_y, head_x, tail_y, tail_x)		
	if(j == 8 or j == "part1"):
		visited_locations.append((tail_y, tail_x))
	return (head_y, head_x, tail_y, tail_x)

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

def Solve(i, k):
	while i:
		instruction = i.split(" ")
		direction = instruction[0]
		amount = instruction[1]
		for _ in range(int(amount)):
			(knots_y[0], knots_x[0]) = MoveHead(direction, knots_y[0], knots_x[0])
			for j in range(k):
				if(k == 1):
					(knots_y[0], knots_x[0], knots_y[1], knots_x[1]) = MoveTail(direction, "part1", knots_y[0], knots_x[0], knots_y[1], knots_x[1])
				else:
					(knots_y[j], knots_x[j], knots_y[j + 1], knots_x[j + 1]) = MoveTail(direction, j, knots_y[j], knots_x[j], knots_y[j + 1], knots_x[j + 1])
		i = input_part.readline()[:-1]

input_part = open("day9_input.txt")
i = input_part.readline()[:-1]
knots_x, knots_y = [0] * 10, [0] * 10

visited_locations = []
Solve(i, number_of_knots:=1)

# part 1: 
print("day9: solution for part 1: " + str(len(set(visited_locations))))

input_part = open("day9_input.txt")
i = input_part.readline()[:-1]
knots_x, knots_y = [0] * 10, [0] * 10

visited_locations = []
Solve(i, number_of_knots:=9)

# part 2:  
print("day9: solution for part 2: " + str(len(set(visited_locations))))