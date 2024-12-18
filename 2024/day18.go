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

type position struct {
    x int
    y int
}

var (
    valueOfDestination int
    grid [][]string
    currPos position
    visited map[position]int
    xlength = 71
    ylength = 71
)

func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

    grid = make([][]string, xlength)
    for i := range grid {
        grid[i] = make([]string, ylength)
    }

    for i := 0; i < xlength; i++ {
        for j := 0; j < ylength; j++ {
            grid[i][j] = "."
        }
    }

    grid[0][0] = "S"
    grid[xlength - 1][ylength - 1] = "E"
    currPos = position{0, 0}

    rows := strings.Split(input, "\n")
    for i := 0; i < 1024; i++ {
        coords := strings.Split(rows[i], ",")
        ypos, _ := strconv.Atoi(coords[0])
        xpos, _ := strconv.Atoi(coords[1])
        grid[xpos][ypos] = "#"
    }

    visited = make(map[position]int)
    for x := 0; x < len(grid); x++ {
        for y := 0; y < len(grid[x]); y++ {
            visited[position{x, y}] = 1000
        }
    }

    start := time.Now()
    DFS(0, currPos)
    fmt.Println("Day 16 Solution (Part 1):", valueOfDestination)
    fmt.Println("Part 1 execution time:", time.Since(start), "\n")

    valueOfDestination = -1
    grid[0][0] = "S"
    grid[xlength - 1][ylength - 1] = "E"
    currPos = position{0, 0}

    visited = make(map[position]int)
    for x := 0; x < len(grid); x++ {
        for y := 0; y < len(grid[x]); y++ {
            visited[position{x, y}] = 100000
        }
    }
        
    var mazeBlocker []string
    rows = strings.Split(input, "\n")
    for i := 1024; i < len(rows); i++ {
        coords := strings.Split(rows[i], ",")
        ypos, _ := strconv.Atoi(coords[0])
        xpos, _ := strconv.Atoi(coords[1])
        grid[xpos][ypos] = "#"


        DFS(0, currPos)
        if visited[position{xlength - 1, ylength - 1}] == 100000{
            mazeBlocker = coords
            break
        }

        for x := 0; x < len(grid); x++ {
            for y := 0; y < len(grid[x]); y++ {
                visited[position{x, y}] = 100000
            }
        }
    }

    res := mazeBlocker[0]+","+mazeBlocker[1]
    fmt.Println("Day 16 Solution (Part 2):", res)
    fmt.Println("Part 2 execution time:", time.Since(start))
}

func DFS(count int, currPos position){
    if grid[currPos.x][currPos.y] == "E" {
        if count < visited[position{currPos.x, currPos.y}] {
            visited[position{currPos.x, currPos.y}] = count
            valueOfDestination = count
        }

        return
    }
    
    if visited[position{currPos.x, currPos.y}] <= count{
        return
    }

    visited[position{currPos.x, currPos.y}] = count
    neighbours := []position{
        position{currPos.x-1, currPos.y}, 
        position{currPos.x, currPos.y+1}, 
        position{currPos.x+1, currPos.y}, 
        position{currPos.x, currPos.y-1}}

    for _, neighbour := range neighbours {
        if  neighbour.x > xlength - 1 ||
            neighbour.x < 0 ||
            neighbour.y > ylength - 1 ||
            neighbour.y < 0 ||
            grid[neighbour.x][neighbour.y] == "#"{
            continue
        }
        
        DFS(count + 1, neighbour)
    }
}