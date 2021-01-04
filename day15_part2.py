import time

def main(part):
    spoken_vals = {0:(0,None), 1:(1,None), 5:(2,None), 10:(3,None),3:(4,None),12:(5,None),19:(6,None)} # no real need for i/o here lol
    last_spoken = 19

    for i in range(len(spoken_vals), part):
        (a, b) = spoken_vals[last_spoken]
        if b == None:
            spoken_vals[0] = (i, spoken_vals[0][0])
            last_spoken = 0
        else:
            if a - b in spoken_vals.keys():
                last_spoken = a - b
                (c, _) = spoken_vals[a - b]
                spoken_vals[a - b] = (i, c)
            else:
                last_spoken = a - b
                spoken_vals[a - b] = (i, None)

    return last_spoken
    
if __name__ == '__main__':
    start_time = time.time()
    returnVal = main(2020) 
    print(f"part 1: answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 1373
    start_time = time.time()
    returnVal = main(30_000_000)
    print(f"part 2: answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 112458