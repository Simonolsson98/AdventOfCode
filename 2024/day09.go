package main

import (
    "fmt"
    "strings"
    "os"
    "2024/utils"
    "strconv"
    "path/filepath"
    "time"
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

    var currentPickingIndex int
    var lol = []test{}
    splitted := strings.Split(input, "")
    for i := 0; i < len(splitted); i+=2 {
        if i + 1 >= len(splitted){
            break
        }
        fileVal, _ := strconv.Atoi(splitted[i])
        freespaceVal, _ := strconv.Atoi(splitted[i + 1])

        lol = append(lol, test{file: fileVal, freespace: freespaceVal, index: i})
        currentPickingIndex = i
    }

    fmt.Println(lol)
    return
    for i, val := range lol {
        freeSpacesToReplace := val.freespace
        fmt.Println("running for:", freeSpacesToReplace, "in: ", val)
        for {
            if currentPickingIndex < 0 {
                break
            }

            piecesToBeMoved, _ := strconv.Atoi(splitted[currentPickingIndex]) // 4 out of 4 0 16
            fmt.Println("piecesToBeMoved: ", piecesToBeMoved)
            if piecesToBeMoved == 0 {
                currentPickingIndex -= 2
                continue
            }
            
            if freeSpacesToReplace > piecesToBeMoved{
                fmt.Println("freeSpacesToReplace > piecesToBeMoved", freeSpacesToReplace, piecesToBeMoved)
                freeSpacesToReplace -= piecesToBeMoved
                piecesToBeMoved = 0
                fmt.Println(splitted)
                splitted[currentPickingIndex - 1] = "0"
                fmt.Println(splitted)
                val.freespace = freeSpacesToReplace
                currentPickingIndex -= 2
                lol[i] = val
                continue
            } else { // more than enough to move
                fmt.Println("freeSpacesToReplace <= piecesToBeMoved", freeSpacesToReplace, piecesToBeMoved)
                piecesToBeMoved -= freeSpacesToReplace
                val.freespace = 0
                valOfMovedStuff := currentPickingIndex/2
                val.index = valOfMovedStuff
                fmt.Println("valOfMovedStuff:", valOfMovedStuff)
                fmt.Println("currpick:", currentPickingIndex)
                lol[i] = val
                break
            }

            check, _ := strconv.Atoi(splitted[currentPickingIndex])
            if check <= 0 {
                currentPickingIndex -= 2
            }
            if freeSpacesToReplace <= 0 {
                break
            }
        }
    }

    sum := 0
    for i := 0; i < len(lol); i++ {
        if i + 1 >= len(lol){
            break
        }

        sum += (i * lol[i].file + (i + 1) * (lol[i].index * (lol[i+1].file - lol[i].file)))
    }

    fmt.Println(lol)
	start := time.Now()
	// exec part1()
    fmt.Println("Day 9 Solution (Part 1):", sum)
    fmt.Println("Part 1 execution time:", time.Since(start), "\n")

	start = time.Now()
	// exec part2()
    fmt.Println("Day 9 Solution (Part 2):")
    fmt.Println("Part 2 execution time:", time.Since(start))
}
