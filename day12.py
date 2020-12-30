import time

def main():
    input = open("day12_input.txt")
    i = input.readline()
    xpos = 0
    ypos = 0
    ship_direction = 90
    while i: #get input into a list of strings
        operator = i[0]
        range_or_dir = i[1:]
        if operator == "R":
            ship_direction = get_direction(int(range_or_dir), ship_direction)
        elif operator == "L":
            ship_direction = get_direction(-1 * int(range_or_dir), ship_direction)
        elif operator == "F":
            if ship_direction == 0:
                ypos += int(range_or_dir)
            elif ship_direction == 90:
                xpos += int(range_or_dir)
            elif ship_direction == 180:
                ypos -= int(range_or_dir)
            else: # ship_direction == 270
                xpos -= int(range_or_dir)
        elif operator == "N":
            ypos += int(range_or_dir)
        elif operator == "S":
            ypos -= int(range_or_dir)
        elif operator == "W":
            xpos -= int(range_or_dir)
        else: #operator == "E"
            xpos += int(range_or_dir)
        
        i = input.readline()
    return abs(xpos) + abs(ypos)

def get_direction(degrees, ship_dir):
    ship_dir += degrees
    while ship_dir >= 360 or ship_dir < 0:
        if(ship_dir >= 360):
            ship_dir -= 360
        elif(ship_dir < 0):
            ship_dir += 360
    return ship_dir


if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 1294
