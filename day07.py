import math
def main():
    input = open("day7_input.txt")
    global valid_bags
    global already_checked_bags
    already_checked_bags = set()
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
    
    find_bags(lines, "shiny gold bags")
    return len(already_checked_bags)


def find_bags(lines, bag_to_check):
    global valid_bags
    global already_checked_bags
    bigger_bag = set()
    for each_line in lines:
        split_input = str(each_line).split(" contain")
        can_carry_these_bags = split_input[1].split(",")
        for i in range(0, len(can_carry_these_bags)):
            if(can_carry_these_bags[i][3:] == bag_to_check or can_carry_these_bags[i][3:] + 's' == bag_to_check): #cover both "..bag" and "..bags" input
                bigger_bag.add(split_input[0]) #bags that can contain the bag we are interested in
    if len(bigger_bag) == 0: #no more recursive calls needed, so return
        return len(already_checked_bags)
    for bags in bigger_bag:
        if(bags not in already_checked_bags): #if we havent already checked this bag, check the types of bags that bags hold this bag!
            already_checked_bags.add(bags)
            find_bags(lines, bags)    
    return
            
if __name__ == '__main__':
	returnVal = main()
	print(returnVal) #answer = 235