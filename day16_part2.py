import time

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
        ranges.append((int(line.split(": ")[1].split(" or ")[0].split("-")[0]), (int(line.split(": ")[1].split(" or ")[0].split("-")[1]))))
        ranges.append((int(line.split(": ")[1].split(" or ")[1].split("-")[0]), (int(line.split(": ")[1].split(" or ")[1].split("-")[1]))))

    nearby_tickets = list(split_lines[2][16:].split("\n")) #use this to get all the ranges as entries in a list
    each_nearby_ticket = []
    for i in range(len(nearby_tickets)):
        each_nearby_ticket.append(nearby_tickets[i].split(","))
        
    for j in range(len(each_nearby_ticket)): #transform ticket numbers into ints
        for k in range(len(each_nearby_ticket[j])):
            each_nearby_ticket[j][k] = int(each_nearby_ticket[j][k])
        
    valid_tickets = []
    for number in each_nearby_ticket:
        check = 0
        for value in number:
            for number_range in ranges:
                if number_range[0] <= value and value <= number_range[1]: #if last 
                    check += 1
                    if number not in valid_tickets and check == len(number):
                        valid_tickets.append(number)
                    break          

    print(nearby_tickets)
    print(valid_tickets)
    for i in range(len(valid_tickets)):
        pass

    return None

if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 1373