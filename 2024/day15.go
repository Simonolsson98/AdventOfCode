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

func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

    start := time.Now()
    var startingPos position
    warehouseAndMoves := strings.Split(input, "\n\n")
    warehouse := warehouseAndMoves[0]
    moves := warehouseAndMoves[1]
    
    var warehouse2dArr [][]string
    for x, line := range strings.Split(warehouse, "\n") {
        splitLine := strings.Split(line, "")
        for y, char := range splitLine {
            if char == "@" {
                startingPos = position{x, y}
            }
        }
        warehouse2dArr = append(warehouse2dArr, strings.Split(line, ""))
    }

    xlen := len(warehouse2dArr)
    ylen := len(warehouse2dArr[0])
    for _, move := range strings.Split(moves, "\n") {
        for _, individualMove := range strings.Split(move, "") {
            if individualMove == "^" {
                validity := false
                numberOfBoxesToMove := 0
                for i := startingPos.x-1; i > 0; i-- {
                    if warehouse2dArr[i][startingPos.y] == "."{
                        validity = true
                        break
                    } else if warehouse2dArr[i][startingPos.y] == "#"{
                        break
                    }
                    numberOfBoxesToMove++
                }

                if validity {
                    for i := numberOfBoxesToMove; i > 0; i-- {
                        newIndex := startingPos.x - (i + 1)
                        warehouse2dArr[newIndex][startingPos.y] = warehouse2dArr[newIndex + 1][startingPos.y]
                    }

                    warehouse2dArr[startingPos.x][startingPos.y] = "."
                    startingPos = position{startingPos.x - 1, startingPos.y}
                    warehouse2dArr[startingPos.x][startingPos.y] = "@"
                }
            } else if individualMove == ">" {
                validity := false
                numberOfBoxesToMove := 0
                for i := startingPos.y+1; i < ylen-1; i++ {
                    if warehouse2dArr[startingPos.x][i] == "."{
                        validity = true
                        break
                    } else if warehouse2dArr[startingPos.x][i] == "#"{
                        break
                    }
                    numberOfBoxesToMove++
                }

                if validity {
                    for i := numberOfBoxesToMove; i > 0; i-- {
                        newIndex := startingPos.y + i + 1
                        warehouse2dArr[startingPos.x][newIndex] = warehouse2dArr[startingPos.x][newIndex - 1]
                    }

                    warehouse2dArr[startingPos.x][startingPos.y] = "."
                    startingPos = position{startingPos.x, startingPos.y + 1}
                    warehouse2dArr[startingPos.x][startingPos.y] = "@"
                }
                
            } else if individualMove == "v" {
                validity := false
                numberOfBoxesToMove := 0
                for i := startingPos.x+1; i < xlen-1; i++ {
                    if warehouse2dArr[i][startingPos.y] == "."{
                        validity = true
                        break
                    } else if warehouse2dArr[i][startingPos.y] == "#"{
                        break
                    }
                    numberOfBoxesToMove++
                }

                if validity {
                    for i := numberOfBoxesToMove; i > 0; i-- {
                        newIndex := startingPos.x + i + 1
                        warehouse2dArr[newIndex][startingPos.y] = warehouse2dArr[newIndex - 1][startingPos.y]
                    }

                    warehouse2dArr[startingPos.x][startingPos.y] = "."
                    startingPos = position{startingPos.x + 1, startingPos.y}
                    warehouse2dArr[startingPos.x][startingPos.y] = "@"
                }
            } else { // <
                validity := false
                numberOfBoxesToMove := 0
                for i := startingPos.y-1; i > 0; i-- {
                    if warehouse2dArr[startingPos.x][i] == "."{
                        validity = true
                        break
                    } else if warehouse2dArr[startingPos.x][i] == "#"{
                        break
                    }
                    numberOfBoxesToMove++
                }

                if validity {
                    for i := numberOfBoxesToMove; i > 0; i-- {
                        newIndex := startingPos.y - (i + 1)
                        warehouse2dArr[startingPos.x][newIndex] = warehouse2dArr[startingPos.x][newIndex + 1]
                    }

                    warehouse2dArr[startingPos.x][startingPos.y] = "."
                    startingPos = position{startingPos.x, startingPos.y - 1}
                    warehouse2dArr[startingPos.x][startingPos.y] = "@"
                }
            }
        }
    }

    total := 0
    for x, row := range warehouse2dArr {
        for y, char := range row {
            if char == "O"{
                total += (100 * x + y)
            }
        }
    }
    fmt.Println("Day 15 Solution (Part 1):", total)
    fmt.Println("Part 1 execution time:", time.Since(start), "\n")

	start = time.Now()
	// exec part2()
    fmt.Println("Day 15 Solution (Part 2):")
    fmt.Println("Part 2 execution time:", time.Since(start))
}
