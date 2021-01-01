import time

def main():
    input = open("day12_input.txt")
    i = input.readline()
    xpos = 0
    ypos = 0
    waypoint = (1, 10) #(N/S, E/W)
    while i: #get input into a list of strings
        operator = i[0]
        range_or_dir = i[1:]
        if operator == "R":
            for i in range(0, range_or_dir / 90): #turn 3 times for 270 degrees, for example
                if waypoint[0] >= 0 and waypoint[1] >= 0:
                    waypoint = (-waypoint[1], waypoint[0])
                elif waypoint[0] < 0 and waypoint[1] >= 0:
                    waypoint = (-waypoint[1], -waypoint[0])
                elif waypoint[0] < 0 and waypoint[1] < 0:
                    waypoint = (-waypoint[1], waypoint[0])
                else:
                    waypoint = (-waypoint[1], waypoint[0])
        elif operator == "L":
            for i in range(0, range_or_dir / 90):
                if waypoint[0] >= 0 and waypoint[1] >= 0:
                    waypoint = (waypoint[1], -waypoint[0])
                elif waypoint[0] < 0 and waypoint[1] >= 0:
                    waypoint = (-waypoint[1], -waypoint[0])
                elif waypoint[0] < 0 and waypoint[1] < 0:
                    waypoint = (-waypoint[1], waypoint[0])
                else:
                    waypoint = (waypoint[1], waypoint[0])
        elif operator == "F":
            xchange = waypoint[0] * range_or_dir
            ychange = waypoint[1] * range_or_dir
            xpos += xchange
            ypos += ychange
        elif operator == "N":
            waypoint[0] += range_or_dir
        elif operator == "S":
            waypoint[0] -= range_or_dir
        elif operator == "W":
            waypoint[1] -= range_or_dir
        else: #operator == "E"
            waypoint[1] += range_or_dir
        
        i = input.readline()
    return abs(xpos) + abs(ypos) #manhattan distance
    
if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 1294
