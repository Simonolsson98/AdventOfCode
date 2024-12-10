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

type fileAndFreespaceStruct struct {
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
    var fileFreespaceTuple = []fileAndFreespaceStruct{}
    diskMap := strings.Split(input, "")

    // extra 0 for the last "pair of values" to represent 0 free spaces
    if(len(diskMap) % 2 != 0){
        diskMap = append(diskMap, "0")
    }

    for i := 0; i < len(diskMap); i+=2 {
        fileVal, _ := strconv.Atoi(diskMap[i])
        freespaceVal, _ := strconv.Atoi(diskMap[i + 1])
        fileFreespaceTuple = append(fileFreespaceTuple, fileAndFreespaceStruct{file: fileVal, freespace: freespaceVal})
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
    fileFreespaceTuple = []fileAndFreespaceStruct{}
    diskMap = strings.Split(input, "")

    // extra 0 for the last "pair of values" to represent 0 free spaces
    if(len(diskMap) % 2 != 0){
        diskMap = append(diskMap, "0")
    }

    for i := 0; i < len(diskMap); i+=2 {
        fileVal, _ := strconv.Atoi(diskMap[i])
        freespaceVal, _ := strconv.Atoi(diskMap[i + 1])
        fileFreespaceTuple = append(fileFreespaceTuple, fileAndFreespaceStruct{file: fileVal, freespace: freespaceVal})
    }

    fileAndFreespaceStruct := []string{}
    intervalOfDots := make(map[int]int)
    for i := 0; i < len(diskMap); i++ {
        char, _ := strconv.Atoi(diskMap[i])
        for j := 0; j < char; j++ {
            if i % 2 == 0 {
                fileAndFreespaceStruct = append(fileAndFreespaceStruct, strconv.Itoa(i/2))
            } else {
                fileAndFreespaceStruct = append(fileAndFreespaceStruct, ".")
            }
        }
    }

    for i := 0; i < len(fileAndFreespaceStruct); i++ {
        if fileAndFreespaceStruct[i] == "."{
            thisIndex := i
            for {
                if fileAndFreespaceStruct[thisIndex] != "." {
                    intervalOfDots[i] = thisIndex - i
                    break
                }

                thisIndex += 1
                if thisIndex >= len(fileAndFreespaceStruct) {
                    intervalOfDots[i] = thisIndex - i
                    break
                }
            }

            i += (thisIndex - i)
        }
    }

    lockedIndices := []int{}
    currentPickingIndex = 0
    for i := len(fileAndFreespaceStruct) - 1; i > 0; i-- {
        if fileAndFreespaceStruct[i] == "." || slices.Contains(lockedIndices, i) || fileAndFreespaceStruct[i] == "0" {
            continue
        }

        firstEleInFile := fileAndFreespaceStruct[i]
        j := i
        lengthOfShitToMove := 0
        for {
            // hit a dot means the block that should be moved is "complete"
            if fileAndFreespaceStruct[j] != firstEleInFile {
                break
            }

            j -= 1
            lengthOfShitToMove += 1
        }

        for _, keyOfIntervalOfDots := range slices.Sorted(maps.Keys(intervalOfDots)) {
            interval := intervalOfDots[keyOfIntervalOfDots]
            if keyOfIntervalOfDots > i {
                break
            }
            if interval >= lengthOfShitToMove{
                for topLevel := i; topLevel > i - lengthOfShitToMove; topLevel-- {
                    lockedIndices = append(lockedIndices, keyOfIntervalOfDots + (i - topLevel))
                    lockedIndices = append(lockedIndices, topLevel)
                    toMove := fileAndFreespaceStruct[topLevel]
                    fileAndFreespaceStruct[topLevel] = "."
                    fileAndFreespaceStruct[keyOfIntervalOfDots + (i - topLevel)] = toMove
                }

                if intervalOfDots[keyOfIntervalOfDots] - lengthOfShitToMove == 0{
                    delete(intervalOfDots, keyOfIntervalOfDots + lengthOfShitToMove)
                } else {
                    intervalOfDots[keyOfIntervalOfDots + lengthOfShitToMove] = intervalOfDots[keyOfIntervalOfDots] - lengthOfShitToMove
                }

                delete(intervalOfDots, keyOfIntervalOfDots)
                intervalOfDots[j + 1] = lengthOfShitToMove
                for _, key := range slices.Sorted(maps.Keys(intervalOfDots)) {
                    _, exists := intervalOfDots[key + intervalOfDots[key]]
                    if exists {
                        removeThisIndex := key + intervalOfDots[key]
                        intervalOfDots[key] = intervalOfDots[key] + intervalOfDots[key + intervalOfDots[key]]
                        delete(intervalOfDots, removeThisIndex)
                    }
                }

                break
            } 
        }

        i -= (lengthOfShitToMove - 1)
    }

    sum = 0
    for i, char := range fileAndFreespaceStruct {
        if char == "." {
            continue
        }

        num, _ := strconv.Atoi(char)
        sum += (i * num)
    }

    fmt.Println("Day 9 Solution (Part 2):", sum)
    fmt.Println("Part 2 execution time:", time.Since(start))
}
