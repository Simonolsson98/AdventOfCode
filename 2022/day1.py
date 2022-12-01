input = open("day1_input.txt")
lines = []
i = input.readline()
subtotal = 0;

while i:
	subtotal += int(i)
	i = input.readline()
	if(i == '\n'):
		lines.append(subtotal)
		subtotal = 0
		i = input.readline()

# part 1: 
		
print("solution for part 1: " + str(max(lines)))

# part 2:  
topThreeSum = (sum(sorted(lines, reverse=True)[:3]))

print("solution for part 2: " + str(topThreeSum))