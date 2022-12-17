def asd(i, level):
	ranges = []
	ranges_2 = []

	while i:
		sensor = i[10:].split(", ")
		sensor_x = sensor[0].split("=")[1]
		sensor_y = sensor[1].split(":")[0].split("=")[1]

		beacon = i.split("is at ")[1].split(",")
		beacon_x = beacon[0].split("=")[1]
		beacon_y = beacon[1].split("=")[1]

		manhattan_dist = abs(int(sensor_x) - int(beacon_x)) + abs(int(sensor_y) - int(beacon_y))
		
		if(int(sensor_y) > level):
			width = level - (int(sensor_y) - manhattan_dist)
			if(width < 0):
				i = input.readline()[:-1]
				continue
		else:
			width = (int(sensor_y) + manhattan_dist) - level
			if(width < 0):
				i = input.readline()[:-1]
				continue

		ranges.append(range(int(sensor_x) - width, int(sensor_x) + width))

		lower = int(sensor_x) - width
		if(lower < 0):
			lower = 0
		upper = int(sensor_x) + width
		if(upper > upper_limit - 1):
			upper = upper_limit - 1
		ranges_2.append(range(lower, upper + 1))

		i = input.readline()[:-1]

	return ranges, ranges_2

input = open("day15_input.txt")
i = input.readline()[:-1]

#4000001 for part2 but its too slow?
upper_limit = 21

beacon_loc = []
level = int(upper_limit - 1 / 2)

ranges, _ = asd(i, level)

all_ranges = []
for interval in ranges:
	all_ranges += interval

res = len(set(list(sorted(all_ranges))))

# part 1: 
print("day15: solution for part 1: " + str(res))

ranges_2 = []
for level in range(upper_limit):
	#print(level)
	input = open("day15_input.txt")
	i = input.readline()[:-1]
	ranges_2 = asd(i, level)[1]

	all_ranges = []
	for interval in ranges_2:
		all_ranges += interval

	foo = set(range(0, upper_limit))
	bar = set(all_ranges)

	if(foo != bar):
		print(f"level: {level}, bar: {bar}")
		res = int(list(foo.difference(bar))[0]) * 4000000 + level
		


# part 2:  
print("day15: solution for part 2: " + str(res))
