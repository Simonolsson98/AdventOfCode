import time

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
		if(upper > upper_limit):
			upper = upper_limit
		ranges_2.append(range(lower, upper + 1))

		i = input.readline()[:-1]

	ranges_2 = sorted(ranges_2, key=lambda r: r.start)
	return ranges, ranges_2

input = open("day15_input.txt")
i = input.readline()[:-1]

# 21 for part1, 4000001 for part2
upper_limit = 4000001

level = int((upper_limit - 1) / 2)
ranges, _ = asd(i, level)

all_ranges = []
for interval in ranges:
	all_ranges += interval

res = len(set(list(sorted(all_ranges))))

# part 1: 
print("day15: solution for part 1: " + str(res))

start_time = time.time()

foo = set(range(0, upper_limit))
cont = False
missing = 0

#reversed here finds result faster, very ugly
for level in reversed(range(upper_limit)):
	if(level % 10000 == 0):
		print(level)

	input = open("day15_input.txt")
	i = input.readline()[:-1]
	ranges_2 = asd(i, level)[1]
	
	old_interval = ranges_2[0]
	largest = old_interval.stop
	for interval in ranges_2[1:]:
		if(interval.start > old_interval.stop and interval.start > largest):
			missing = interval.start - 1
			cont = True
			break
		if(interval.stop > largest):
			largest = interval.stop
		old_interval = interval

	if(cont):
		res = (missing * (upper_limit - 1)) + level
		break

# part 2:  
print(f"day15: solution for part 2: {str(res)}, execution time: {str(round(time.time() - start_time, 2))} seconds")
