package main

import (
    "fmt"
    "strings"
    "os"
    "2024/utils"
    "path/filepath"
)

func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

    var grid [][]rune
    for _, line := range strings.Split(input, "\n") {
        grid = append(grid, []rune(line))
    }

    var sum int
    for i, row := range grid {
        for j, char := range row {
            sum += CheckPart1Matches(char, grid, i, j)
        }
    }

    fmt.Println("Day 4 Solution (Part 1):", sum)
    fmt.Println("Day 4 Solution (Part 2):")
}

func CheckPart1Matches(character rune, grid [][]rune, i int, j int) (sum int){
    // Down
    if i+3 < len(grid) && character == 'X' && 
        grid[i+1][j] == 'M' && 
        grid[i+2][j] == 'A' && 
        grid[i+3][j] == 'S' { 
        sum += 1
    }
    // Up
    if i-3 >= 0 && character == 'X' && 
       grid[i-1][j] == 'M' && 
       grid[i-2][j] == 'A' && 
       grid[i-3][j] == 'S' { 
        sum += 1
    }
    // Right
    if j+3 < len(grid[0]) && character == 'X' && 
       grid[i][j+1] == 'M' && 
       grid[i][j+2] == 'A' && 
       grid[i][j+3] == 'S' { 
        sum += 1
    }
    // Left
    if j-3 >= 0 && character == 'X' && 
       grid[i][j-1] == 'M' && 
       grid[i][j-2] == 'A' && 
       grid[i][j-3] == 'S' { 
        sum += 1
    }
    // Diagonal Down-Right
    if i+3 < len(grid) && j+3 < len(grid[0]) && character == 'X' && 
       grid[i+1][j+1] == 'M' && 
       grid[i+2][j+2] == 'A' && 
       grid[i+3][j+3] == 'S' {
        sum += 1
    }
    // Diagonal Down-Left
    if i+3 < len(grid) && j-3 >= 0 && character == 'X' && 
       grid[i+1][j-1] == 'M' && 
       grid[i+2][j-2] == 'A' && 
       grid[i+3][j-3] == 'S' { 
        sum += 1
    }
    // Diagonal Up-Right
    if i-3 >= 0 && j+3 < len(grid[0]) && character == 'X' && 
       grid[i-1][j+1] == 'M' && 
       grid[i-2][j+2] == 'A' && 
       grid[i-3][j+3] == 'S' { 
        sum += 1
    }
    // Diagonal Up-Left
    if i-3 >= 0 && j-3 >= 0 && character == 'X' && 
       grid[i-1][j-1] == 'M' && 
       grid[i-2][j-2] == 'A' && 
       grid[i-3][j-3] == 'S' { 
        sum += 1
    }

    return sum
}
