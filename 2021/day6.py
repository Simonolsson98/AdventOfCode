def init():
	input = open("day6_input.txt")
	lines = []

	while(i := input.readline()):
		i = i.rstrip("\n")
		lines = [int(x) for x in i.split(",")]

	return lines

lines = init()

def foo(days):
    occurrences = []
    for i in range(9):
        occurrences.append(lines.count(i))
    for i in range(days):
        occurrences[(i % 9) - 2] += occurrences[i % 9]
    return occurrences

print("solution of part 1 is: " + str(sum(foo(80))))
print("solution of part 2 is: " + str(sum(foo(256))))