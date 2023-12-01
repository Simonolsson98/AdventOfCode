import os
with open(os.path.dirname(__file__)+"/day01_input.txt", 'r') as input_text:
	total = 0
	while i := input_text.readline():
		for char in i:
			try:
				firstnum = int(char)
				break
			except:
				pass

		for char in i[::-1]:
			try:
				lastnum = int(char)
				total = total + int(str(firstnum)+str(lastnum))
				break
			except:
				pass

# part 1: 
print("day1: python solution for part 1: " + str(total))

with open(os.path.dirname(__file__)+"/day01_input.txt", 'r') as input_text:
	total = 0
	numdict = { "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9" }
	while i := input_text.readline():
		substr=""
		for char in i:
			try:
				firstnum = int(char)
				break
			except:
				substr+=char
				breakcon = False
				for key in numdict.keys():
					if key in substr:
						firstnum = numdict[key]
						breakcon = True
						break
				if breakcon:
					break

		substr=""
		for char in i[::-1]:
			try:
				lastnum = int(char)
				total = total + int(str(firstnum)+str(lastnum))
				break
			except:
				substr=char+substr
				breakcon = False
				for key in numdict.keys():
					if key in substr:
						lastnum = numdict[key]
						total = total + int(str(firstnum)+str(lastnum))
						breakcon = True
						break
				if breakcon:
					break

# part 2: 
print("day1: python solution for part 2: " + str(total))