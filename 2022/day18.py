input = open("day18_input.txt")
i = input.readline()[:-1]

cubes = []
while i:
	cubes.append(list(map(int, i.split(","))))
	i = input.readline()[:-1]

total_exposed_sides = 0
for cube in cubes:
	cube_exposed_sides = 6
	for other_cube in cubes:
		if other_cube == cube:
			continue

		#conditions for cubes being adjacent
		x_adjacent = abs(other_cube[0] - cube[0]) == 1 and other_cube[1] == cube[1] and other_cube[2] == cube[2]
		y_adjacent = abs(other_cube[1] - cube[1]) == 1 and other_cube[0] == cube[0] and other_cube[2] == cube[2]
		z_adjacent = abs(other_cube[2] - cube[2]) == 1 and other_cube[0] == cube[0] and other_cube[1] == cube[1]
		
		if(x_adjacent ^ y_adjacent ^ z_adjacent):
			cube_exposed_sides -= 1

	total_exposed_sides += cube_exposed_sides


# part 1: 
print("day18: solution for part 1: " + str(total_exposed_sides))

# part 2:  
print("day18: solution for part 2: " + str())
