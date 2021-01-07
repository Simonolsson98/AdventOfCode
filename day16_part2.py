from os import remove
import time
import math
def main():
    input = open("day16_input.txt")
    lines = ""
    i = input.readline()
    
    while i: #get input into a list of strings
        lines += i
        i = input.readline()    

    split_lines = lines.split("\n\n")
    all_ranges = split_lines[0]
    all_ranges = all_ranges.split("\n")
    ranges = []
    for line in all_ranges: #get all ranges into a list
        #kinda crazy string manipulation here, but its essentially only extracting the ranges from the input, putting them in a tuple
        ranges.append(range(int(line.split(": ")[1].split(" or ")[0].split("-")[0]), (int(line.split(": ")[1].split(" or ")[0].split("-")[1]) + 1)))
        ranges.append(range(int(line.split(": ")[1].split(" or ")[1].split("-")[0]), (int(line.split(": ")[1].split(" or ")[1].split("-")[1]) + 1)))

    nearby_tickets = list(split_lines[2][16:].split("\n")) #use this to get all the ranges as entries in a list
    each_nearby_ticket = []
    for i in range(len(nearby_tickets)):
        each_nearby_ticket.append(nearby_tickets[i].split(","))
        
    for j in range(len(each_nearby_ticket)): #transform ticket numbers into ints
        for k in range(len(each_nearby_ticket[j])):
            each_nearby_ticket[j][k] = int(each_nearby_ticket[j][k])
        
    valid_tickets = []
    for list_of_numbers in each_nearby_ticket:
        check = 0
        for value in list_of_numbers:
            for range_index in range(0, len(ranges), 2):
                if value in range(ranges[range_index][0], ranges[range_index][-1] + 1) or value in range(ranges[range_index + 1][0], ranges[range_index + 1][-1] + 1): #if last 
                    check += 1
                    if list_of_numbers not in valid_tickets and check == len(list_of_numbers):
                        valid_tickets.append(list_of_numbers)
                    break

    try_this = [[]]
    for i in range(1, len(valid_tickets[0])):
        try_this.append([])
    for i in range(len(valid_tickets[0])):
        for j in range(len(valid_tickets)):    
            #list of lists of columns of values
            try_this[i].append(valid_tickets[j][i])

    check = []
    print(ranges)
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

    print(check)
    asd = []
    bs = []

    while(True):
        for c in check:
            bs.append(c[1])
            
        for i in range(0,20):
            if bs.count(i) == 1:
                asd.append(i)
        print(asd)
        for vals in asd:
            print(vals)
            for val in check:
                print(val)
                if val[1] == vals:
                    for remove_these in check:
                        if remove_these[0] == val[0]:
                            print(f"REMOVING: {remove_these}")
                            check.remove(remove_these)
        asd = []
        bs = []

    print(check)
    rows_to_look = []
    for i in range(len(all_ranges)):
        if all_ranges[i][0:3] == "dep":
            rows_to_look.append(i)

    #print(rows_to_look)
    my_ticket = split_lines[1][13:].split(",")
    #print(my_ticket)
    result = 1
    for i in range(6):
        result *= int(my_ticket[i])
    return result         

    """ while(True):
        if all(not value for value in try_this.values()):
            break
        #print(len(try_this[0])
        for value in try_this.values():
            if len(value) == 2:
                check.append((value[0], value[1]))
            print(value)
            for k in range(0, 19):
                #print(i)
                try:
                    if k not in value:
                        for key in try_this.keys():
                            try:
                                valid_tickets[i][k]
                                vals = try_this[key]
                                #print(vals)
                                index = vals.index(k)
                                vals.remove(k)
                                vals.pop(index - 1)
                                #print(vals)
                                try_this[key] = vals
                                #print("REMOVING")
                            except ValueError:
                                pass
                except ValueError:
                    pass """



if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 3029180675981