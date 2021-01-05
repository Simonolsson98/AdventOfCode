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
        ranges.append(line.split(": ")[1].split(" or ")[0])
        ranges.append(line.split(": ")[1].split(" or ")[1])

    #print(ranges)
    my_ticket = split_lines[1]
    nearby_tickets = split_lines[2]
    
if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 1373