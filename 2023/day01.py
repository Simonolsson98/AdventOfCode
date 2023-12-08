import os
import time

start = time.time()
with open(os.path.dirname(__file__)+"/day01_input.txt", 'r') as input_text:
	total = 0
	for i in input_text:
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
print(f"day8: Python solution for part 1: {str(total)}, time: {round(time.time() - start, 3)} s")

start = time.time()
with open(os.path.dirname(__file__)+"/day01_input.txt", 'r') as input_text:
	total = 0
	numdict = { "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9" }
	for i in input_text:
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
				break
			except:
				substr=char+substr
				breakcon = False
				for key in numdict.keys():
					if key in substr:
						lastnum = numdict[key]
						breakcon = True
						break
				if breakcon:
					break
					
		total = total + int(str(firstnum)+str(lastnum))

# part 2: 
print(f"day1: Python solution for part 2: {str(total)}, time: {round(time.time() - start, 3)} s")