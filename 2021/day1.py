
input = open("day1_input.txt")
lines = []
i = input.readline()
while i:
	lines.append(int(i))
	i = input.readline()

inc_count = 0

# part 1: check all indices if they 
# increased (but not last index)
for j in range(len(lines) - 1):
	if lines[j+1] > lines[j]:
		inc_count += 1
		
print("solution for part 1: " + str(inc_count))

inc_count = 0

# part 2: check all index-3groups if they 
# increased (but not last 3 indices)
for k in range(len(lines) - 3):
	if(lines[k+1] + lines[k+2] + lines[k+3] 
		> lines[k] + lines[k+1] + lines[k+2]):
		inc_count += 1

print("solution for part 2: " + str(inc_count))