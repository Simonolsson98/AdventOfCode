from os import times
import time
from typing import Type

def main():
    input = open("day13_input.txt")
    _ = input.readline()
    buses = input.readline()
    departures = list(buses.split(","))
    print(departures)
    result = -1
    real_buses = []
    
    for j in range(len(departures)):
        try:
            int(departures[j])
            real_buses.append(int(departures[j])) #adds the buses with real ID's to a separate list
        except ValueError: #ignore 'x' entries
            pass
    real_buses.sort()
    print(real_buses)

    return None

if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 
