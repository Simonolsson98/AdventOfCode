import string
def main():
    sum_of_questions = 0
    set_of_values = set()
    input = open("day6_input.txt")
    input_string = ""
    lines = []
    i = input.readline()
    while i: #get input into a list of strings
        lines.append(i)
        i = input.readline()
    for s in lines:
        input_string += s
    list_of_groups = input_string.split("\n\n")
    alphabet_string = string.ascii_lowercase

    for group in list_of_groups:
        group_members = group.split("\n") #split answers from each member into a separate list

        for individual_member in group_members: #for each member
            for answer in individual_member: #for each answer from a member
                set_of_values.add(answer) #add each (unique) character to a set

            alphabet_string = set_of_values.intersection(alphabet_string) #will return answers that are shared between all in a group
            set_of_values.clear() #prepare for answers from a new group member

        sum_of_questions += len(alphabet_string) #length of the set = amount of unique yes answers
        alphabet_string = string.ascii_lowercase #prepare for new group

    return sum_of_questions

if __name__ == '__main__':
	returnVal = main()
	print(returnVal) #answer = 3254