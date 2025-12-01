package main

import (
    "fmt"
    "strings"
    "os"
    "github.com/simonolsson98/adventofcode/utils"
    "strconv"
    "path/filepath"
    "time"
)

type someStruct struct  {
    posX int
    posY int
    dir int
}
func (s someStruct) key() string {
    return strconv.Itoa(s.posX) + "," + strconv.Itoa(s.posY)
}
func (s someStruct) key2() string {
    return strconv.Itoa(s.posX) + "," + strconv.Itoa(s.posY) + "," + strconv.Itoa(s.dir)
}

var visited []someStruct
var uniqueMap map[string]bool = make(map[string]bool)
var uniqueVisited []someStruct
var grid [][]string

var startingPosX int
var startingPosY int

var start time.Time
func main() {
    start = time.Now()
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

    var currPosX int
    var currPosY int
    for x, line := range strings.Split(input, "\n") {
        col := strings.Split(line, "")
        for y, char := range col {
            // get starting pos of guard
            if char == "^" {
                currPosX = x
                currPosY = y

                startingPosX = currPosX
                startingPosY = currPosY
            }
        }

        grid = append(grid, col)
    }

    part1(grid, currPosX, currPosY)
}

func part1(grid [][]string, startX, startY int) {
    defer GuardOutOfSight()
    currPosX, currPosY := startX, startY
    direction := 0

    // Add the starting position
    visited = append(visited, someStruct{posX: currPosX, posY: currPosY})

    for ok := true; ok; {
        var nextEle string
        switch direction {
        case 0: // Up
            nextEle = grid[currPosX-1][currPosY]
            if nextEle == "#" {
                direction = (direction + 1) % 4
            } else {
                currPosX--
                visited = append(visited, someStruct{posX: currPosX, posY: currPosY})
            }
        case 1: // Right
            nextEle = grid[currPosX][currPosY+1]
            if nextEle == "#" {
                direction = (direction + 1) % 4
            } else {
                currPosY++
                visited = append(visited, someStruct{posX: currPosX, posY: currPosY})
            }
        case 2: // Down
            nextEle = grid[currPosX+1][currPosY]
            if nextEle == "#" {
                direction = (direction + 1) % 4
            } else {
                currPosX++
                visited = append(visited, someStruct{posX: currPosX, posY: currPosY})
            }
        case 3: // Left
            nextEle = grid[currPosX][currPosY-1]
            if nextEle == "#" {
                direction = (direction + 1) % 4
            } else {
                currPosY--
                visited = append(visited, someStruct{posX: currPosX, posY: currPosY})
            }
        }
    }
}

func GuardOutOfSight(){
    if r := recover(); r != nil {
        for _, pos := range visited {
            if !uniqueMap[pos.key()] {
                uniqueVisited = append(uniqueVisited, pos)
                uniqueMap[pos.key()] = true
            }
        }

        fmt.Println("Day 6 Solution (Part 1):", len(uniqueVisited))
        fmt.Println("Part 1 execution time:", time.Since(start))
    }

    var differentPositions int
    for _, pos := range uniqueVisited {
        x := pos.posX
        y := pos.posY
        uniqueMap = make(map[string]bool)
        if grid[x][y] == "." {
            grid[x][y] = "#"
        } else{
            continue
        }

        hmm := part2(grid)
        if hmm {
            differentPositions += 1
        }

        grid[x][y] = "."
    }

    fmt.Println("Day 6 Solution (Part 2):", differentPositions)
    fmt.Println("Part 2 execution time:", time.Since(start))
}

func part2(grid [][]string) (loop bool) {
    currPosX, currPosY := startingPosX, startingPosY
    direction := 0

    // Add the starting position
    visited = append(visited, someStruct{posX: currPosX, posY: currPosY, dir: direction})

    for ok := true; ok; {
        var nextEle string
        switch direction {
        case 0: // Up
            if currPosX - 1 < 0 {
                return false
            }
            nextEle = grid[currPosX-1][currPosY]
            if nextEle == "#" {
                direction = (direction + 1) % 4
            } else {
                currPosX--
                pos := someStruct{posX: currPosX, posY: currPosY, dir: direction}
                if !uniqueMap[pos.key2()] {
                    uniqueVisited = append(uniqueVisited, pos)
                    uniqueMap[pos.key2()] = true
                } else {
                    return true
                }
            }
        case 1: // Right
            if currPosY + 1 > len(grid[0]) - 1 {
                return false
            }
            nextEle = grid[currPosX][currPosY+1]
            if nextEle == "#" {
                direction = (direction + 1) % 4
            } else {
                currPosY++
                pos := someStruct{posX: currPosX, posY: currPosY, dir: direction}
                if !uniqueMap[pos.key2()] {
                    uniqueVisited = append(uniqueVisited, pos)
                    uniqueMap[pos.key2()] = true
                } else {
                    return true
                }
            }
        case 2: // Down
            if currPosX + 1 > len(grid) - 1 {
                return false
            }
            nextEle = grid[currPosX+1][currPosY]
            if nextEle == "#" {
                direction = (direction + 1) % 4
            } else {
                currPosX++
                pos := someStruct{posX: currPosX, posY: currPosY, dir: direction}
                if !uniqueMap[pos.key2()] {
                    uniqueVisited = append(uniqueVisited, pos)
                    uniqueMap[pos.key2()] = true
                } else {
                    return true
                }
            }
        case 3: // Left
            if currPosY - 1 < 0 {
                return false
            }
            nextEle = grid[currPosX][currPosY-1]
            if nextEle == "#" {
                direction = (direction + 1) % 4
            } else {
                currPosY--
                pos := someStruct{posX: currPosX, posY: currPosY, dir: direction}
                if !uniqueMap[pos.key2()] {
                    uniqueVisited = append(uniqueVisited, pos)
                    uniqueMap[pos.key2()] = true
                } else {
                    return true
                }
            }
        }
    }

    // wont reach
    return false
}
