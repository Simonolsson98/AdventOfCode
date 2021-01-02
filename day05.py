import math
def main():
	input = open("day5_input.txt")
	row_num = -1
	col_num = -1
	maxId = -1
	line = input.readline()
	while line:
		rowRange = range(0, 127)
		colRange = range(0, 7)
		row_max = 127
		col_max = 7
		row_min = 0
		col_min = 0
		while line:
			character = line[0]
			line = line[1:]
			if character == 'B':
				row_min = math.ceil((row_max - row_min)/2) + row_min
				rowRange = range(row_min, row_max)
			elif character == 'F':
				row_max = math.floor((row_max - row_min)/2) + row_min
				rowRange = range(row_min, row_max)
			elif character == 'L':
				col_max = math.floor((col_max - col_min)/2) + col_min
				colRange = range(col_min, col_max)
			elif character == 'R':
				col_min = math.ceil((col_max - col_min)/2) + col_min
				colRange = range(col_min, col_max)
			
		if(len(rowRange) == 0):
			row_num = row_max
		if(len(colRange) == 0):
			col_num = col_max
		if row_num * 8 + col_num > maxId:
			maxId = row_num * 8 + col_num	
		line = input.readline()
		
	
	return maxId


if __name__ == '__main__':
	returnVal = main()
	print(returnVal)