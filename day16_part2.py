from os import remove
import time

def main():
    input = open("day16_input.txt")
    lines = ""
    i = input.readline()
    
    while i: # get input into a list of strings
        lines += i
        i = input.readline()    

    split_lines = lines.split("\n\n")
    all_ranges = split_lines[0]
    all_ranges = all_ranges.split("\n")
    ranges = []
    for line in all_ranges: # get all ranges into a list
        # kinda crazy string manipulation here, but its essentially only extracting the ranges from the input, putting them in a tuple
        ranges.append(range(int(line.split(": ")[1].split(" or ")[0].split("-")[0]), (int(line.split(": ")[1].split(" or ")[0].split("-")[1]) + 1)))
        ranges.append(range(int(line.split(": ")[1].split(" or ")[1].split("-")[0]), (int(line.split(": ")[1].split(" or ")[1].split("-")[1]) + 1)))

    nearby_tickets = list(split_lines[2][16:].split("\n")) # use this to get all the ranges as entries in a list
    each_nearby_ticket = []
    for i in range(len(nearby_tickets)):
        each_nearby_ticket.append(nearby_tickets[i].split(","))
        
    for j in range(len(each_nearby_ticket)): # transform ticket numbers into ints
        for k in range(len(each_nearby_ticket[j])):
            each_nearby_ticket[j][k] = int(each_nearby_ticket[j][k])
        
    valid_tickets = []
    for list_of_numbers in each_nearby_ticket:
        check = 0
        for value in list_of_numbers:
            for range_index in range(0, len(ranges), 2):
                if value in range(ranges[range_index][0], ranges[range_index][-1] + 1) or value in range(ranges[range_index + 1][0], ranges[range_index + 1][-1] + 1): # if last 
                    check += 1
                    if list_of_numbers not in valid_tickets and check == len(list_of_numbers):
                        valid_tickets.append(list_of_numbers) # if we havent already added
                    break

    try_this = [[]]
    for i in range(1, len(valid_tickets[0])):
        try_this.append([])
    for i in range(len(valid_tickets[0])):
        for j in range(len(valid_tickets)):    
            # list of lists of columns of values
            try_this[i].append(valid_tickets[j][i])

    check = []
    for i in range(len(try_this)):
        for k in range(0, len(ranges), 2):
            for j in range(len(try_this[i])):
                value = try_this[i][j]
                if value in range(ranges[k][0], ranges[k][-1] + 1) or value in range(ranges[k+1][0], ranges[k+1][-1] + 1): 
                    if j+1 == len(try_this[i]):
                        check.append((i, int(k/2)))
                        break
                    continue
                else:
                    break

    values_appearing_once = []
    bs = []
    rows_to_look = []
    amount = 0
    index = 0
    while(check):
        for tup in check:
            bs.append(tup[1]) # add all the ranges that some column could possibly be assigned to
        for i in range(0,20):
            if bs.count(i) == 1: # if there is only 1 instance of a certain range (row), this row can be assigned to a column instantly
                values_appearing_once.append(i)

        for vals in values_appearing_once:
            for val in check: # check all tuples:
                if val[1] == vals: # for the tuples that have this unique value:
                    number_to_remove = val[0]
                    rows_to_look.append((number_to_remove, val[1]))
                    for tuple in check:
                        if tuple[0] == number_to_remove:
                            index = check.index(tuple)
                            amount += 1
                    for i in range(index, index + amount): # remove the column that got a range assigned to it
                        check.pop(index - amount + 1)
        
        # reset counters
        amount = 0
        values_appearing_once = []
        bs = []

    resulting_cols = []
    for i in range(0, 6): # the first 6 rows are the departure ranges
        for val in rows_to_look:
            if val[1] == i:
                resulting_cols.append(val[0])
                break
    
    my_ticket = split_lines[1][13:].split(",") # get my ticket values into a list
    result = 1
    for index in resulting_cols:
        result *= int(my_ticket[index]) # multply these values together
    
    return result         

if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 3029180675981