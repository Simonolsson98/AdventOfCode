package main

import (
    "fmt"
    "strings"
    "os"
    "2024/utils"
    "strconv"
    "path/filepath"
    "time"
    "regexp"
)

func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

	start := time.Now()
	
    games := strings.Split(input, "\n\n")
    totalTokens := 0
    for _, game := range games {
        minres := -1
        splitGame := strings.Split(game, "\n")
        numsA := extractNumbers(splitGame[0])
        numsB := extractNumbers(splitGame[1])
        numsP := extractNumbers(splitGame[2])
        for i := 0; i <= 100; i++ {
            for j := 0; j <= 100; j++ {
                calcValX := i * numsA[0] + j * numsB[0]
                calcValY := i * numsA[1] + j * numsB[1]
                if calcValX == numsP[0] && calcValY == numsP[1] {
                    if minres == -1 || minres > 3 * i + 1 * j {
                        minres = 3 * i + 1 * j
                    }
                }
            }
        }

        if minres == -1{
            minres = 0
        }
        totalTokens += minres
    } 

    fmt.Println("Day 13 Solution (Part 1):", totalTokens)
    fmt.Println("Part 1 execution time:", time.Since(start), "\n")

	start = time.Now()
	// exec part2()
    fmt.Println("Day 13 Solution (Part 2):")
    fmt.Println("Part 2 execution time:", time.Since(start))
}

func extractNumbers(input string) ([]int) {
    re := regexp.MustCompile(`[+=](\d+)`)

    // Find all matches
    matches := re.FindAllStringSubmatch(input, -1)

    // Extract the numbers
    var numbers []int
    for _, match := range matches {
        if len(match) > 1 {
            num, err := strconv.Atoi(match[1])
            if err == nil {
                numbers = append(numbers, num)
            }
        }
    }

    return numbers
}
