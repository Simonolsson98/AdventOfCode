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
    xpos int
    ypos int
}

var visited map[position][]position = make(map[position][]position)
func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

    zeroes := []position{}
    for x, line := range strings.Split(input, "\n") {
        for y, char := range strings.Split(line, ""){
            if char == "0"{
                zeroes = append(zeroes, position{xpos: x, ypos: y})
            }
        }
    }

    var numberOfStuff int; 
    for _, startingPos := range zeroes {
        numberOfStuff += (
            checkPos(strings.Split(input, "\n"), startingPos, 0, 0, startingPos) + 
            checkPos(strings.Split(input, "\n"), startingPos, 0, 1, startingPos) + 
            checkPos(strings.Split(input, "\n"), startingPos, 0, 2, startingPos) +
            checkPos(strings.Split(input, "\n"), startingPos, 0, 3, startingPos)) 
    }

	start := time.Now()
	// exec part1()
    fmt.Println("Day 10 Solution (Part 1):", numberOfStuff)
    fmt.Println("Part 1 execution time:", time.Since(start), "\n")

	start = time.Now()
	// exec part2()
    fmt.Println("Day 10 Solution (Part 2):")
    fmt.Println("Part 2 execution time:", time.Since(start))
}

func checkPos(splitInput []string, startPos position, value int, dir int, OGPos position) (res int){
    for {
        x := startPos.xpos
        y := startPos.ypos

        if dir == 0 && x-1 >= 0{
            up, _ := strconv.Atoi(strings.Split(splitInput[x-1], "")[y])
            if up == 9 && up == value + 1 {
                reallies := visited[position{x-1, y}]
                for _, real := range reallies {
                    if real == OGPos {
                        return 0
                    }
                }

                visited[position{x-1, y}] = append(visited[position{x-1, y}], OGPos)
                return 1
            } else if up == value + 1 {
                return checkPos(splitInput, position{xpos: x-1, ypos: y}, up, 0, OGPos) +
                    checkPos(splitInput, position{xpos: x-1, ypos: y}, up, 1, OGPos) +
                    checkPos(splitInput, position{xpos: x-1, ypos: y}, up, 2, OGPos) +
                    checkPos(splitInput, position{xpos: x-1, ypos: y}, up, 3, OGPos)
            } else {
                return 0
            }
        }

        if dir == 1 && y+1 < len(splitInput[0]){
            right, _ := strconv.Atoi(strings.Split(splitInput[x], "")[y+1])
            if right == 9 && right == value + 1 {
                reallies := visited[position{x, y+1}]
                for _, real := range reallies {
                    if real == OGPos {
                        return 0
                    } 
                }

                visited[position{x, y+1}] = append(visited[position{x, y+1}], OGPos)
                return 1
            } else if right == value + 1 {
                return checkPos(splitInput, position{xpos: x, ypos: y+1}, right, 0, OGPos) +
                    checkPos(splitInput, position{xpos: x, ypos: y+1}, right, 1, OGPos) +
                    checkPos(splitInput, position{xpos: x, ypos: y+1}, right, 2, OGPos) +
                    checkPos(splitInput, position{xpos: x, ypos: y+1}, right, 3, OGPos)
            } else {
                return 0
            }
        }

        if dir == 3 && y-1 >= 0{
            left, _ := strconv.Atoi(strings.Split(splitInput[x], "")[y-1])
            if left == 9 && left == value + 1 {
                reallies := visited[position{x, y-1}]
                for _, real := range reallies {
                    if real == OGPos {
                        return 0
                    } 
                }

                visited[position{x, y-1}] = append(visited[position{x, y-1}], OGPos)
                return 1
            } else if left == value + 1 {
                return checkPos(splitInput, position{xpos: x, ypos: y-1}, left, 0, OGPos) +
                    checkPos(splitInput, position{xpos: x, ypos: y-1}, left, 1, OGPos) +
                    checkPos(splitInput, position{xpos: x, ypos: y-1}, left, 2, OGPos) +
                    checkPos(splitInput, position{xpos: x, ypos: y-1}, left, 3, OGPos)
            } else {
                return 0
            }
        }

        if dir == 2 && x+1 < len(splitInput){
            down, _ := strconv.Atoi(strings.Split(splitInput[x+1], "")[y])
            if down == 9 && down == value + 1 {
                reallies := visited[position{x+1, y}]
                for _, real := range reallies {
                    if real == OGPos {
                        return 0
                    } 
                }

                visited[position{x+1, y}] = append(visited[position{x+1, y}], OGPos)
                return 1
            } else if down == value + 1 {
                return checkPos(splitInput, position{xpos: x+1, ypos: y}, down, 0, OGPos) +
                    checkPos(splitInput, position{xpos: x+1, ypos: y}, down, 1, OGPos) +
                    checkPos(splitInput, position{xpos: x+1, ypos: y}, down, 2, OGPos) +
                    checkPos(splitInput, position{xpos: x+1, ypos: y}, down, 3, OGPos)
            } else {
                return 0
            } 
        }

        return 0
    }
}
