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

func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

    start := time.Now()
    // exec part 1
    fmt.Println("Day 23 Solution (Part 1):")
    fmt.Println("Part 1 execution time:", time.Since(start), "\n")

    start = time.Now()
    // exec part 2
    fmt.Println("Day 23 Solution (Part 2):")
    fmt.Println("Part 2 execution time:", time.Since(start))
}