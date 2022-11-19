import time

def main():
    spoken_vals = [0,1,5,10,3,12,19] # no real need for i/o here lol
    last_spoken = spoken_vals[::-1][0] #fun way to retrieve last element of a list

    for i in range(len(spoken_vals), 2020):
        if(last_spoken not in spoken_vals[:-1]): # if number hasnt appeared before, add it and say 0
            last_spoken = 0
            spoken_vals.append(last_spoken)
        else:
            # get the index of the last occurring number that is last_spoken, 
            # and assign last_spoken to the difference between the turn value and this value
            last_spoken = i - (len(spoken_vals) - spoken_vals[:-1][::-1].index(last_spoken) - 1) 
            spoken_vals.append(last_spoken)
    
    return last_spoken
    
if __name__ == '__main__':
    start_time = time.time()
    returnVal = main() 
    print(f"answer = {returnVal}, execution time: {time.time() - start_time} seconds") #answer = 1373