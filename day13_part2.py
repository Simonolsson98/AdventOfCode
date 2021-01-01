import time

def main():
    input = open("day13_input.txt")
    _ = input.readline()
    buses = input.readline()
    split_buses = buses.split(",")
    departures = []

    for i in range(len(split_buses)):
        try: #will only add the integers in split_buses
            departures.append(int(split_buses[i]))
        except ValueError: #simply ignore the error
            pass

    chosen_bus = -1

    return None

if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 2935
