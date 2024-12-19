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

var (
    allAvailablePatterns []string
    sortedStripes = make(map[byte][]string, 0)
)

func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

    splitInput := strings.Split(input, "\n\n")
    allAvailablePatterns = strings.Split(splitInput[0], ", ")
    for _, pattern := range allAvailablePatterns {
        sortedStripes[pattern[0]] = append(sortedStripes[pattern[0]], pattern)
    }

    towelsToCheck := strings.Split(splitInput[1], "\n")
    availableTowels := 0
    
    start := time.Now()
    for i, towelToCheck := range towelsToCheck {
        available := checkAll([]string{towelToCheck})

        if !available {
            fmt.Println("unavailable:", towelToCheck)
        } else {
            availableTowels++
        }

        fmt.Println("i: ", i, "done and available was:", available)
    }


    // exec part 1
    fmt.Println("Day 19 Solution (Part 1):", availableTowels)
    fmt.Println("Part 1 execution time:", time.Since(start), "\n")

    start = time.Now()
    // exec part 2
    fmt.Println("Day 19 Solution (Part 2):")
    fmt.Println("Part 2 execution time:", time.Since(start))
}

func checkPattern(towel string, pattern string) (bool){
    return strings.HasPrefix(towel, pattern)
}

func checkAll(validTowels []string) (bool) {
    var atleastOnePassing bool = false
    var newTowels []string
    for _, validTowel := range validTowels {
        for _, availablePattern := range sortedStripes[validTowel[0]] {
            if len(availablePattern) > len(validTowel){
                continue
            }

            if checkPattern(validTowel, availablePattern){
                atleastOnePassing = true
                newTowel := validTowel[len(availablePattern):]
                if len(newTowel) == 0{
                    return true
                }

                newTowels = append(newTowels, newTowel)
            }
        }
    }
    
    if !atleastOnePassing {
        return false
    }

    return checkAll(newTowels)
}