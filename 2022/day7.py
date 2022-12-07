input = open("day7_input.txt")
i = input.readline()[:-1]

# somehow allow duplicate dirs..
asd = [newDict = {"/": 0}]

prevDirs = []
currentDir = ""
while i:
	if(i[:4] == "$ cd"):
		if(currentDir != "" and i[5:] != ".."):
			prevDirs.append(currentDir)
			print(f"adding {currentDir} to prevDirs")

		currentDir = i[5:]
		if(currentDir == ".."):
			currentDir = prevDirs.pop()
			print(f"going back to {currentDir}")

		print(f"CD TO {currentDir}")

		i = input.readline()[:-1]
	elif(i[:4] == "$ ls"):
		i = input.readline()[:-1]
		while(i != "" and i[0] != "$"):
			first = i.split(" ")
			print(f"{first[0]} {first[1]}")
			if(first[0] == "dir"):
				newDict.update({first[1]: 0})
			else:
				newDict[currentDir] += int(first[0])
				print(f"adding {first[0]} to currentDir: {currentDir}")
				for prevDir in prevDirs:
					newDict[prevDir] += int(first[0])
					print(f"adding {first[0]} to prevDir: {prevDir}")
			
			i = input.readline()[:-1]

result = sum([val for val in newDict.values() if val <= 100_000])

print(newDict)

# part 1: 
print("day7: solution for part 1: " + str(result))

# part 2:  
print("day7: solution for part 2: " + str())