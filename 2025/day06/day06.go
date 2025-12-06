package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"

	"github.com/simonolsson98/adventofcode/utils"

	"path/filepath"
	"time"
)

func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

    start := time.Now()
    result := part1(input)
    fmt.Println("Day 6 Solution (Part 1):", result)
    fmt.Println("Part 1 execution time:", time.Since(start))

    start = time.Now()
    result = part2(input)
    fmt.Println("Day 6 Solution (Part 2):", result)
    fmt.Println("Part 2 execution time:", time.Since(start))
}

func part1(input string) int {
    var grid [][]string
    for _, line := range strings.Split(input, "\n") {
        grid = append(grid, strings.Fields(line))
    }

    total := 0
    colSize := len(grid[0])
    rowSize := len(grid)
    
    for i := range colSize {
        operation := grid[rowSize-1][i]
        startingValue := 0
        if operation == "*" {
            startingValue = 1
        }

        for j := 0; j < rowSize-1; j++ {
            val, _ := strconv.Atoi(grid[j][i])

            switch operation {
            case "+":
                startingValue += val
            case "*":
                startingValue *= val
            }
        }

        total += startingValue
    }
    return total
}

func part2(input string) int {
    rows := strings.Split(input, "\n")
    height := len(rows)
    if height == 0 {
        return 0
    }
    width := len(rows[0])

    total := 0
    var pendingNums []int

    for col := width - 1; col >= 0; col-- {
        var currentNumStr string

        for row := 0; row < height; row++ {
            char := string(rows[row][col])
            trimmed := strings.TrimSpace(char)

            if trimmed == "+" || trimmed == "*" {
                if currentNumStr != "" {
                    val, _ := strconv.Atoi(currentNumStr)
                    pendingNums = append(pendingNums, val)
                }

                if trimmed == "+" {
                    sum := 0
                    for _, n := range pendingNums {
                        sum += n
                    }
                    total += sum
                } else {
                    prod := 1
                    for _, n := range pendingNums {
                        prod *= n
                    }
                    total += prod
                }

                // reset
                pendingNums = []int{}
                currentNumStr = ""
                break
            }

            currentNumStr += trimmed
        }

        if currentNumStr != "" {
            val, _ := strconv.Atoi(currentNumStr)
            pendingNums = append(pendingNums, val)
        }
    }

    return total
}
