import time

def main():
    input = open("day12_input.txt")
    i = input.readline()
    xpos = 0
    ypos = 0
    waypoint = (10, 1) #(E, N)
    while i: #get input into a list of strings
        operator = i[0]
        range_or_dir = i[1:]
        if operator == "R":
            pass
        elif operator == "L":
            pass
        elif operator == "F":
            xpos += waypoint[0]
            ypos += waypoint[1]
        elif operator == "N":
            pass
        elif operator == "S":
            pass
        elif operator == "W":
            pass
        else: #operator == "E"
            pass
        
        i = input.readline()
    return abs(xpos) + abs(ypos) #manhattan distance

def get_direction(degrees, ship_dir):
    
    return ship_dir


if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 1294
