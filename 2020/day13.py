import time

def main():
    input = open("day13_input.txt")
    time_of_departure = int(input.readline())
    buses = input.readline()
    split_buses = buses.split(",")
    departures = []

    for i in range(len(split_buses)):
        try: #will only add the integers in split_buses
            departures.append(int(split_buses[i]))
        except ValueError: #simply ignore the error
            pass

    chosen_bus = -1
    find_time_to_depart = time_of_departure

    while True:
        for j in range(len(departures)):
            if (find_time_to_depart % departures[j] == 0):
                chosen_bus = departures[j]
        if chosen_bus != -1: #silly solution to know when to break out of the loop
            break        
        find_time_to_depart += 1 #see if a bus comes in 1 more minute (essentially)
        
    return chosen_bus * (find_time_to_depart - time_of_departure) #return bus id * time to wait 

if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 2935
