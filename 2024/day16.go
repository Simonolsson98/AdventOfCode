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

type position struct {
    x int
    y int
}
 
var (
    valueOfDestination int;
    grid [][]string
    currPos position
    visited map[position]int
)

func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

    rows := strings.Split(input, "\n")
    for x, row := range rows {
        for y, char := range row {
            if char == 'S' {
                currPos = position{x, y}
            }

        }
        grid = append(grid, strings.Split(row, ""))
    }

    visited = make(map[position]int)
    for x := 0; x < len(grid); x++ {
        for y := 0; y < len(grid[x]); y++ {
            pos := position{x, y}
            visited[pos] = 99999999999
        }
    }

    BFS(0, "e")


	start := time.Now()
	// 147584 too high
    fmt.Println("Day 16 Solution (Part 1):", valueOfDestination)
    fmt.Println("Part 1 execution time:", time.Since(start), "\n")

	start = time.Now()
	// exec part2()
    fmt.Println("Day 16 Solution (Part 2):")
    fmt.Println("Part 2 execution time:", time.Since(start))
}

func BFS(count int, dir string){
    if grid[currPos.x][currPos.y] == "E" {

        fmt.Println("HERE WITH:", count)
        if count < visited[position{currPos.x, currPos.y}] {
            visited[position{currPos.x, currPos.y}] = count
            valueOfDestination = count
        }
        return
    }
    
    if visited[position{currPos.x, currPos.y}] < count{
        return
    }

    visited[position{currPos.x, currPos.y}] = count
    neighbours := []position{position{currPos.x-1, currPos.y}, position{currPos.x, currPos.y+1}, position{currPos.x+1, currPos.y}, position{currPos.x, currPos.y-1}}
    for _, neighbour := range neighbours {
        if grid[neighbour.x][neighbour.y] == "#"{
            continue
        }
        
        tempCount := count
        var nextDir string
        switch dir {
            case "e":
                if neighbour.x == currPos.x - 1{ //neighbour north
                    nextDir = "n"
                    tempCount += 1001
                } else if neighbour.y == currPos.y + 1{ //neighbour east
                    nextDir = "e"
                    tempCount += 1
                } else if neighbour.y == currPos.y - 1{ //neighbour west
                    continue
                } else { //neighbour south
                    nextDir = "s"
                    tempCount += 1001
                }
            case "s":
                if neighbour.x == currPos.x - 1{ //neighbour north
                    continue
                } else if neighbour.y == currPos.y + 1{ //neighbour east
                    nextDir = "e"
                    tempCount += 1001
                } else if neighbour.y == currPos.y - 1{ //neighbour west
                    nextDir = "w"
                    tempCount += 1001
                } else { //neighbour south
                    nextDir = "s"
                    tempCount += 1
                }
            case "w":
                if neighbour.x == currPos.x - 1{ //neighbour north
                    nextDir = "n"
                    tempCount += 1001
                } else if neighbour.y == currPos.y + 1{ //neighbour east
                    continue
                } else if neighbour.y == currPos.y - 1{ //neighbour west
                    nextDir = "w"
                    tempCount += 1
                } else { //neighbour south
                    nextDir = "s"
                    tempCount += 1001
                }
            case "n":
                if neighbour.x == currPos.x - 1{ //neighbour north
                    nextDir = "n"
                    tempCount += 1
                } else if neighbour.y == currPos.y + 1{ //neighbour east
                    nextDir = "e"
                    tempCount += 1001
                } else if neighbour.y == currPos.y - 1{ //neighbour west
                    nextDir = "w"
                    tempCount += 1001
                } else { //neighbour south
                    continue
                }
        }

        currPos = neighbour
        BFS(tempCount, nextDir)
    }
}