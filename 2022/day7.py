input = open("day7_input.txt")
i = input.readline()[:-1]

newDict = {"/": 0}
prevDirs = []
currentDir = ""

while i:
	if(i[:4] == "$ cd"):
		if(currentDir != "" and i[5:] != ".."):
			prevDirs.append(currentDir)

		currentDir += i[5:]
		if(i[5:] == ".."):
			currentDir = prevDirs.pop()

		i = input.readline()[:-1]
	elif(i[:4] == "$ ls"):
		i = input.readline()[:-1]
		while(i != "" and i[0] != "$"):
			first = i.split(" ")
			if(first[0] == "dir"):
				newDict.update({(currentDir + first[1]): 0})
			else:
				newDict[currentDir] += int(first[0])
				for prevDir in prevDirs:
					newDict[prevDir] += int(first[0])
			
			i = input.readline()[:-1]

result = sum([val for val in newDict.values() if val <= 100_000])

# part 1: 
print("day7: solution for part 1: " + str(result))

totalUsed = newDict["/"]
total = 70_000_000
needed = 30_000_000
freeUpAmount = needed - (total - totalUsed)

closest = min([val for val in newDict.values() if val - freeUpAmount > 0])

# part 2:  
print("day7: solution for part 2: " + str(closest))