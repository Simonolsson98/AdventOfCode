input = open("day18_input.txt")
i = input.readline()[:-1]

cubes = []
while i:
	cubes.append(list(map(int, i.split(","))))
	i = input.readline()[:-1]

largest_x = 0
largest_y = 0
largest_z = 0
def part1():
	total_exposed_sides = 0
	global largest_x, largest_y, largest_z
	for cube in cubes:
		if(cube[0] > largest_x):
			largest_x = cube[0]
		if(cube[1] > largest_y):
			largest_y = cube[1]
		if(cube[2] > largest_z):
			largest_z = cube[2]

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
	return total_exposed_sides

total_exposed_sides = part1()
# part 1: 
print("day18: solution for part 1: " + str(total_exposed_sides))

visited = set()
for x in range(-2, largest_x + 2):
	for y in range(-2, largest_y + 2):
		for z in range(-2, largest_z + 2):
			coords = [x, y, z]
			if(coords in cubes):
				visited.add(tuple(coords))
				break
for x in range(-2, largest_x + 2):
	for z in range(-2, largest_z + 2):
		for y in range(-2, largest_y + 2):
			coords = [x, y, z]
			if(coords in cubes):
				visited.add(tuple(coords))
				break

for y in range(-2, largest_y + 2):
	for x in range(-2, largest_x + 2):
		for z in range(-2, largest_z + 2):
			coords = [x, y, z]
			if(coords in cubes):
				visited.add(tuple(coords))
				break
for y in range(-2, largest_y + 2):
	for z in range(-2, largest_z + 2):
		for x in range(-2, largest_x + 2):
			coords = [x, y, z]
			if(coords in cubes):
				visited.add(tuple(coords))
				break

for z in range(-2, largest_z + 2):
	for x in range(-2, largest_x + 2):
		for y in range(-2, largest_y + 2):
			coords = [x, y, z]
			if(coords in cubes):
				visited.add(tuple(coords))
				break

for z in range(-2, largest_z + 2):
	for y in range(-2, largest_y + 2):
		for x in range(-2, largest_x + 2):
			coords = [x, y, z]
			if(coords in cubes):
				visited.add(tuple(coords))
				break

print(visited)
exp = 0
for cube in cubes:
	first  = ((cube[0] + 1, cube[1], cube[2]) in visited)
	second = ((cube[0] - 1, cube[1], cube[2]) in visited)
	third  = ((cube[0], cube[1] + 1, cube[2]) in visited)
	fourth = ((cube[0], cube[1] - 1, cube[2]) in visited)
	fifth  = ((cube[0], cube[1], cube[2] + 1) in visited)
	sixth  = ((cube[0], cube[1], cube[2] - 1) in visited)
	
	asd = [first, second, third, fourth, fifth, sixth]
	print(asd)
	for elem in asd:
		if elem == True:
			exp += 1 

#2540
# part 2:  
print("day18: solution for part 2: " + str(exp))
