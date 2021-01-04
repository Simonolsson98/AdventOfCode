import time

def main():
    spoken_vals = {0:0,1:1,5:2,10:3,3:4,12:5,19:6} # no real need for i/o here lol
    last_spoken = 19 #fun way to retrieve last element of a list

    for i in range(len(spoken_vals), 2020):
        
        index = spoken_vals[last_spoken]
        print(index)
        spoken_vals[last_spoken] = i
        last_spoken = i - index - 1
        
    
    return last_spoken
    
if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer =