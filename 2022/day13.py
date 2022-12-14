def Compare(val1, val2):
	if(isinstance(val1, str) and isinstance(val2, str)):
		print(f"comparing {val1} to {val2}")
		if(int(val1) < int(val2)):
			return 2
		elif(int(val1) > int(val2)):
			return 1
		else:
			#print(f"no difference!")
			return -1
	elif(isinstance(val1, list) and isinstance(val2, list)):
		print(f"both lists: {val1} and {val2}")
		if(len(val1) == 0 and len(val2) == 0):
			return -1
		elif(len(val1) == 0):
			return 2
		elif(len(val2) == 0):
			return 1

		for k in range(min(len(val1), len(val2))):
			#print(f"k: {k} while looping over: {min(len(val1), len(val2))}")
			#print(f"sending with {val1[k]} and {val2[k]}")
			val = Compare(val1[k], val2[k])
			#print(f"returned: {val}")
			if(val != -1):
				#print(f"returning {val} for values: {val1[k]} and {val2[k]}")
				return val
			if(len(val1[k]) == k and len(val2[k]) != k):
				#print("what is this return2")
				return 2
			elif(len(val1[k]) != k and len(val2[k]) == k):
				#print("what is this return")
				return 1

		if(len(val1) < len(val2)):
			return 2
		elif(len(val1) > len(val2)):
			#print("??")
			return 1
		else:
			return -1
	else:
		#print(f"val1: {val1} and val2: {val2}")
		if(isinstance(val1, str)):
			#print(f"val1: {val1} to list")
			val1 = list(val1)
		elif(isinstance(val2, str)):
			#print(f"val2: {val2} to list")
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

asd = []
input = open("day13_input.txt")
right_order = []
index = 1
while i := input.readline()[:-1]:
	first_packet = i
	final_list = []
	result = EntryList(0, first_packet, final_list)

	flat_result = [item for sublist in result for item in sublist]

	final_list = []
	second_packet = input.readline()[:-1]
	result2 = EntryList(0, second_packet, final_list)

	flat_result2 = [item for sublist in result2 for item in sublist]

	print(f"first:  {flat_result}")
	print(f"second: {flat_result2}")

	val = Compare(flat_result, flat_result2)
	if(val == 1 or val == -1):
		pass
	if(val == 2):
		asd.append(index - 1)
		right_order.append(index)

	#newline
	i = input.readline()[:-1]
	index += 1
	
print(sum(asd))
# ANS: 5529
# part 1: 
print("day13: solution for part 1: " + str(sum(right_order)))

# part 2:  
print("day13: solution for part 2: " + str())
