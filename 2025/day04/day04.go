package main

import (
    "fmt"
    "strings"
    "os"
    "github.com/simonolsson98/adventofcode/utils"
    //"strconv"
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
    fmt.Println("Day 4 Solution (Part 1):", result)
    fmt.Println("Part 1 execution time:", time.Since(start), "\n")

    start = time.Now()
    result = part2(input)
    fmt.Println("Day 4 Solution (Part 2):", result)
    fmt.Println("Part 2 execution time:", time.Since(start))
}

func part1(input string) int {
    
    return 0
}

func part2(input string) int {
    
    return 0
}
