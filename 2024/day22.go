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

func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

    nums := strings.Split(input, "\n")

    start := time.Now()
    var result int
    for _, num := range nums {
        secretNum, _ := strconv.Atoi(num)
        for i := 0; i < 2000; i++ {
            subResult := secretNum * 64
            secretNum = subResult ^ secretNum
            secretNum = secretNum % 16777216

            subResult = secretNum / 32
            secretNum = subResult ^ secretNum
            secretNum = secretNum % 16777216

            subResult = secretNum * 2048
            secretNum = subResult ^ secretNum
            secretNum = secretNum % 16777216
        }

        result += secretNum
    }

    fmt.Println("Day 22 Solution (Part 1):", result)
    fmt.Println("Part 1 execution time:", time.Since(start), "\n")

    start = time.Now()
    // exec part 2
    fmt.Println("Day 22 Solution (Part 2):")
    fmt.Println("Part 2 execution time:", time.Since(start))
}