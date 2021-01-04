import time

def main():
    spoken_vals = {0:(0,None), 3:(1, None), 6:(2, None)} # no real need for i/o here lol
    last_spoken = 6

    for i in range(len(spoken_vals), 10):
        (a, b) = spoken_vals[last_spoken]
        
        if b == None:
            spoken_vals[0] = (i,spoken_vals[0][0])
            last_spoken = 0
        else:
            if a - b in spoken_vals.keys():
                last_spoken = a - b
                (c, _) = spoken_vals[a - b]
                spoken_vals[a - b] = (i, c)
            else:
                last_spoken = a - b
                spoken_vals[a - b] = (i, None)
        print(f"{spoken_vals} {last_spoken}")
    
    return last_spoken
    
if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer =