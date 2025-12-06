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

    var grid [][]string
    for _, line := range strings.Split(input, "\n") {
        var row []string
        for _, field := range strings.Fields(line) {
            row = append(row, field)
        }
        grid = append(grid, row)
    }

    start := time.Now()
    result := part1(grid)
    fmt.Println("Day 6 Solution (Part 1):", result)
    fmt.Println("Part 1 execution time:", time.Since(start))

    start = time.Now()
    result = part2(grid)
    fmt.Println("Day 6 Solution (Part 2):", result)
    fmt.Println("Part 2 execution time:", time.Since(start))
}

func part1(grid [][]string) int {
    var total int = 0
    colSize := len(grid[0])
    rowSize := len(grid)
    for i := range colSize {
        var operation string = grid[rowSize - 1][i] 
        startingValue := 0
        if operation == "*" {
            startingValue = 1
        }
            
        for j := 0; j < rowSize - 1; j++ {
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

func part2(grid [][]string) int {
    
    return 0
}
