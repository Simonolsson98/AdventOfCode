from os import times
import time

def main():
    input = open("day13_input.txt")
    _ = input.readline()
    buses = input.readline()
    split_buses = buses.split(",")
    departures = list(split_buses)
    #print(departures)
    result = -1
    timestamp = 1
    max_departure = 0
    """ for i in range(len(departures)):
        print(i)
        try:
            print(max_departure)
            if int(departures[i]) > max_departure:
                print(int(departures[i]))
                print(i)
                max_departure = departures[i]
        except TypeError:
            pass
        except ValueError:
            pass """
    
    while timestamp >= 1:
        #print(timestamp)
        for j in range(len(departures)):
            try:
                if((timestamp + j) % int(departures[j]) != 0):
                    timestamp += (732 - int(departures[j]))
                    break
            except ValueError: #ignore 'x' entries
                pass
            #print(f"GOT PAST: {departures[j]}")
            if(j == len(departures)):
                return timestamp
    

    return result

if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 
