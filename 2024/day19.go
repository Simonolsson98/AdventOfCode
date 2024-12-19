package main

import (
    "fmt"
    "strings"
    "os"
    "2024/utils"
    //"strconv"
    "path/filepath"
    "time"
    "sort"
)

var (
    allAvailablePatterns []string
    sortedStripes = make(map[byte][]string, 0)
    checkedParts map[string]bool
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
    for _, towelToCheck := range towelsToCheck {
        available := checkAll([]string{towelToCheck})

        if available {
            availableTowels++
        }

        fmt.Println(towelToCheck, "done and available was:", available)
    }


    // exec part 1
    fmt.Println("Day 19 Solution (Part 1):", availableTowels) //LF 324 
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
    checkedParts = make(map[string]bool)
    var atleastOnePassing bool = false
    for _, validTowel := range validTowels {
        for _, availablePattern := range sortedStripes[validTowel[0]] {
            if len(availablePattern) > len(validTowel){
                continue
            }

            if checkPattern(validTowel, availablePattern){
                checkedParts[availablePattern] = true
                newTowel := validTowel[len(availablePattern):]
                if len(newTowel) == 0{
                    return true
                }

                if checkedParts[newTowel]{
                    fmt.Println("cached: ", newTowel)
                    return true
                }

                atleastOnePassing = checkAll([]string{newTowel  })
                    return atleastOnePassing
            }
        }
    }

    return false
}