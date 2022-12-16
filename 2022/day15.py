input = open("day15_input.txt")
i = input.readline()[:-1]

while i:
	sensor = i[10:].split(", ")
	sensor_x = sensor[0].split("=")[1]
	sensor_y = sensor[1].split(":")[0].split("=")[1]

	beacon = i.split("is at ")[1].split(",")
	beacon_x = beacon[0].split("=")[1]
	beacon_y = beacon[1].split("=")[1]

	manhattan_dist = abs(int(sensor_x) - int(beacon_x)) + abs(int(sensor_y) - int(beacon_y))
	print(f"manhattan_dist: {manhattan_dist}")
	i = input.readline()[:-1]

# part 1: 
print("day15: solution for part 1: " + str())

# part 2:  
print("day15: solution for part 2: " + str())
