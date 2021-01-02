import time

def main():
    input = open("day13_input.txt")
    _ = input.readline() #ignore first line of input
    buses = input.readline()
    departures = list(buses.split(","))

    mods = {}
    for idx, bus_id in enumerate(departures):
        if bus_id != 'x': #ignore x's
            mods[int(bus_id)] = -idx % int(bus_id)

    iterator = 0
    increment = 1
    for bus in mods.keys():
        while iterator % bus != mods[bus]:
            iterator += increment
        increment *= bus

    return iterator

if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 836024966345345