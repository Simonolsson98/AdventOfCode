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
        #kinda crazy string manipulation here, but its essentially only extracting the ranges from the input
        ranges.append((int(line.split(": ")[1].split(" or ")[0].split("-")[0]), (int(line.split(": ")[1].split(" or ")[0].split("-")[1]))))
        ranges.append((int(line.split(": ")[1].split(" or ")[1].split("-")[0]), (int(line.split(": ")[1].split(" or ")[1].split("-")[1]))))

    #print(ranges)
    my_ticket = split_lines[1]
    nearby_tickets = list(split_lines[2][16:].replace("\n", ",").split(","))

    for i in range(len(nearby_tickets)):
        nearby_tickets[i] = int(nearby_tickets[i])
    
    erronous_ticket = 0
    for number in nearby_tickets:
        for number_range in ranges:
            if number_range[0] <= number <= number_range[1]: #if its in a range, its not erronous
                break
        erronous_ticket += number     
    
    return erronous_ticket

if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 1373