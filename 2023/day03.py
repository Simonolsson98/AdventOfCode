import os
import math
import time

arr=[]
def part(part_num):
    with open(os.path.dirname(__file__)+"/day03_input.txt", 'r') as input_text:
        for line in input_text:
            arr.append(line[:-1])

    subtotal=0
    validnum = False
    currnum=""
    for rowindex in range(len(arr)):
        for colindex in range(len(arr[rowindex])):
            topleft  = "."
            topmid   = "."  
            topright = "."
            midleft  = "."  
            midright = "."  
            botleft  = "."
            botmid   = "."  
            botright = "."
            value = arr[rowindex][colindex]
            try:
                topleft  = arr[rowindex - 1][colindex - 1]
                topmid   = arr[rowindex - 1][colindex]
                topright = arr[rowindex - 1][colindex + 1]
                midleft  = arr[rowindex][colindex - 1]
                midright = arr[rowindex][colindex + 1]
                botleft  = arr[rowindex + 1][colindex - 1]
                botmid   = arr[rowindex + 1][colindex]
                botright = arr[rowindex + 1][colindex + 1]
            except:
                pass   

            # part 1
            if(part_num == "1"):
                if(value == "."):
                    currnum=""
                elif(value.isdigit()):
                    currnum += value
                    if((topleft != "." and not topleft.isdigit()) or (topmid != "." and not topmid.isdigit()) or (topright != "." and not topright.isdigit())
                            or (midleft != "." and not midleft.isdigit()) or (midright != "." and not midright.isdigit()) or (botleft != "." and not botleft.isdigit()) 
                            or (botmid != "." and not botmid.isdigit()) or (botright != "." and not botright.isdigit())):
                        validnum=True
                    if(not midright.isdigit() and validnum):
                        validnum=False
                        subtotal += int(currnum)
                        currnum = ""
            # part 2, disgusting code
            if(part_num == "2"):
                if(value == "*"):
                    nums=[]
                    number_of_parts=0
                    if(topmid.isdigit()):
                        num=topmid
                        number_of_parts += 1
                        index=colindex - 1
                        while arr[rowindex - 1][index].isdigit():
                            num = arr[rowindex - 1][index] + num
                            index -= 1

                        index=colindex + 1
                        while arr[rowindex - 1][index].isdigit():
                            num = num + arr[rowindex - 1][index] 
                            index += 1
                        nums.append(int(num))
                    else:
                        if(topright.isdigit()):
                            num=topright
                            number_of_parts += 1
                            index=colindex + 2
                            while arr[rowindex - 1][index].isdigit():
                                num = num + arr[rowindex - 1][index]
                                index += 1
                            nums.append(int(num))
                        if(topleft.isdigit()):
                            num=topleft
                            number_of_parts += 1
                            index=colindex - 2
                            while arr[rowindex - 1][index].isdigit():
                                num = arr[rowindex - 1][index] + num
                                index -= 1
                            nums.append(int(num))

                    if(botmid.isdigit()):
                        num=botmid
                        number_of_parts += 1
                        index=colindex - 1
                        while arr[rowindex + 1][index].isdigit():
                            num = arr[rowindex + 1][index] + num
                            index -= 1

                        index=colindex + 1
                        while arr[rowindex + 1][index].isdigit():
                            num = num + arr[rowindex + 1][index] 
                            index += 1
                        nums.append(int(num))
                    else:
                        if(botright.isdigit()):
                            num=botright
                            number_of_parts += 1
                            index=colindex + 2
                            try:
                                while arr[rowindex + 1][index].isdigit():
                                    num = num + arr[rowindex + 1][index]
                                    index += 1
                            except:
                                pass
                            nums.append(int(num))

                        if(botleft.isdigit()):
                            num=botleft
                            number_of_parts += 1
                            index=colindex - 2
                            while arr[rowindex + 1][index].isdigit():
                                num = arr[rowindex + 1][index] + num
                                index -= 1
                            nums.append(int(num))

                    if(midleft.isdigit()):
                        num=midleft
                        number_of_parts += 1
                        index=colindex - 2
                        while arr[rowindex][index].isdigit():
                            num = arr[rowindex][index] + num
                            index -= 1
                        nums.append(int(num))

                    if(midright.isdigit()):
                        num=midright
                        number_of_parts += 1
                        index=colindex + 2
                        while arr[rowindex][index].isdigit():
                            num = num + arr[rowindex][index]
                            index += 1
                        nums.append(int(num))

                    if(number_of_parts == 2):
                        subtotal += math.prod(nums)

    if part_num == "1":
        print(f"day3: Python solution for part 1: {subtotal}, time: {round(time.time() - start, 2)} s")
    elif part_num == "2":
        print(f"day3: Python solution for part 2: {subtotal//2}, time: {round(time.time() - start, 2)} s")

start = time.time()
part("1")
start = time.time()
part("2")