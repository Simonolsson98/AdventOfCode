package main

import (
    "fmt"
    "strings"
    "strconv"
    "os"
    "path/filepath"
    "2024/utils"
)

func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

    // Split the input on double newlines
    parts := strings.Split(input, "\n\n")
    rules := strings.Split(parts[0], "\n")
    inputRows := strings.Split(parts[1], "\n")

    // Create a list to store the rules as pairs
    constraints := make([][2]int, 0)

    // Parse the rules into the constraints list
    for _, rule := range rules {
        res := strings.Split(rule, "|")
        firstNum, _ := strconv.Atoi(res[0])
        secondNum, _ := strconv.Atoi(res[1])
        constraints = append(constraints, [2]int{firstNum, secondNum})
    }

    sum := part1(inputRows, constraints)

    fmt.Println("Day 5 Solution (Part 1):", sum)
    fmt.Println("Day 5 Solution (Part 2):")
}

func part1(inputRows []string, constraints [][2]int) (int) {
    var validPaths []string
    var invalidPaths []string
    var sum int

    for _, inputRow := range inputRows {
        nums := strings.Split(inputRow, ",")
        valid := true

        // Check each constraint
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

        // Append to valid or invalid paths
        if valid {
            validPaths = append(validPaths, inputRow)
        } else {
            invalidPaths = append(invalidPaths, inputRow)
        }
    }

    // Calculate the sum of middle elements for valid paths
    for _, validPath := range validPaths {
        epiclist := strings.Split(validPath, ",")
        ffs, _ := strconv.Atoi(epiclist[(len(epiclist)-1)/2])
        sum += ffs
    }

    return sum
}

// Helper function to find the index of a number in a slice
func findIndex(nums []string, target int) int {
    for i, num := range nums {
        realNum, _ := strconv.Atoi(num)
        if realNum == target {
            return i
        }
    }
    return -1
}
