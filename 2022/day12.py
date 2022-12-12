input = open("day12_input.txt")
x = input.readline()[:-1]

heightmap = []
while x:
	heightmap.append(list(x))	
	x = input.readline()[:-1]

current_height = -1

def Init():
	for i in range(len(heightmap)):
		for j in range(len(heightmap[i])):
			if(heightmap[i][j] == "S"):
				current_height = heightmap[i][j]
				return (i, j)

global asdf
asdf = []

path = []
def Step(current_height, i, j, count, visited):
	count += 1
	global asdf
	neighbours = []
	
	if(i + 1 < len(heightmap)):
		if(ord(heightmap[i + 1][j]) == 69 and ord(current_height) == 122):
			asdf.append(count)
			return count
		if(ord(heightmap[i + 1][j]) - ord(current_height) <= 1 and (i + 1, j) not in visited):
			neighbours.append((ord(heightmap[i + 1][j]), i + 1, j))

	if(j + 1 < len(heightmap[i])):
		if(ord(heightmap[i][j + 1]) == 69 and ord(current_height) == 122):
			asdf.append(count)
			return count
		if(ord(heightmap[i][j + 1]) - ord(current_height) <= 1 and (i, j + 1) not in visited):
			neighbours.append((ord(heightmap[i][j + 1]), i, j + 1))
	if(i - 1 >= 0):
		if(ord(heightmap[i - 1][j]) == 69 and ord(current_height) == 122):
			asdf.append(count)
			return count
		if(ord(heightmap[i - 1][j]) - ord(current_height) <= 1 and (i - 1, j) not in visited):
			neighbours.append((ord(heightmap[i - 1][j]), i - 1, j))
	if(j - 1 >= 0):	
		if(ord(heightmap[i][j - 1]) == 69 and ord(current_height) == 122):
			asdf.append(count)
			return count
		if(ord(heightmap[i][j - 1]) - ord(current_height) <= 1 and (i, j - 1) not in visited):
			neighbours.append((ord(heightmap[i][j - 1]), i, j - 1))

	sorted(neighbours)

	temp = visited.copy()
	for asd in neighbours:
		visited.append((asd[1], asd[2]))
		path.append(heightmap[asd[1]][asd[2]])
		Step(heightmap[asd[1]][asd[2]], asd[1], asd[2], count, visited)
		visited = temp


(i, j) = Init()
print(i, j)

current_height = "a"

Step(current_height, i, j, 0, [(i, j)])

print(f"asdf: {min(asdf)}")
#print(path)
# part 1: 
print("day12: solution for part 1: " + str(min(asdf)))

# part 2:  
print("day12: solution for part 2: " + str())
