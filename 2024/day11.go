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

type numAndIter struct {
    num int
    iter int
}
var cache = map[numAndIter]int{}

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
    cache = map[numAndIter]int{}
    fmt.Println("Day 11 Solution (Part 2):", test(25, nums))
    fmt.Println("Part 2 execution time:", time.Since(start))
}

func test(iters int, nums []string) (res int){
    total := 0
    for _, strnum := range nums {
        num, _ := strconv.Atoi(strnum)
        total += stoneBlink(iters, num)
    }

    return total
}

func stoneBlink(iters int, num int) (int){
    if iters == 0{
        return 1
    }
    _, exists := cache[numAndIter{num, iters}]
    if exists {
        return cache[numAndIter{num, iters}]
    }

    numAsStr := strconv.Itoa(num)
    nextNums := []int{}
    if num == 0{
        nextNums = append(nextNums, 1)
    } else if (len(numAsStr) % 2 == 0){
        //trims leading zeroes
        firstNum, _ := strconv.Atoi(numAsStr[0:len(numAsStr)/2])
        secondNum, _ := strconv.Atoi(numAsStr[len(numAsStr)/2:])

        nextNums = append(nextNums, firstNum)
        nextNums = append(nextNums, secondNum)
    } else {
        nextNums = append(nextNums, num * 2024)
    }

    count := 0
    for _, recNum := range nextNums {
        count += stoneBlink(iters - 1, recNum)
    }

    cache[numAndIter{num, iters}] = count
    return count
}