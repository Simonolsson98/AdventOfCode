def init():
	input = open("day7_input.txt")
	lines = []

	while(i := input.readline()):
		i = i.rstrip("\n")
		lines = [int(x) for x in i.split(",")]

	return lines

lines = init()

median = 0

if len(lines) % 2 == 0:
    median = (lines[len(lines) // 2] + lines[len(lines)//2 - 1]) / 2
else:
    median = lines[len(lines)//2]

fuel = 0
for i in range(len(lines)):
    fuel += (abs(lines[i] - median))

print("solution of part 1 is: " + str(int(fuel)))

min_fuel = float("inf")
index = 0

for i in range(max(lines)):
	sub_sum = 0
	for j in range(len(lines)):
		n = abs(lines[j] - i)
		sub_sum += n * (n + 1) // 2
	if(sub_sum < min_fuel):
		min_fuel = sub_sum
		index = i

print("solution of part 2 is: " + str(int(min_fuel)) + " fuel to align on position: " + str(index))

