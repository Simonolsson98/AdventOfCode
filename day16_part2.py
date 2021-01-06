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
    print(ranges)
    for list_of_numbers in each_nearby_ticket:
        check = 0
        for value in list_of_numbers:
           # print(f"for value: {value}")
            for range_index in range(0, len(ranges), 2):
               # print(f"{value} in {ranges[range_index][-1]+1} or {ranges[range_index+1][-1]+1}")
                if value in range(ranges[range_index][0], ranges[range_index][-1] + 1) or value in range(ranges[range_index + 1][0], ranges[range_index + 1][-1] + 1): #if last 
                    check += 1
                    #print(f"check: {check}")
                    if list_of_numbers not in valid_tickets and check == len(list_of_numbers):
                        #print(f"appending: {list_of_numbers}")
                        valid_tickets.append(list_of_numbers)
                    break

    try_this = {}
    """ for i in range(0, len(ranges), 2):
        try_this[i] = [] """
    print(valid_tickets[0])

    for j in range(len(valid_tickets[0])):
        for k in range(0, len(ranges), 2):
            if valid_tickets[0][j] in range(ranges[k][0], ranges[k][-1] + 1) or valid_tickets[0][j] in range(ranges[k + 1][0], ranges[k + 1][-1] + 1):
                if j not in try_this.keys():
                    try_this[j] = []
                try_this[j].append(valid_tickets[0][j])
                try_this[j].append(k/2)
       
    check = []
    print(try_this)
    while(try_this):
        for value in try_this.values():
            print(value)
            if len(value) == 2:
                check.append((value[0], value[1]))
                for i in range(len(try_this)):
                    print(i)
                    if value[1] in try_this[i]:
                        index = try_this[i].index(value[1])
                        print(index)
                        try_this[i].pop(index)
                        try_this[i].pop(index - 1)


    print(try_this)
    return None

if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 1373