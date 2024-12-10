package main

import (
    "fmt"
    "strings"
    "os"
    "2024/utils"
    "strconv"
    "path/filepath"
    "time"
    "maps"
    "slices"
    "math"
)

type test struct {
    file int
    freespace int
}

func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

    start := time.Now()
    var fileFreespaceTuple = []test{}
    diskMap := strings.Split(input, "")

    // extra 0 for the last "pair of values" to represent 0 free spaces
    if(len(diskMap) % 2 != 0){
        diskMap = append(diskMap, "0")
    }

    for i := 0; i < len(diskMap); i+=2 {
        fileVal, _ := strconv.Atoi(diskMap[i])
        freespaceVal, _ := strconv.Atoi(diskMap[i + 1])
        fileFreespaceTuple = append(fileFreespaceTuple, test{file: fileVal, freespace: freespaceVal})
    }
    
    currentPickingIndex := len(diskMap) - 2
    mapOfMovedDiskFiles := make(map[int][]int)
    for i, val := range fileFreespaceTuple {
        if i == len(fileFreespaceTuple) {
            break
        }

        freeSpacesToReplace := val.freespace
        for {
            if currentPickingIndex <= 2 * i {
                break
            }

            piecesToBeMoved, _ := strconv.Atoi(diskMap[currentPickingIndex])
            // nothing left to take from in this pair, go to next candidate
            if piecesToBeMoved == 0 {
                currentPickingIndex -= 2
                continue
            }
            
            if freeSpacesToReplace > piecesToBeMoved{
                diff := freeSpacesToReplace - piecesToBeMoved

                diskMap[2*i+1] = strconv.Itoa(diff)
                diskMap[currentPickingIndex] = "0"

                self, _ := strconv.Atoi(diskMap[currentPickingIndex+1])
                diskMap[currentPickingIndex+1] = strconv.Itoa(self + piecesToBeMoved)
                
                for j := 0; j < piecesToBeMoved; j++ {
                    mapOfMovedDiskFiles[i] = append(mapOfMovedDiskFiles[i], int(math.Ceil(float64(currentPickingIndex/2))))
                }

                freeSpacesToReplace = diff
                continue
            } else if freeSpacesToReplace == piecesToBeMoved {
                diskMap[2*i+1] = "0"

                diskMap[currentPickingIndex] = "0"

                asd2, _ := strconv.Atoi(diskMap[currentPickingIndex + 1])
                diskMap[currentPickingIndex + 1] = strconv.Itoa(asd2 + piecesToBeMoved)
                
                for j := 0; j < piecesToBeMoved; j++ {
                    mapOfMovedDiskFiles[i] = append(mapOfMovedDiskFiles[i], int(math.Ceil(float64(currentPickingIndex/2))))
                }
                
                break
            } else { // more than enough to move
                diff := piecesToBeMoved - freeSpacesToReplace
                diskMap[2*i+1] = "0"

                diskMap[currentPickingIndex] = strconv.Itoa(diff)

                asd2, _ := strconv.Atoi(diskMap[currentPickingIndex + 1])
                diskMap[currentPickingIndex + 1] = strconv.Itoa(asd2 + diff)
                

                for j := 0; j < freeSpacesToReplace; j++ {
                    mapOfMovedDiskFiles[i] = append(mapOfMovedDiskFiles[i], int(math.Ceil(float64(currentPickingIndex/2))))
                }

                break
            }
        }
    }

    thisIndexLol := 0
    sum := 0
    compIndex := 0
    for i, char := range diskMap {
        if i % 2 == 0 {
            num, _ := strconv.Atoi(char)
            for j := 0; j < num; j++ {
                sum += (compIndex * (i / 2))
                compIndex += 1
            }
        } else {
            for _, bruh := range mapOfMovedDiskFiles[thisIndexLol] {
                sum += (compIndex * bruh)
                compIndex += 1
            } 
            thisIndexLol += 1
        }
    }

    fmt.Println("Day 9 Solution (Part 1):", sum)
    fmt.Println("Part 1 execution time:", time.Since(start), "\n")

	start = time.Now()
    fileFreespaceTuple = []test{}
    diskMap = strings.Split(input, "")

    // extra 0 for the last "pair of values" to represent 0 free spaces
    if(len(diskMap) % 2 != 0){
        diskMap = append(diskMap, "0")
    }

    for i := 0; i < len(diskMap); i+=2 {
        fileVal, _ := strconv.Atoi(diskMap[i])
        freespaceVal, _ := strconv.Atoi(diskMap[i + 1])
        fileFreespaceTuple = append(fileFreespaceTuple, test{file: fileVal, freespace: freespaceVal})
    }

    test := []string{}
    intervalOfDots := make(map[int]int)
    for i := 0; i < len(diskMap); i++ {
        char, _ := strconv.Atoi(diskMap[i])
        for j := 0; j < char; j++ {
            if i % 2 == 0 {
                test = append(test, strconv.Itoa(i/2))
            } else {
                test = append(test, ".")
            }
        }
    }

    for i := 0; i < len(test); i++ {
        if test[i] == "."{
            thisIndex := i
            for {
                if test[thisIndex] != "." {
                    intervalOfDots[i] = thisIndex - i
                    break
                }

                thisIndex += 1
            }

            i += (thisIndex - i)
        }
        
    }
    
    currentPickingIndex = 0
    firstEle, _ := strconv.Atoi(test[0])
    for i := len(test) - 1; i > firstEle; i-- {
        if test[i] == "." {
            continue
        }

        first := test[i]
        j := i
        lengthOfShitToMove := 0
        for {
            if test[j] != first {
                break
            }

            j -= 1
            lengthOfShitToMove += 1
        }
        for j, keyOfIntervalOfDots := range slices.Sorted(maps.Keys(intervalOfDots)) {
            interval := intervalOfDots[keyOfIntervalOfDots]
            if j > i - lengthOfShitToMove {
                break
            }
            if interval >= lengthOfShitToMove{
                for topLevel := i; topLevel > i - lengthOfShitToMove; topLevel-- {
                    toMove := test[topLevel]
                    test[topLevel] = "."
                    test[keyOfIntervalOfDots + (i - topLevel)] = toMove
                }

                intervalOfDots[keyOfIntervalOfDots + lengthOfShitToMove] = intervalOfDots[keyOfIntervalOfDots] - lengthOfShitToMove
                intervalOfDots[keyOfIntervalOfDots] = 0
                currentPickingIndex = keyOfIntervalOfDots
                break
            } 
        }

        i -= (lengthOfShitToMove - 1)

        // surely
        if currentPickingIndex > i{
            fmt.Println(currentPickingIndex, i)
            break
        }
    }

    fmt.Println("OUT: ", test)
    sum = 0
    for i, char := range test {
        if char == "." {
            continue
        }

        num, _ := strconv.Atoi(char)
        sum += (i * num)
    }

    //6478232739671 - 
    fmt.Println("Day 9 Solution (Part 2):", sum)
    fmt.Println("Part 2 execution time:", time.Since(start))
}