package main

import (
    "fmt"
    "strings"
    "os"
    "2024/utils"
    "strconv"
    "path/filepath"
    "time"
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
    currentCharIsNotZero := false
    for i, char := range diskMap {
        if char != "0" {
            if currentCharIsNotZero {
                break
            } else {
                currentCharIsNotZero = true
            }
            num, _ := strconv.Atoi(char)
            for j := 0; j < num; j++ {
                // fmt.Println("MUL:", compIndex, (i / 2), "=", compIndex * (i / 2))
                sum += (compIndex * (i / 2))
                compIndex += 1
            }
        } else {
            currentCharIsNotZero = false
            for _, bruh := range mapOfMovedDiskFiles[thisIndexLol] {
                // fmt.Println("MUL:", compIndex, bruh, "=", compIndex * bruh)
                sum += (compIndex * bruh)

                compIndex += 1
            } 
            thisIndexLol += 1
        }
    }

    fmt.Println("Day 9 Solution (Part 1):", sum)
    fmt.Println("Part 1 execution time:", time.Since(start), "\n")

	start = time.Now()
	// exec part2()
    fmt.Println("Day 9 Solution (Part 2):")
    fmt.Println("Part 2 execution time:", time.Since(start))
}
