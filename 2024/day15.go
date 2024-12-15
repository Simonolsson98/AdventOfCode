package main

import (
    "fmt"
    "strings"
    "os"
    "2024/utils"
    "sort"
    "path/filepath"
    "time"
)

type position struct {
    x int
    y int
}

var warehouse2dArr = [][]string{}
var startingPos = position{}
func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

    start := time.Now()
    warehouseAndMoves := strings.Split(input, "\n\n")
    InitWarehouse2dArr(warehouseAndMoves[0])
    Part1(warehouseAndMoves[1])
    fmt.Println("Day 15 Solution (Part 1):", CalcTotalGPSCoords())
    fmt.Println("Part 1 execution time:", time.Since(start), "\n")

	start = time.Now()
    warehouse2dArr = [][]string{}
    InitWarehouse2dArrPart2(warehouseAndMoves[0])
	Part2(warehouseAndMoves[1])
    fmt.Println("Day 15 Solution (Part 2):", CalcTotalGPSCoords())
    fmt.Println("Part 2 execution time:", time.Since(start))
}

func Part1(moves string){
    xlen := len(warehouse2dArr)
    ylen := len(warehouse2dArr[0])
    for _, move := range strings.Split(moves, "\n") {
        for _, individualMove := range strings.Split(move, "") {
            if individualMove == "^" {
                validity := false
                numberOfBoxesToMove := 0
                for i := startingPos.x - 1; i > 0; i-- {
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
}

var numberOfBoxesToMove int;
var lastBoxXPos int;
var boxesToMove []position
func CheckRecursiveValidity(x int, y int, dir string) (bool){
    if dir == "up" {
        if warehouse2dArr[x][y] == "[" && warehouse2dArr[x][y + 1] == "]" {
            boxesToMove = append(boxesToMove, position{x, y})
            boxesToMove = append(boxesToMove, position{x, y + 1})
            lastBoxXPos = x - 1
            return (CheckRecursiveValidity(x - 1, y, dir) || warehouse2dArr[x - 1][y] == ".") && 
                (CheckRecursiveValidity(x - 1, y + 1, dir) || warehouse2dArr[x - 1][y + 1] == ".")
        } else if warehouse2dArr[x][y] == "]" && warehouse2dArr[x][y - 1] == "["{
            lastBoxXPos = x - 1
            boxesToMove = append(boxesToMove, position{x, y})
            boxesToMove = append(boxesToMove, position{x, y - 1})
            return (CheckRecursiveValidity(x - 1, y - 1, dir) || warehouse2dArr[x - 1][y - 1] == ".") && 
                (CheckRecursiveValidity(x - 1, y, dir) || warehouse2dArr[x - 1][y] == ".")
        } else {
            lastBoxXPos = x
            return warehouse2dArr[x][y] == "."
        }
    } else {
        if warehouse2dArr[x][y] == "[" && warehouse2dArr[x][y + 1] == "]" {
            boxesToMove = append(boxesToMove, position{x, y})
            boxesToMove = append(boxesToMove, position{x, y+1})
            lastBoxXPos = x + 1
            return (CheckRecursiveValidity(x + 1, y, dir) || warehouse2dArr[x + 1][y] == ".") && 
                (CheckRecursiveValidity(x + 1, y + 1, dir) || warehouse2dArr[x + 1][y + 1] == ".")
        } else if warehouse2dArr[x][y] == "]" && warehouse2dArr[x][y - 1] == "["{
            boxesToMove = append(boxesToMove, position{x, y})
            boxesToMove = append(boxesToMove, position{x, y-1})
            lastBoxXPos = x + 1
            return (CheckRecursiveValidity(x + 1, y - 1, dir) || warehouse2dArr[x + 1][y - 1] == ".") && 
                (CheckRecursiveValidity(x + 1, y, dir) || warehouse2dArr[x + 1][y] == ".")
        } else {
            lastBoxXPos = x
            return warehouse2dArr[x][y] == "."
        }
    }
}

func Part2(moves string){
    xlen := len(warehouse2dArr)
    ylen := len(warehouse2dArr[0])
    for _, move := range strings.Split(moves, "\n") {
        for _, individualMove := range strings.Split(move, "") {
            fmt.Println(individualMove)
            boxesToMove = []position{}
            if individualMove == "^" {
                validity := false
                lastBoxXPos = startingPos.x - 1
                for i := startingPos.x - 1; i > 0; i-- {
                    if warehouse2dArr[i][startingPos.y] == "[" {
                        validity = CheckRecursiveValidity(i, startingPos.y, "up") && CheckRecursiveValidity(i, startingPos.y + 1, "up")
                    } else if warehouse2dArr[i][startingPos.y] == "]" { 
                        validity = CheckRecursiveValidity(i, startingPos.y, "up") && CheckRecursiveValidity(i, startingPos.y - 1, "up")
                    } else {
                        validity = warehouse2dArr[i][startingPos.y] == "."
                        break
                    }

                    if !validity{
                        break
                    }
                }
                if validity {
                    sort.Slice(boxesToMove, func(i, j int) bool {return boxesToMove[i].x < boxesToMove[j].x})
                    alreadyChecked := map[position]bool{}
                    for _, boxesToMove := range boxesToMove {
                        _, exists := alreadyChecked[position{boxesToMove.x, boxesToMove.y}]
                        if !exists{
                            warehouse2dArr[boxesToMove.x - 1][boxesToMove.y] = warehouse2dArr[boxesToMove.x][boxesToMove.y]
                            warehouse2dArr[boxesToMove.x][boxesToMove.y] = "."
                            alreadyChecked[position{boxesToMove.x, boxesToMove.y}] = true
                        }
                    }

                    warehouse2dArr[startingPos.x][startingPos.y] = "."
                    startingPos = position{startingPos.x - 1, startingPos.y}
                    warehouse2dArr[startingPos.x][startingPos.y] = "@"
                    if warehouse2dArr[startingPos.x][startingPos.y + 1] == "]" {
                        warehouse2dArr[startingPos.x][startingPos.y + 1] = "."
                    }
                    if warehouse2dArr[startingPos.x][startingPos.y - 1] == "[" {
                        warehouse2dArr[startingPos.x][startingPos.y - 1] = "."
                    }
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
                lastBoxXPos = startingPos.x + 1
                for i := startingPos.x + 1; i < xlen - 1; i++ {
                    if warehouse2dArr[i][startingPos.y] == "[" {
                        validity = CheckRecursiveValidity(i, startingPos.y, "down") && CheckRecursiveValidity(i, startingPos.y + 1, "down")
                    } else if warehouse2dArr[i][startingPos.y] == "]" { 
                        validity = CheckRecursiveValidity(i, startingPos.y, "down") && CheckRecursiveValidity(i, startingPos.y - 1, "down")
                    } else {
                        validity = warehouse2dArr[i][startingPos.y] == "."
                        break
                    }

                    if !validity{
                        break
                    }
                }

                if validity {
                    sort.Slice(boxesToMove, func(i, j int) bool {return boxesToMove[i].x > boxesToMove[j].x})
                    alreadyChecked := map[position]bool{}
                    for _, boxesToMove := range boxesToMove {
                        _, exists := alreadyChecked[position{boxesToMove.x, boxesToMove.y}]
                        if !exists{
                            warehouse2dArr[boxesToMove.x + 1][boxesToMove.y] = warehouse2dArr[boxesToMove.x][boxesToMove.y]
                            warehouse2dArr[boxesToMove.x][boxesToMove.y] = "."
                            alreadyChecked[position{boxesToMove.x, boxesToMove.y}] = true
                        }
                    }

                    warehouse2dArr[startingPos.x][startingPos.y] = "."
                    startingPos = position{startingPos.x + 1, startingPos.y}
                    warehouse2dArr[startingPos.x][startingPos.y] = "@"
                    if warehouse2dArr[startingPos.x][startingPos.y + 1] == "]" {
                        warehouse2dArr[startingPos.x][startingPos.y + 1] = "."
                    }
                    if warehouse2dArr[startingPos.x][startingPos.y - 1] == "[" {
                        warehouse2dArr[startingPos.x][startingPos.y - 1] = "."
                    }
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
}

func debuggrid(){
        fmt.Println()
    for _, line := range warehouse2dArr {
        fmt.Println(line)
    }
        fmt.Println()
}

func InitWarehouse2dArr(warehouse string){
    for x, line := range strings.Split(warehouse, "\n") {
        splitLine := strings.Split(line, "")
        for y, char := range splitLine {
            if char == "@" {
                startingPos = position{x, y}
            }
        }
        warehouse2dArr = append(warehouse2dArr, splitLine)
    }
}
func InitWarehouse2dArrPart2(warehouse string){
    for x, line := range strings.Split(warehouse, "\n") {
        splitLine := strings.Split(line, "")
        newSplit := make([]string, 2*len(splitLine))
        for y, char := range splitLine {
            if char == "@" {
                startingPos = position{x, 2 * y}
                newSplit[2 * y] = "@"
                newSplit[2 * y + 1] = "."
            } else if char == "O"{
                newSplit[2 * y] = "["
                newSplit[2 * y + 1] = "]"
            } else if char == "#"{
                newSplit[2 * y] = "#"
                newSplit[2 * y + 1] = "#"
            } else if char == "."{
                newSplit[2 * y] = "."
                newSplit[2 * y + 1] = "."
            } 
        }
        warehouse2dArr = append(warehouse2dArr, newSplit)
    }
}

func CalcTotalGPSCoords() (int){
    total := 0
    for x, row := range warehouse2dArr {
        for y, char := range row {
            if char == "["{
                total += (100 * x + y)
            }
        }
    }

    return total
}