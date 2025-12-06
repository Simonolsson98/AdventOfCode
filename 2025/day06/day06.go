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
        var row []string
        for _, field := range strings.Fields(line) {
            row = append(row, field)
        }
        grid = append(grid, row)
    }

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

func part2(input string) int {
    rows := strings.Split(input, "\n")
    rowLength := len(rows)
    colIndexLength := len(rows[0])

    var total int = 0
    nums := []int{}
    for colIndex := colIndexLength - 1; colIndex >= 0; colIndex-- {
        var digit string = ""
        for rowIndex := range rowLength {
            char := rows[rowIndex][colIndex]
            if string(char) == "" {
                continue
            }

            numToAdd , _ := strconv.Atoi(digit)

            // reached operator, so perform operation
            if strings.TrimSpace(string(char)) == "+" {
                nums = append(nums, numToAdd)
                
                sum := 0
                for i := 0; i < len(nums); i++ {
                    numToAdd = nums[i]
                    sum += numToAdd
                }

                total += sum
                digit = ""
                nums = []int{}
                break
            } else if strings.TrimSpace(string(char)) == "*" {
                nums = append(nums, numToAdd)

                product := 1
                for i := 0; i < len(nums); i++ {
                    numToAdd = nums[i]
                    product *= numToAdd
                }
                
                total += product
                digit = ""
                nums = []int{}
                break
            }

            digit = digit + strings.TrimSpace(string(char))
        }

        if strings.TrimSpace(digit) == "" {
            continue
        }
        numToAdd, _ := strconv.Atoi(strings.TrimSpace(digit))
        nums = append(nums, numToAdd)
    }

    return total
}
