def main():
	input = open("day1_input.txt")
	lines = []
	i = input.readline()
	while i:
		lines.append(i)
		i = input.readline()
	for j in range(int(len(lines))):
		sum1 = int(lines[j])
		for k in range(int(len(lines))):
			sum2 = int(lines[k])
			if sum1 + sum2 == 2020:
				return sum1 * sum2

if __name__ == '__main__':
	returnVal = main()
	print(returnVal)