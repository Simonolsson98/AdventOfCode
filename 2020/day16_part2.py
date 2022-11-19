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

    all_nearby_tickets = list(split_lines[2][16:].split("\n")) # use this to get all the ranges as entries in a list
    
    ticket_values = []
    for i in range(len(all_nearby_tickets)): #split each ticket into their own list
        ticket_values.append(all_nearby_tickets[i].split(","))
        
    for j in range(len(ticket_values)): # transform ticket numbers into ints
        for k in range(len(ticket_values[j])):
            ticket_values[j][k] = int(ticket_values[j][k])
        
    valid_tickets = []
    for each_value in ticket_values:
        counter = 0
        for value in each_value:
            for range_index in range(0, len(ranges), 2):
                if value in range(ranges[range_index][0], ranges[range_index][-1] + 1) or value in range(ranges[range_index + 1][0], ranges[range_index + 1][-1] + 1): 
                    counter += 1
                    if counter == len(each_value):
                        valid_tickets.append(each_value) # if all numbers in the ticket fit in some column, the ticket is valid
                    break

    list_of_columns = [[]]
    for i in range(1, len(valid_tickets[0])):
        list_of_columns.append([])
    for i in range(len(valid_tickets[0])):
        for j in range(len(valid_tickets)):    
            # list of lists of columns of values
            list_of_columns[i].append(valid_tickets[j][i])

    row_col_pair = []
    for i in range(len(list_of_columns)):
        for k in range(0, len(ranges), 2):
            for j in range(len(list_of_columns[i])):
                value = list_of_columns[i][j]
                if value in range(ranges[k][0], ranges[k][-1] + 1) or value in range(ranges[k+1][0], ranges[k+1][-1] + 1): 
                    if j+1 == len(list_of_columns[i]): #if all columns fit in a certain range (row i)
                        row_col_pair.append((i, int(k/2))) #designate the column to this row
                        break
                    continue
                else:
                    break

    values_appearing_once = []
    row_values = []
    rows_to_look = []
    amount = 0
    index = 0
    while(row_col_pair): #while there are pairs left
        for tup in row_col_pair:
            row_values.append(tup[1]) # add all the ranges that some column could possibly be assigned to
        for i in range(0,20):
            if row_values.count(i) == 1: # if there is only 1 instance of a certain range (row), this row can be assigned to a column instantly
                values_appearing_once.append(i)

        for vals in values_appearing_once:
            for val in row_col_pair: # check all tuples:
                if val[1] == vals: # for the tuples that have this unique value:
                    number_to_remove = val[0]
                    rows_to_look.append((number_to_remove, val[1]))
                    for tuple in row_col_pair:
                        if tuple[0] == number_to_remove:
                            index = row_col_pair.index(tuple)
                            amount += 1
                    for i in range(index, index + amount): # remove the column that got a range assigned to it
                        row_col_pair.pop(index - amount + 1)
        
        # reset counters
        amount = 0
        values_appearing_once = []
        row_values = []

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