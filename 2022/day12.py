input = open("day12_input.txt")
i = input.readline()[:-1]

heightmap = []
while i:
	heightmap.append(list(i))	
	i = input.readline()[:-1]

print(heightmap)

current_height = heightmap[i][j]

def Init():
	for i in range(len(heightmap)):
		for j in range(heightmap[i]):
			neighbours = []
			neighbours.append(heightmap[i + 1][j + 1])
			neighbours.append(heightmap[i - 1][j + 1])
			neighbours.append(heightmap[i + 1][j - 1])
			neighbours.append(heightmap[i - 1][j - 1])

			if(heightmap[i][j] == "S"):
				current_height = heightmap[i][j]

			
def Step(heightmap, current_height, neighbour, count):
	count += 1
	current_height = neighbour
	Step(heightmap, current_height)

	for neighbour in neighbours:
		if(ord(neighbour) - ord(current_height)):
			Step(current_height, neighbours)






# part 1: 
print("day12: solution for part 1: " + str())

# part 2:  
print("day12: solution for part 2: " + str())
