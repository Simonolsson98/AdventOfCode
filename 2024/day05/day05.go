package main

import (
    "fmt"
    "strings"
    "strconv"
    "os"
    "path/filepath"
    "github.com/simonolsson98/adventofcode/utils"
    "time"
)

func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

    parts := strings.Split(input, "\n\n")
    rules := strings.Split(parts[0], "\n")
    inputRows := strings.Split(parts[1], "\n")

    constraints := make([][2]int, 0)

    for _, rule := range rules {
        res := strings.Split(rule, "|")
        firstNum, _ := strconv.Atoi(res[0])
        secondNum, _ := strconv.Atoi(res[1])
        constraints = append(constraints, [2]int{firstNum, secondNum})
    }

    start := time.Now()
    sum := part1(inputRows, constraints)
    fmt.Println("Day 5 Solution (Part 1):", sum)
    fmt.Println("Part 1 execution time:", time.Since(start), "\n")
    
    start = time.Now()
    sum2 := part2(inputRows, constraints)
    fmt.Println("Day 5 Solution (Part 2):", sum2-sum)
    fmt.Println("Part 2 execution time:", time.Since(start))
}

func part1(inputRows []string, constraints [][2]int) (int) {
    var validPaths []string
    var invalidPaths []string
    var sum int

    for _, inputRow := range inputRows {
        nums := strings.Split(inputRow, ",")
        valid := true

        for _, constraint := range constraints {
            firstNum, secondNum := constraint[0], constraint[1]

            firstIndex := findIndex(nums, firstNum)
            secondIndex := findIndex(nums, secondNum)

            // Valid if either constraint is not part of it, or first element appears before second element
            if (firstIndex == -1 || secondIndex == -1) || firstIndex < secondIndex {
                continue
            }

            valid = false
            break
        }

        if valid {
            validPaths = append(validPaths, inputRow)
        } else {
            invalidPaths = append(invalidPaths, inputRow)
        }
    }

    for _, validPath := range validPaths {
        epiclist := strings.Split(validPath, ",")
        numberToAdd, _ := strconv.Atoi(epiclist[(len(epiclist)-1)/2])
        sum += numberToAdd
    }

    return sum
}

var firstI int = -1
var secondI int = -1
func part2(inputRows []string, constraints [][2]int) (int) {
    var sum int

    for _, inputRow := range inputRows {
        nums := strings.Split(inputRow, ",")
        for ok := !check(nums, constraints); ok; ok = !check(nums, constraints) {
            if firstI == -1 || secondI == -1 {
                continue
            }

            temp := nums[firstI]
            nums[firstI] = nums[secondI]
            nums[secondI] = temp
        }

        numberToAdd, _ := strconv.Atoi(nums[(len(nums)-1)/2])
        sum += numberToAdd
    }

    return sum
}

func check(nums []string, constraints [][2]int) (surely bool){
    for _, constraint := range constraints {
        firstNum, secondNum := constraint[0], constraint[1]

        firstIndex := findIndex(nums, firstNum)
        secondIndex := findIndex(nums, secondNum)

        // Valid if either constraint is not part of it, or first element appears before second element
        if (firstIndex == -1 || secondIndex == -1) || firstIndex < secondIndex {
            firstI = -1
            secondI = -1
            continue
        }

        firstI = firstIndex
        secondI = secondIndex

        return false 
    }

    return true 
}

func findIndex(nums []string, target int) int {
    for i, num := range nums {
        realNum, _ := strconv.Atoi(num)
        if realNum == target {
            return i
        }
    }
    return -1
}
