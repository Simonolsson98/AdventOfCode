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

    defer GuardOutOfSight()
    
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

    visited = append(visited, someStruct { posX: currPosX, posY: currPosY})
    direction := 0 
    for ok := true; ok; ok = true {
        if direction == 0 { // up
            nextEle := grid[currPosX - 1][currPosY]
            if nextEle == "#"{
                direction += 1
            } else{
                currPosX = currPosX - 1
                visited = append(visited, someStruct { posX: currPosX, posY: currPosY})
            }
        } else if direction == 1 { // right
            nextEle := grid[currPosX][currPosY + 1]
            if nextEle == "#"{
                direction += 1
            } else{
                currPosY = currPosY + 1
                visited = append(visited, someStruct { posX: currPosX, posY: currPosY})
            }
        } else if direction == 2 { // down
            nextEle := grid[currPosX + 1][currPosY]
            if nextEle == "#"{
                direction += 1
            } else{
                currPosX = currPosX + 1
                visited = append(visited, someStruct { posX: currPosX, posY: currPosY})
            }
        } else if direction == 3 { // left
            nextEle := grid[currPosX][currPosY - 1]
            if nextEle == "#"{
                direction = 0
            } else{
                currPosY = currPosY - 1
                visited = append(visited, someStruct { posX: currPosX, posY: currPosY})
            }
        }
    }


    fmt.Println("Day 6 Solution (Part 2):")
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