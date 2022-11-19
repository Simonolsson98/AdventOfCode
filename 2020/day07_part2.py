import sys
import time

def main():
    sys.setrecursionlimit(10**6)
    input = open("day7_input.txt")
    global valid_bags
    valid_bags = 0
    lines = []
    i = input.readline()
    if(i[-1:] == "\n"):
        i = i[:-1]
    if(i[-1:] == "."):
        i = i[:-1]
    while i: #get input into a list of strings
        lines.append(i)
        i = input.readline()
        if(i[-1:] == "\n"):
            i = i[:-1]
        if(i[-1:] == "."):
            i = i[:-1]
    split_input = []
    can_carry_these_bags = []
    
    for each_line in lines: #handling input data
        split_input.append(str(each_line).split(" contain")[0])
        can_carry_these_bags.append(str(each_line).split(" contain")[1].split(","))
    find_bags(split_input, can_carry_these_bags, "shiny gold bags") #starting entry with shiny gold bags
    return valid_bags

def find_bags(split_input, can_carry_these_bags, bag_to_check):
    global valid_bags
    
    if(bag_to_check + 's' in split_input): #cover singular bag entries, for instance "1 muted tomato bag"
        bag_to_check += 's'
    if bag_to_check in split_input:
        bag_index = split_input.index(bag_to_check)
        for i in range(len(can_carry_these_bags[bag_index])):
            amount_of_bags = can_carry_these_bags[int(bag_index)][i][1]
            
            if amount_of_bags == 'n': # "contain no other bags"...
                valid_bags += 0
                return         

            valid_bags += int(amount_of_bags) #adds 3 to bag count if 3 bags etc

            for _ in range(int(amount_of_bags)): #check recursively for each bag
                find_bags(split_input, can_carry_these_bags, can_carry_these_bags[int(bag_index)][i][3:])
        return

if __name__ == '__main__':
    start_time = time.time()
    returnVal = main()
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 158493
