def main():
	input = open("day3_input.txt")
	lines = []
	i = input.readline()
	while i:
		lines.append(i)
		i = input.readline()

	# for part1, just 
	#return treeCount(lines, 3, 1)
	return treeCount(lines, 1, 1) * treeCount(lines, 3, 1) * treeCount(lines, 5, 1) * treeCount(lines, 7, 1) * treeCount(lines, 1, 2)

def treeCount(lines, xslope, yslope):
	xPos = 0
	trees = 0
	xMax = 31
	j = yslope
	for i in range(j, len(lines), yslope):
		xPos += xslope
		if xPos >= 31:
			xPos = xPos % 31
		if lines[i][xPos] == '#':
			trees += 1 
	return trees



if __name__ == '__main__':
	returnVal = main()
	print(returnVal)