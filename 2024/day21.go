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

type position struct{
    x int
    y int
}

func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

    numerickeypad := [][]string{
        []string{"7","8","9"},
        []string{"4","5","6"},
        []string{"1","2","3"},
        []string{"-1","0","A"}}
    numKeypadMap := make(map[string]position, 0)
    for x, rows := range numerickeypad {
        for y, row := range rows {
            numKeypadMap[row] = position{x, y}
        }
    }
    
    directionalkeypad := [][]string{
        []string{"-1","^","A"},
        []string{"<","v",">"},
    }
    direcKeypadMap := make(map[string]position, 0)
    for x, rows := range directionalkeypad {
        for y, row := range rows {
            direcKeypadMap[row] = position{x, y}
        }
    }

    start := time.Now()
    codes := strings.Split(input, "\n")
    complexity := 0
    for _, code := range codes {
        total := ""
        actualTotal := ""
        currPosNumKeypad := numKeypadMap["A"]
        for _, singleCode := range strings.Split(code, "") {
            nextPos := numKeypadMap[singleCode]

            xdiff := nextPos.x - currPosNumKeypad.x
            ydiff := nextPos.y - currPosNumKeypad.y

            if ydiff < 0 {
                if currPosNumKeypad.x == 3 && currPosNumKeypad.y + ydiff == 0{
                    // would end up in gap
                    total += strings.Repeat("^", (xdiff * -1))
                    total += strings.Repeat("<", (ydiff * -1))

                    currPosNumKeypad = nextPos
                    total += "A"
                    continue
                } else {
                    total += strings.Repeat("<", (ydiff * -1))
                }
            }

            if xdiff < 0 {
                total += strings.Repeat("^",  (xdiff * -1))
            }

            if xdiff > 0{
                if currPosNumKeypad.y == 0 && currPosNumKeypad.x + xdiff == 3{
                    // would end up in gap
                    total += strings.Repeat(">", (ydiff))
                    total += strings.Repeat("v", (xdiff))
                    
                    currPosNumKeypad = nextPos
                    total += "A"
                    continue
                } else {
                    total += strings.Repeat("v", (xdiff))
                }
            }

            if ydiff > 0{
                total += strings.Repeat(">",  (ydiff))
            }

            total += "A"
            currPosNumKeypad = nextPos
        }

        for i := 0; i < 2; i++ {
            currPosDirecKeypad := direcKeypadMap["A"]
            for _, direcMove := range strings.Split(total, "") {
                nextPos := direcKeypadMap[direcMove]

                xdiff := nextPos.x - currPosDirecKeypad.x
                ydiff := nextPos.y - currPosDirecKeypad.y
                
                fmt.Println(xdiff, ydiff)
                if ydiff < 0 {
                    if currPosDirecKeypad.x == 0 && currPosDirecKeypad.y + ydiff == 0{
                        // would end up in gap
                        actualTotal += "v"
                        actualTotal += strings.Repeat("<", (ydiff * -1))
                        
                        actualTotal += "A"
                        currPosDirecKeypad = nextPos
                        continue
                    } else {
                        actualTotal += strings.Repeat("<", (ydiff * -1))
                    }
                } 

                if xdiff > 0{
                    actualTotal += strings.Repeat("v", (xdiff))
                }

                if xdiff < 0 {
                    if currPosDirecKeypad.y == 0 && currPosDirecKeypad.x + xdiff == 0{
                        // would end up in gap
                        actualTotal += strings.Repeat(">", ydiff)
                        actualTotal += "^"

                        actualTotal += "A"
                        currPosDirecKeypad = nextPos
                        continue
                    } else {
                        actualTotal += strings.Repeat("^", (xdiff * -1))
                    }
                }

                if ydiff > 0{
                    actualTotal += strings.Repeat(">", (ydiff))
                }

                actualTotal += "A"
                currPosDirecKeypad = nextPos

            }

            total = actualTotal
            actualTotal = ""
        }

        val, _ := strconv.Atoi(strings.TrimRight(code, "A"))
        fmt.Println(total, len(total), val)
        complexity += (len(total) * val)
    }

    fmt.Println("Day 21 Solution (Part 1):", complexity)
    fmt.Println("Part 1 execution time:", time.Since(start), "\n")

    start = time.Now()
    // exec part 2
    fmt.Println("Day 21 Solution (Part 2):")
    fmt.Println("Part 2 execution time:", time.Since(start))
}