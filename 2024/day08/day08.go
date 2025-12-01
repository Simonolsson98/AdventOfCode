package main

import (
    "fmt"
    "strings"
    "os"
    "github.com/simonolsson98/adventofcode/utils"
    "path/filepath"
    "time"
)

type position struct {
    xPos int
    yPos int
}

func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

	start := time.Now()
    fmt.Println("Day 8 Solution (Part 1):", part1(input))
    fmt.Println("Part 1 execution time:", time.Since(start))

	start = time.Now()
    fmt.Println("Day 8 Solution (Part 2):", part2(input))
    fmt.Println("Part 2 execution time:", time.Since(start))
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

            existingPositions, otherAntennasExist := antennas[char]
            antennas[char] = append(antennas[char], &position{ xPos: x, yPos: y })
            if !otherAntennasExist { 
                continue
            }

            for _, existingPos := range existingPositions {
                xdiff := existingPos.xPos - x
                ydiff := existingPos.yPos - y

                newXAnti := existingPos.xPos + xdiff
                newYAnti := existingPos.yPos + ydiff
                if newXAnti < xLimit && newXAnti >= 0 && newYAnti < yLimit && newYAnti >= 0 {
                    antiNodes = addifunique(antiNodes, newXAnti, newYAnti)
                }

                newXAnti = x - xdiff
                newYAnti = y - ydiff
                if newXAnti < xLimit && newXAnti >= 0 && newYAnti < yLimit && newYAnti >= 0 {
                    antiNodes = addifunique(antiNodes, newXAnti, newYAnti)
                }
            }
        }
    }

    return len(antiNodes)
}

func part2(input string) (antis int) {
    antiNodes := []position{}
    antennas := make(map[string][]*position)

    for x, line := range strings.Split(input, "\n") {
        xLimit := len(line)
        yLimit := len(strings.Split(line, ""))
        for y, char := range strings.Split(line, "") {
            if char == "." {
                continue
            }

            existingPositions, otherAntennasExist := antennas[char]
            antennas[char] = append(antennas[char], &position{ xPos: x, yPos: y })
            if !otherAntennasExist {
                continue
            }

            for _, existingPos := range existingPositions {
                antiNodes = addifunique(antiNodes, existingPos.xPos, existingPos.yPos)
                antiNodes = addifunique(antiNodes, x, y)

                origxdiff := existingPos.xPos - x
                origydiff := existingPos.yPos - y
                newxDiff := 0; newyDiff := 0
                newXAnti := existingPos.xPos + origxdiff
                newYAnti := existingPos.yPos + origydiff
                for {
                    if newXAnti >= xLimit || newXAnti < 0 || newYAnti >= yLimit || newYAnti < 0 {
                        break
                    }

                    antiNodes = addifunique(antiNodes, newXAnti, newYAnti)
                    
                    newxDiff += origxdiff; newyDiff += origydiff
                    newXAnti = existingPos.xPos + newxDiff
                    newYAnti = existingPos.yPos + newyDiff
                }

                newxDiff = 0; newyDiff = 0
                newXAnti = x - origxdiff
                newYAnti = y - origydiff
                for {
                    if newXAnti >= xLimit || newXAnti < 0 || newYAnti >= yLimit || newYAnti < 0 {
                        break 
                    }

                    antiNodes = addifunique(antiNodes, newXAnti, newYAnti)
                    
                    newxDiff += origxdiff; newyDiff += origydiff
                    newXAnti = x - newxDiff
                    newYAnti = y - newyDiff
                }
            }
        }
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