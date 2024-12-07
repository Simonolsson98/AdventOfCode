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

    start := time.Now()
    var validSum int64
    lines := strings.Split(input, "\n")
    for _, line := range lines {
        nums := strings.Split(line, " ")
        target, _ := strconv.ParseInt(strings.TrimRight(nums[0], ":"), 10, 64)
        startSum, _ := strconv.ParseInt(nums[1], 10, 64)
        // start at index 2, since 0 is target and 1 is first num
        validity := checkLimit(target, "*", startSum, nums, 2)
        if validity {
            validSum += target
            continue
        }

        validity = checkLimit(target, "+", startSum, nums, 2)
        if validity {
            validSum += target
            continue
        }
    }

    fmt.Println("Day 7 Solution (Part 1):", validSum)
    fmt.Println("Part 1 execution time:", time.Since(start), "\n")

	start = time.Now()
	// exec part2()
    fmt.Println("Day 7 Solution (Part 2):")
    fmt.Println("Part 2 execution time:", time.Since(start))
}

func checkLimit(target int64, operator string, subSum int64, nums []string, index int) (valid bool){
    var sum int64
    nextNum, _ := strconv.ParseInt(nums[index], 10, 64)
    if operator == "*" {
        sum = subSum * nextNum
    } else {
        sum = subSum + nextNum
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

        val:= checkLimit(target, "*", sum, nums, index)
        if val {
            return val
        }

        val = checkLimit(target, "+", sum, nums, index)
        if val {
            return val
        }

        return false
    }
}
// wut   2654749936343
// wrong 2654749936423