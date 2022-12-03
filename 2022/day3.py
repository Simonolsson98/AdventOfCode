input = open("day3_input.txt")
i = input.readline()

def ElementToPrio(element):
	if(element.isupper()):
		return ord(element) - 38
	else:
		return ord(element) - 96

shared_chars = []
prio_total = 0
while i:
	first_compartment = i[:int(len(i[:-1])/2)]
	second_compartment = i[int(len(i[:-1])/2):]
	
	shared_chars.append(set(first_compartment) & set(second_compartment))
	i = input.readline()

for element in shared_chars:
	prio_total += ElementToPrio(list(element)[0])

# part 1: 
print("solution for part 1: " + str(prio_total))

#--------------------------------part 2--------------------------------------------#

input = open("day3_input.txt")
i = input.readline()

shared_chars = []
prio_total = 0
while i:
	first_rucksack  = i[:-1]
	second_rucksack = input.readline()[:-1]
	third_rucksack = input.readline()[:-1]

	shared_chars.append(set(first_rucksack) & set(second_rucksack) & set(third_rucksack))
	i = input.readline()

for element in shared_chars:
	prio_total += ElementToPrio(list(element)[0])

# part 2:  
print("solution for part 2: " + str(prio_total))