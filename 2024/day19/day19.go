package main

import (
    "fmt"
    "strings"
    "os"
    "github.com/simonolsson98/adventofcode/utils"
    //"strconv"
    "path/filepath"
    "time"
    "sort"
)

var (
    allAvailablePatterns []string
    sortedStripes = make(map[byte][]string, 0)
    checkedParts map[string]int
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
    sort.Slice(allAvailablePatterns, func(i, j int) bool {
        return len(allAvailablePatterns[i]) > len(allAvailablePatterns[j])
    })

    for _, pattern := range allAvailablePatterns {
        sortedStripes[pattern[0]] = append(sortedStripes[pattern[0]], pattern)
    }

    towelsToCheck := strings.Split(splitInput[1], "\n")
    availableTowels := 0
    
    start := time.Now()
    checkedParts = make(map[string]int)
    for _, towelToCheck := range towelsToCheck {
        available := checkAll(towelToCheck)

        if available {
            availableTowels++
        }
    }

    fmt.Println("Day 19 Solution (Part 1):", availableTowels)
    fmt.Println("Part 1 execution time:", time.Since(start))

    start = time.Now()
    // exec part 2
    fmt.Println("Day 19 Solution (Part 2):")
    fmt.Println("Part 2 execution time:", time.Since(start))
}

func checkAll(validTowel string) (bool) {
    if len(validTowel) == 0{
        checkedParts[validTowel] = 1
        return true
    }

    for _, availablePattern := range sortedStripes[validTowel[0]] {
        if len(availablePattern) > len(validTowel){
            continue
        }

        if checkedParts[validTowel] == -1 {
            return false
        }

        if checkPattern(validTowel, availablePattern){
            newTowel := validTowel[len(availablePattern):]
            if checkAll(newTowel){
                return true
            }
        }
    }

    checkedParts[validTowel] = -1
    return false
}

func checkPattern(towel string, pattern string) (bool){
    return strings.HasPrefix(towel, pattern)
}