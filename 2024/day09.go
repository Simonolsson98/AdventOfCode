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
    index int
}

func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

    start := time.Now()
    var currentPickingIndex int
    var lol = []test{}
    splitted := strings.Split(input, "")
    if(len(splitted) % 2 != 0){
        splitted = append(splitted, "0")
    }
    for i := 0; i < len(splitted); i+=2 {
        if i + 1 >= len(splitted){
            break
        }
        fileVal, _ := strconv.Atoi(splitted[i])
        freespaceVal, _ := strconv.Atoi(splitted[i + 1])

        lol = append(lol, test{file: fileVal, freespace: freespaceVal, index: i})
        currentPickingIndex = i
    }

    testMap := make(map[int][]int)

    for i, val := range lol {
        if i == len(lol) {
            break
        }

        freeSpacesToReplace := val.freespace
        for {
            if currentPickingIndex < 0 || currentPickingIndex <= 2 * i {
                break
            }

            piecesToBeMoved, _ := strconv.Atoi(splitted[currentPickingIndex])
            if piecesToBeMoved == 0 {
                currentPickingIndex -= 2
                continue
            }
            
            if freeSpacesToReplace > piecesToBeMoved{
                diff := freeSpacesToReplace - piecesToBeMoved

                splitted[2*i+1] = strconv.Itoa(diff)
                splitted[currentPickingIndex] = "0"

                self, _ := strconv.Atoi(splitted[currentPickingIndex+1])
                splitted[currentPickingIndex+1] = strconv.Itoa(self + piecesToBeMoved)
                
                for j := 0; j < piecesToBeMoved; j++ {
                    testMap[i] = append(testMap[i], int(math.Ceil(float64(currentPickingIndex/2))))
                }

                freeSpacesToReplace = diff
                continue
            } else if freeSpacesToReplace == piecesToBeMoved {
                splitted[2*i+1] = "0"

                splitted[currentPickingIndex] = "0"

                asd2, _ := strconv.Atoi(splitted[currentPickingIndex + 1])
                splitted[currentPickingIndex + 1] = strconv.Itoa(asd2 + piecesToBeMoved)
                
                for j := 0; j < piecesToBeMoved; j++ {
                    testMap[i] = append(testMap[i], int(math.Ceil(float64(currentPickingIndex/2))))
                }
                
                break
            } else { // more than enough to move
                diff := piecesToBeMoved - freeSpacesToReplace
                splitted[2*i+1] = "0"

                splitted[currentPickingIndex] = strconv.Itoa(diff)

                asd2, _ := strconv.Atoi(splitted[currentPickingIndex + 1])
                splitted[currentPickingIndex + 1] = strconv.Itoa(asd2 + diff)
                

                for j := 0; j < freeSpacesToReplace; j++ {
                    testMap[i] = append(testMap[i], int(math.Ceil(float64(currentPickingIndex/2))))
                }

                break
            }
        }
    }

    thisIndexLol := 0
    sum := 0
    compIndex := 0
    currentCharIsNotZero := false
    for i, char := range splitted {
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
            for _, bruh := range testMap[thisIndexLol] {
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
