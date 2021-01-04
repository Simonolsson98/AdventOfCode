import time

def main():
    spoken_vals = {0:(0,None), 3:(1, None), 6:(2, None)} # no real need for i/o here lol
    last_spoken = 6

    for i in range(len(spoken_vals), 2020):
        (a, b) = spoken_vals[last_spoken]
        if b == None:
            spoken_vals[i] = (i,a)
        else:
            if a - b in spoken_vals.keys():
                (c, _) = spoken_vals[a - b]
                spoken_vals[a - b] = (i, c)
            else:
                spoken_vals[a - b] = (i, None)


    print(spoken_vals.keys())
    return last_spoken
    
if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer =