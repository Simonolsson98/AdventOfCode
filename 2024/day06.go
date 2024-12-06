package main

import (
    "fmt"
    "strings"
    "os"
    "2024/utils"
    "strconv"
    "path/filepath"
)

type someStruct struct  {
    posX int
    posY int
}
func (s someStruct) key() string {
    return strconv.Itoa(s.posX) + "," + strconv.Itoa(s.posY)
}

var visited []someStruct
var uniqueMap map[string]bool = make(map[string]bool)

func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

    
    var grid [][]string
    var currPosX int
    var currPosY int
    for x, line := range strings.Split(input, "\n") {
        col := strings.Split(line, "")
        for y, char := range col {
            // get starting pos of guard
            if char == "^" {
                currPosX = x
                currPosY = y
            }
        }

        grid = append(grid, col)
    }


    part1(grid, currPosX, currPosY)

    fmt.Println("Day 6 Solution (Part 2):")
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
        uniqueVisited := []someStruct {}
        for _, pos := range visited {
            if !uniqueMap[pos.key()] {
                uniqueVisited = append(uniqueVisited, pos)
                uniqueMap[pos.key()] = true
            }
        }

        fmt.Println("Day 6 Solution (Part 1):", len(uniqueVisited))
    }
}