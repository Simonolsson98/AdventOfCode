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
    var sum2 int
    for i, row := range grid {
        for j, char := range row {
            sum += CheckPart1Matches(char, grid, i, j)
            sum2 += CheckPart2Matches(char, grid, i, j)
        }
    }

    fmt.Println("Day 4 Solution (Part 1):", sum)
    fmt.Println("Day 4 Solution (Part 2):", sum2)
}

func CheckPart1Matches(character rune, grid [][]rune, i int, j int) (sum int){
    // down
    if i+3 < len(grid) && character == 'X' && 
        grid[i+1][j] == 'M' && 
        grid[i+2][j] == 'A' && 
        grid[i+3][j] == 'S' { 
        sum += 1
    }
    // up
    if i-3 >= 0 && character == 'X' && 
       grid[i-1][j] == 'M' && 
       grid[i-2][j] == 'A' && 
       grid[i-3][j] == 'S' { 
        sum += 1
    }
    // right
    if j+3 < len(grid[0]) && character == 'X' && 
       grid[i][j+1] == 'M' && 
       grid[i][j+2] == 'A' && 
       grid[i][j+3] == 'S' { 
        sum += 1
    }
    // left
    if j-3 >= 0 && character == 'X' && 
       grid[i][j-1] == 'M' && 
       grid[i][j-2] == 'A' && 
       grid[i][j-3] == 'S' { 
        sum += 1
    }
    // diagonal down right
    if i+3 < len(grid) && j+3 < len(grid[0]) && character == 'X' && 
       grid[i+1][j+1] == 'M' && 
       grid[i+2][j+2] == 'A' && 
       grid[i+3][j+3] == 'S' {
        sum += 1
    }
    // diagonal down left
    if i+3 < len(grid) && j-3 >= 0 && character == 'X' && 
       grid[i+1][j-1] == 'M' && 
       grid[i+2][j-2] == 'A' && 
       grid[i+3][j-3] == 'S' { 
        sum += 1
    }
    // diagonal up right
    if i-3 >= 0 && j+3 < len(grid[0]) && character == 'X' && 
       grid[i-1][j+1] == 'M' && 
       grid[i-2][j+2] == 'A' && 
       grid[i-3][j+3] == 'S' { 
        sum += 1
    }
    // diagonal up left
    if i-3 >= 0 && j-3 >= 0 && character == 'X' && 
       grid[i-1][j-1] == 'M' && 
       grid[i-2][j-2] == 'A' && 
       grid[i-3][j-3] == 'S' { 
        sum += 1
    }

    return sum
}

func CheckPart2Matches(character rune, grid [][]rune, i int, j int) (sum int){
    if i+1 < len(grid) && i-1 >= 0 && j-1 >= 0 && j+1 < len(grid[0]) && character == 'A' && 
    (
        // M + S or S + M diagonal down right
        ((grid[i+1][j+1] == 'M' && grid[i-1][j-1] == 'S') || (grid[i+1][j+1] == 'S' && grid[i-1][j-1] == 'M')) &&
        // M + S or S + M diagonal down left
        ((grid[i+1][j-1] == 'M' && grid[i-1][j+1] == 'S') || (grid[i+1][j-1] == 'S' && grid[i-1][j+1] == 'M'))) {
    sum += 1
    }

    return sum
}
