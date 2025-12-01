package main

import (
    "fmt"
    "strings"
    "os"
    "github.com/simonolsson98/adventofcode/utils"
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

    start := time.Now()
    validSum := calculateValidSum(input, false)
    fmt.Println("Day 7 Solution (Part 1):", validSum)
    fmt.Println("Part 1 execution time:", time.Since(start))

	start = time.Now()
    validSum = calculateValidSum(input, true)
    fmt.Println("Day 7 Solution (Part 2):", validSum)
    fmt.Println("Part 2 execution time:", time.Since(start))
}

func calculateValidSum(input string, part2 bool) int {
    var validSum int
    lines := strings.Split(input, "\n")
    for _, line := range lines {
        nums := strings.Split(line, " ")
        target, _ := strconv.Atoi(strings.TrimRight(nums[0], ":"))
        startSum, _ := strconv.Atoi(nums[1])

        validity := checkLimit(target, "*", startSum, nums, 2, part2)
        if validity {
            validSum += target
            continue
        }

        validity = checkLimit(target, "+", startSum, nums, 2, part2)
        if validity {
            validSum += target
            continue
        }

        if part2 {
            validity = checkLimit(target, "||", startSum, nums, 2, true)
            if validity {
                validSum += target
                continue
            }
        }
    }

    return validSum
}

func checkLimit(target int, operator string, subSum int, nums []string, index int, part2 bool) (valid bool){
    var sum int
    nextNum, _ := strconv.Atoi(nums[index])
    if operator == "*" {
        sum = subSum * nextNum
    } else if operator == "+" {
        sum = subSum + nextNum
    } else  {
        part1 := strconv.Itoa(subSum)
        part2 := strconv.Itoa(nextNum)
        sum, _= strconv.Atoi(part1 + part2)
    }

    if sum > target {
        return false
    } else if sum == target && index + 1 == len(nums) { // index + 1 == len(nums) since we gotta use all numbers..
        return true
    } else {
        index++
        if index >= len(nums) {
            return false
        }

        val:= checkLimit(target, "*", sum, nums, index, part2)
        if val {
            return val
        }

        val = checkLimit(target, "+", sum, nums, index, part2)
        if val {
            return val
        }

        if part2 {
            val = checkLimit(target, "||", sum, nums, index, part2)
            if val {
                return val
            }
        }

        return false
    }
}