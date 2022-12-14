def Compare(val1, val2):
	if(isinstance(val1, str) and isinstance(val2, str)):
		if(int(val1) < int(val2)):
			return 2
		elif(int(val1) > int(val2)):
			return 1
		else:
			return -1
	elif(isinstance(val1, list) and isinstance(val2, list)):
		for k in range(min(len(val1), len(val2))):
			val = Compare(val1[k], val2[k])
			if(val != -1):
				return val
			if(len(val1[k]) == k and len(val2[k]) != k):
				return 2
			elif(len(val1[k]) != k and len(val2[k]) == k):
				return 1

		if(len(val1) < len(val2)):
			return 2
		elif(len(val1) > len(val2)):
			return 1
		else:
			return -1
	else:
		if(isinstance(val1, str)):
			val1 = [val1]
		elif(isinstance(val2, str)):
			val2 = [val2]

		return Compare(val1, val2)

def EntryList(i, packet, some_list):
	local_list = []
	while i <= len(packet) - 1:
		if(packet[i] == "["):
			local_list, i = EntryList(i + 1, packet, local_list)
			some_list.append(local_list)
			local_list = []
			if(i == len(packet) - 1):
				return some_list
		elif(packet[i] == "]"):
			return some_list, i
		elif(packet[i] == ","):
			pass
		# number to add
		else:
			some_list.append(packet[i:].split(",")[0].split("]")[0])
			i += len(packet[i:].split(",")[0].split("]")[0]) - 1
		i += 1

	return some_list

input = open("day13_input.txt")
right_order = []
index = 1

lower_than_6 = 0
lower_than_2 = 0
while i := input.readline()[:-1]:
	first_packet = i
	final_list = []
	result = EntryList(0, first_packet, final_list)

	first_flat_packet = [item for sublist in result for item in sublist]

	final_list = []
	second_packet = input.readline()[:-1]
	result = EntryList(0, second_packet, final_list)

	second_flat_packet = [item for sublist in result for item in sublist]

	val = Compare(first_flat_packet, second_flat_packet)
	if(val == 2):
		right_order.append(index)

	# part2, count how many packets are to the left of either decider
	if(Compare(first_flat_packet, [['2']]) == 2):
		lower_than_2 += 1
	if(Compare(first_flat_packet, [['6']]) == 2):
		lower_than_6 += 1
	if(Compare(second_flat_packet, [['2']]) == 2):
		lower_than_2 += 1
	if(Compare(second_flat_packet, [['6']]) == 2):
		lower_than_6 += 1

	#newline
	i = input.readline()[:-1]
	index += 1

# part 1: 
print("day13: solution for part 1: " + str(sum(right_order)))

# to account for index not being zero based 
lower_than_2 += 1
lower_than_6 += 1

# [[2]] is lower than [[6]]
lower_than_6 += 1

# part 2:  
print("day13: solution for part 2: " + str(lower_than_2 * lower_than_6))
