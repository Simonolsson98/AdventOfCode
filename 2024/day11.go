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

    nums := strings.Split(input, " ")

    fmt.Println("Day 11 Solution (Part 1):", test(25, nums))
    fmt.Println("Part 1 execution time:", time.Since(start), "\n")

	start = time.Now()
	// exec part2()
    fmt.Println("Day 11 Solution (Part 2):")
    fmt.Println("Part 2 execution time:", time.Since(start))
}

var cache = map[int]int{}
func test(iters int, nums []string) (res int){
    total := 0
    for _, strnum := range nums {
        num, _ := strconv.Atoi(strnum)
        total += runNum(iters, 0, num)
    }

    return total
}

func runNum(iters int, currIter int, num int) (res int){
    for i := currIter; i < iters; i++ {
        val, exists := cache[num]
        if exists && val == i {
            // fmt.Println("cache hit for:", num, ":", val)
            return 1
        }

        numAsStr := strconv.Itoa(num)
        if numAsStr == "0"{
            numAsStr = "1"
            num = 1
        } else if (len(numAsStr) % 2 == 0){
            // fmt.Println("splitting:", num)
            //trims leading zeroes
            firstNum, _ := strconv.Atoi(numAsStr[0:len(numAsStr)/2])
            secondNum, _ := strconv.Atoi(numAsStr[len(numAsStr)/2:])

            // fmt.Println("firstNum:", firstNum, "secondNum:", secondNum)
            return runNum(iters, i + 1, firstNum) + runNum(iters, i + 1, secondNum)
        } else {
            // fmt.Println("add to cache mul:", num, ":", i)
            cache[num] = i
            num *= 2024
        }
    } 
    
    // fmt.Println("add to cache end:", num, ":", iters)
    cache[num] = iters
    return 1
}

func remove(slice []int, ele int) []int {
    for idx, item := range slice {
        if item == ele {
            return append(slice[:idx], slice[idx+1:]...)
        }
    }
    return slice
}
