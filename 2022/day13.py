def Compare(val1, val2):
	if(isinstance(val1, str) and isinstance(val2, str)):
		if(int(val1) > int(val2)):
			return 1
		elif(int(val1) < int(val2)):
			return 2
		else:
			return -1
	elif(isinstance(val1, list) and isinstance(val2, list)):
		if(len(val1) == 0 and len(val2) == 0):
			return -1
		elif(len(val1) == 0):
			right_order.append(j)
			return -1
		elif(len(val2) == 0):
			return -1
		else:
			return Compare(val1[0], val2[0])
	else:
		if(isinstance(val1, str)):
			val1 = list(val1)
		elif(isinstance(val2, str)):
			val2 = list(val2)

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
		#number to add
		else:
			some_list.append(packet[i:].split(",")[0].split("]")[0])
			i += len(packet[i:].split(",")[0].split("]")[0]) - 1
		i += 1

	return some_list


input = open("day13_input.txt")
right_order = []
j = 1
while i := input.readline()[:-1]:
	first_packet = i
	final_list = []
	result = EntryList(0, first_packet, final_list)

	flat_result = [item for sublist in result for item in sublist]

	final_list = []
	second_packet = input.readline()[:-1]
	result2 = EntryList(0, second_packet, final_list)

	flat_result2 = [item for sublist in result2 for item in sublist]

	if(len(flat_result) == 0 and len(flat_result2) != 0):
		right_order.append(j)
		i = input.readline()[:-1]
		continue
	elif(len(flat_result) != 0 and len(flat_result2) == 0):
		i = input.readline()[:-1]
		continue

	val = 12345
	for (val1, val2) in zip(flat_result, flat_result2):
		val = Compare(val1, val2)
		if(val == 1):
			right_order.append(j)

	if(val == -1):
		if(len(flat_result) < len(flat_result2)):
			right_order.append(j)


	#newline
	i = input.readline()[:-1]
	j += 1

# part 1: 
print("day13: solution for part 1: " + str(sum(right_order)))

# part 2:  
print("day13: solution for part 2: " + str())
