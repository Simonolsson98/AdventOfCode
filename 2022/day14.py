input = open("day14_input.txt")
i = input.readline()[:-1]

scan = [["." * 600] for i in range(200)]
second_scan = [["." * 1500] for i in range(1500)]
sand_bottom = 0

# parsing
while i:
	pairs = i.split(" -> ")
	old_pair = pairs[0].split(",")
	pairs = pairs[1:]

	for pair in pairs:
		coord = pair.split(",")
		smallest_y = min(int(coord[1]), int(old_pair[1]))
		largest_y = max(int(coord[1]), int(old_pair[1]))
		if(largest_y > sand_bottom):
			sand_bottom = largest_y

		if(smallest_y != largest_y):
			for j in range(smallest_y, largest_y + 1):
				scan[j][0] = scan[j][0][:int(coord[0])] + "#" + scan[j][0][int(coord[0]) + 1:]
				second_scan[j][0] = second_scan[j][0][:int(coord[0])] + "#" + second_scan[j][0][int(coord[0]) + 1:]

		smallest_x = min(int(coord[0]), int(old_pair[0]))
		largest_x = max(int(coord[0]), int(old_pair[0]))
		if(smallest_x != largest_x):
			for j in range(smallest_x, largest_x + 1):
				scan[int(coord[1])][0] = scan[int(coord[1])][0][:j] + "#" + scan[int(coord[1])][0][j + 1:]
				second_scan[int(coord[1])][0] = second_scan[int(coord[1])][0][:j] + "#" + second_scan[int(coord[1])][0][j + 1:]
		
		old_pair = coord

	i = input.readline()[:-1]

sand_count = 0
i = 0
j = 500
while(True):
	# check for endless falling
	if(i >= sand_bottom):
		break

	# try to move down
	if(scan[i + 1][0][j] == "."):
		i += 1
		continue
	# try to move down + left
	elif(scan[i + 1][0][j - 1] == "."):
		j -= 1
		i += 1
		continue
	# try to move down + right
	elif(scan[i + 1][0][j + 1] == "."):
		j += 1
		i += 1
		continue
	# otherwise we have to stop
	else:
		sand_count += 1
		scan[i][0] = scan[i][0][:j] + "#" + scan[i][0][j + 1:]
		(i, j) = (0, 500)

# visualizing
#[print(row[0][477:550]) for row in scan[0:175]]

# part 1: 
print("day14: solution for part 1: " + str(sand_count))

sand_count = 0
i = 0
j = 500
while(True):
	# check for stop condition
	if(second_scan[0][0][500] == "#"):
		break
	# check for collision with floor
	if(i >= sand_bottom + 2):
		second_scan[i][0] = second_scan[i][0][:j] + "#" + second_scan[i][0][j + 1:]
		(i, j) = (0, 500)
	# try to move down
	if(second_scan[i + 1][0][j] == "."):
		i += 1
		continue
	# try to move down + left
	elif(second_scan[i + 1][0][j - 1] == "."):
		j -= 1
		i += 1
		continue
	# try to move down + right
	elif(second_scan[i + 1][0][j + 1] == "."):
		j += 1
		i += 1
		continue
	# otherwise we have to stop
	else:
		sand_count += 1
		second_scan[i][0] = second_scan[i][0][:j] + "#" + second_scan[i][0][j + 1:]
		(i, j) = (0, 500)

# visualizing
#[print(row[0][350:750]) for row in second_scan[0:179]]

# part 2:  
print("day14: solution for part 2: " + str(sand_count))