def init():
	input = open("day8_input.txt")
	lines = []
	segments = []
	while(i := input.readline()):
		i = i.rstrip("\n").split(" | ")
		lines.append(i[1].split(" "))
		segments.append(i[0].split(" "))

	return lines, segments

lines, segments = init()

count = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        length_to_check = len(lines[i][j])
        if (length_to_check == 2 or length_to_check == 3 or length_to_check == 4 or length_to_check == 7):
            count += 1

for i in range(len(lines)):
	for j in range(len(lines[i])):
		lines[i][j] = set(lines[i][j])

print("solution of part 1 is: " + str(count))


for i in range(len(segments)):
	for j in range(len(segments[i])):
		segments[i][j] = set(segments[i][j])
	
total = 0

for i in range(len(segments)):
	ans = [set() for _ in range(10)]
	for j in range(len(segments[i])):
		if (len(segments[i][j]) == 2):
			ans[1] = segments[i][j]
		elif (len(segments[i][j]) == 3):
			ans[7] = segments[i][j]
		elif(len(segments[i][j]) == 4):
			ans[4] = segments[i][j]
		elif(len(segments[i][j]) == 7):
			ans[8] = segments[i][j]
	ans[9] = [x for x in segments[i] if len(x) == 6 and len(ans[4].intersection(x)) == len(ans[4]) ][0]
	ans[3] = [x for x in segments[i] if len(x) == 5 and len(ans[7].intersection(x)) == len(ans[7]) ][0]
	ans[0] = [x for x in segments[i] if len(x) == 6 and len(ans[7].intersection(x)) == len(ans[7]) and ans[9].intersection(x) != x ][0]
	ans[6] = [x for x in segments[i] if len(x) == 6 and len(ans[0].intersection(x)) != len(x) and len(ans[9].intersection(x)) != len(x) ][0] 
	ans[5] = [x for x in segments[i] if len(x) == 5 and len(ans[6].intersection(x)) == 5][0]
	ans[2] = [x for x in segments[i] if len(x) == 5 and x != ans[3] and x != ans[5]][0]

	result = ""
	for x in lines[i]:
		result += str(ans.index(x))

	total += int(result)

print("solution of part 2 is: " + str(total))