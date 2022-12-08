input = open("day8_input.txt")
i = input.readline()[:-1]
arr = []
count_of_visible_trees = 0

while i:
	arr.append([i])
	i = input.readline()[:-1]

max_score = 0
for i in range(len(arr)):
	current_row = arr[i][0]
	for j in range(len(current_row)):
		current_tree = arr[i][0][j]
		score = 1
		view_len = 0

		if(i == 0 or j == 0 or i + 1 == len(arr) or j + 1 == len(current_row)):
			count_of_visible_trees += 1
		else:
			visibleLeft = True
			visibleRight = True
			visibleUp = True
			visibleDown = True

			for up in reversed(range(i)):
				view_len += 1
				if(arr[up][0][j]) >= current_tree:
					visibleUp = False
					break

			score *= view_len
			view_len = 0
			for down in range(i + 1, len(arr)):
				view_len += 1
				if(arr[down][0][j]) >= current_tree:
					visibleDown = False
					break
			score *= view_len
			view_len = 0
			for left in reversed(range(j)):
				view_len += 1
				if(arr[i][0][left]) >= current_tree:
					visibleLeft = False
					break
			
			score *= view_len
			view_len = 0
			for right in range(j + 1, len(current_row)):
				view_len += 1
				if(arr[i][0][right]) >= current_tree:
					visibleRight = False
					break
			
			if(visibleRight or visibleUp or visibleLeft or visibleDown):
				count_of_visible_trees += 1
			
			score *= view_len
			view_len = 0
			if(score > max_score):
				max_score = score

				
# part 1: 
print("day8: solution for part 1: " + str(count_of_visible_trees))

# part 2:  
print("day8: solution for part 2: " + str(max_score))