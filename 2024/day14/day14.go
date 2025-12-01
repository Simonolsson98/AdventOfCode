package main

import (
    "fmt"
    "strings"
    "os"
    "github.com/simonolsson98/adventofcode/utils"
    "strconv"
    "path/filepath"
    "time"
    "regexp"
)

var xrange = 103
var yrange = 101
func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

    start := time.Now()
    fmt.Println("Day 14 Solution (Part 1):", part1(input))
    fmt.Println("Part 1 execution time:", time.Since(start))

    start = time.Now()
    fmt.Println("Day 14 Solution (Part 2):", part2(input))
    fmt.Println("Part 2 execution time:", time.Since(start))
}

func part1(input string) (int){
    quadrant1 := 0; quadrant2 := 0; quadrant3 := 0; quadrant4 := 0
    for _, line := range strings.Split(input, "\n") {
        newxPos, newyPos := calculateNewPositions(line, 100)

        if newxPos < xrange / 2{
            if newyPos < yrange/2 {
                quadrant1 += 1
            } else if newyPos > yrange/2{
                quadrant2 += 1
            }
        } else if newxPos > xrange/2 {
            if newyPos < yrange/2 {
                quadrant3 += 1
            } else if newyPos > yrange/2  {
                quadrant4 += 1
            }
        }
    }

    return quadrant1 * quadrant2 * quadrant3 * quadrant4
}

func part2(input string) (int){
    limit := 3
    for i := 0; ; i++ {
        posAfterIter := [][]int{}
        for _, line := range strings.Split(input, "\n") {
            newxPos, newyPos := calculateNewPositions(line, i)
            posAfterIter = append(posAfterIter, []int{newxPos, newyPos})
        }

        numOfYInRow := 0
        for x := 0; x < xrange; x++ {
            for y := 0; y < yrange; y++ {
                if check(posAfterIter, []int{x, y}){
                    numOfYInRow += 1
                } else {
                    numOfYInRow = 0
                }

                // I came up with this condition purely by guessing that a christmas tree should be wide at the bottom...
                if numOfYInRow > limit {
                    for a := 0; a < xrange; a++ {
                        for b := 0; b < yrange; b++ {
                            if check(posAfterIter, []int{a, b}){
                                fmt.Print("X")
                            } else {
                                numOfYInRow = 0
                                fmt.Print(" ")
                            }
                        }
                        fmt.Println()
                    }

                    var ans string
                    fmt.Println("does this look like a xmas tree to you? (y/n)")
                    fmt.Scan(&ans)
                    if ans == "y" {
                        return i
                    } else {
                        limit++
                        numOfYInRow = 0
                        break
                    }
                }
            }
        }
    }

    return -1
}

func calculateNewPositions(line string, seconds int) (int, int) {
    re := regexp.MustCompile(`-?\d+`)
    matches := re.FindAllString(line, -1)

    ypos, _ := strconv.Atoi(matches[0])
    xpos, _ := strconv.Atoi(matches[1])
    yvel, _ := strconv.Atoi(matches[2])
    xvel, _ := strconv.Atoi(matches[3])

    // Calculate new positions
    newxPos := ((seconds * xvel + xpos) % xrange + xrange) % xrange
    newyPos := ((seconds * yvel + ypos) % yrange + yrange) % yrange

    return newxPos, newyPos
}

func check(checkThis [][]int, ele []int) (bool){
    for _, eleInIter := range checkThis{
        if ele[0] == eleInIter[0] && ele[1] == eleInIter[1]{
            return true
        }
    }

    return false
}