package main

import (
    "fmt"
    "strings"
    "os"
    "2024/utils"
    //"strconv"
    "path/filepath"
    "time"
)

func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

	start := time.Now()
    fmt.Println("Day 8 Solution (Part 1):", part1(input))
    fmt.Println("Part 1 execution time:", time.Since(start), "\n")

	start = time.Now()
	// exec part2()
    fmt.Println("Day 8 Solution (Part 2):")
    fmt.Println("Part 2 execution time:", time.Since(start))
}

type position struct {
    xPos int
    yPos int
}

func part1(input string) (antis int) {
    antiNodes := []position{}
    antennas := make(map[string][]*position)

    for x, line := range strings.Split(input, "\n") {
        xLimit := len(line)
        yLimit := len(strings.Split(line, ""))
        for y, char := range strings.Split(line, "") {
            if char == "." {
                continue
            }

            existingPositions, exists := antennas[char]
            if exists {
                for _, existingPos := range existingPositions {
                    xdiff := existingPos.xPos - x
                    ydiff := existingPos.yPos - y

                    newXAnti := existingPos.xPos + xdiff
                    newYAnti := existingPos.yPos + ydiff

                    if  newXAnti < xLimit && 
                        newXAnti >= 0 && 
                        newYAnti < yLimit && 
                        newYAnti >= 0 {
                        antiNodes = addifunique(antiNodes, existingPos.xPos + xdiff, existingPos.yPos + ydiff)
                    }

                    newXAnti = x - xdiff
                    newYAnti = y - ydiff
                    if  newXAnti < xLimit && 
                        newXAnti >= 0 && 
                        newYAnti < yLimit && 
                        newYAnti >= 0 {

                        antiNodes = addifunique(antiNodes, x - xdiff, y - ydiff)
                    }

                }
            } else {
                fmt.Println("new pos: ", x, y)
            }

            antennas[char] = append(antennas[char], &position{ xPos: x, yPos: y })
        }
    }

    for _, node := range antiNodes {
        fmt.Println(node.xPos, node.yPos)
    }
    return len(antiNodes)
}

func addifunique(antiNodes []position, newXPos int, newYPos int) ([]position){
    exists := false
    for _, p := range antiNodes {
        if p.xPos == newXPos && p.yPos == newYPos  {
            exists = true
            break
        }
    }

    if !exists {
        antiNodes = append(antiNodes, position{ xPos: newXPos, yPos: newYPos })
    }

    return antiNodes
}

