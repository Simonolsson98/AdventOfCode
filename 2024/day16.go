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
    dir string
}

var (
    valueOfDestination int
    tilesInBestPath []position
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
                currPos = position{x, y, "e"}
            }

        }
        grid = append(grid, strings.Split(row, ""))
    }

    visited = make(map[position]int)
    for x := 0; x < len(grid); x++ {
        for y := 0; y < len(grid[x]); y++ {
            visited[position{x, y, "e"}] = 99999999999
            visited[position{x, y, "s"}] = 99999999999
            visited[position{x, y, "w"}] = 99999999999
            visited[position{x, y, "n"}] = 99999999999
        }
    }

    start := time.Now()
    BFS(0, currPos, []position{currPos}, 1)
    fmt.Println("Day 16 Solution (Part 1):", valueOfDestination)
    fmt.Println("Part 1 execution time:", time.Since(start), "\n")

    start = time.Now()
    for x := 0; x < len(grid); x++ {
        for y := 0; y < len(grid[x]); y++ {
            visited[position{x, y, "e"}] = 99999999999
            visited[position{x, y, "s"}] = 99999999999
            visited[position{x, y, "w"}] = 99999999999
            visited[position{x, y, "n"}] = 99999999999
        }
    }

    BFS(0, currPos, []position{currPos}, 2)

    unique := map[position]bool{}
    for _, v := range tilesInBestPath {
        unique[v] = true
    }

    fmt.Println("Day 16 Solution (Part 2):", len(unique))
    fmt.Println("Part 2 execution time:", time.Since(start))
}

func BFS(count int, currPos position, partOfPath []position, part int){
    if grid[currPos.x][currPos.y] == "E" {
        if part == 1{
            if count < visited[position{currPos.x, currPos.y, currPos.dir}] {
                visited[position{currPos.x, currPos.y, currPos.dir}] = count
                valueOfDestination = count
            }
        } else {
            if count == valueOfDestination{
                tilesInBestPath = append(tilesInBestPath, partOfPath...)
            }
        }

        return
    }
    
    if part == 1{
        if visited[position{currPos.x, currPos.y, currPos.dir}] <= count{
            return
        }
    } else {
        if visited[position{currPos.x, currPos.y, currPos.dir}] < count{
            return
        }
    }

    partOfPath = append(partOfPath, position{currPos.x, currPos.y, "x"})

    visited[position{currPos.x, currPos.y, currPos.dir}] = count
    neighbours := []position{
        position{currPos.x-1, currPos.y, "n"}, 
        position{currPos.x, currPos.y+1, "e"}, 
        position{currPos.x+1, currPos.y, "s"}, 
        position{currPos.x, currPos.y-1, "w"}}
    for _, neighbour := range neighbours {
        if grid[neighbour.x][neighbour.y] == "#"{
            continue
        }
        
        tempCount := count
        switch currPos.dir {
            case "e":
                if neighbour.x == currPos.x - 1{ //neighbour north
                    tempCount += 1001
                } else if neighbour.y == currPos.y + 1{ //neighbour east
                    tempCount += 1
                } else if neighbour.y == currPos.y - 1{ //neighbour west
                    continue
                } else { //neighbour south
                    tempCount += 1001
                }
            case "s":
                if neighbour.x == currPos.x - 1{ //neighbour north
                    continue
                } else if neighbour.y == currPos.y + 1{ //neighbour east
                    tempCount += 1001
                } else if neighbour.y == currPos.y - 1{ //neighbour west
                    tempCount += 1001
                } else { //neighbour south
                    tempCount += 1
                }
            case "w":
                if neighbour.x == currPos.x - 1{ //neighbour north
                    tempCount += 1001
                } else if neighbour.y == currPos.y + 1{ //neighbour east
                    continue
                } else if neighbour.y == currPos.y - 1{ //neighbour west
                    tempCount += 1
                } else { //neighbour south
                    tempCount += 1001
                }
            case "n":
                if neighbour.x == currPos.x - 1{ //neighbour north
                    tempCount += 1
                } else if neighbour.y == currPos.y + 1{ //neighbour east
                    tempCount += 1001
                } else if neighbour.y == currPos.y - 1{ //neighbour west
                    tempCount += 1001
                } else { //neighbour south
                    continue
                }
            default:
                panic("lol")
        }

        BFS(tempCount, neighbour, partOfPath, part)
    }
}