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

type priceChangeSeq struct{
    a int
    b int
    c int
    d int
}

var (
    iterations int = 2000
    result int
)

func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

    nums := strings.Split(input, "\n")

    start := time.Now()
    fmt.Println("Day 22 Solution (Part 1):", part1(nums))
    fmt.Println("Part 1 execution time:", time.Since(start))

    start = time.Now()
    fmt.Println("Day 22 Solution (Part 2):", part2(nums))
    fmt.Println("Part 2 execution time:", time.Since(start))
}

func part1(nums []string) (int){
    for _, num := range nums {
        secretNum, _ := strconv.Atoi(num)
        for i := 0; i < iterations; i++ {
            secretNum = calcSecretNum(secretNum)
        }

        result += secretNum
    }

    return result
}

func part2(nums []string) (int){
    priceForPriceChangeSeq := make(map[priceChangeSeq]int, 0)
    currentPriceChangeSeq := priceChangeSeq{}
    for _, num := range nums {
        secretNum, _ := strconv.Atoi(num)
        prevPrice, _ := strconv.Atoi(strings.Split(num, "")[len(num) - 1])

        priceChangeSeqUsage := make(map[priceChangeSeq]bool, 0)
        for i := 0; i < iterations; i++ {
            secretNum = calcSecretNum(secretNum)

            secNumAsStr := strings.Split(strconv.Itoa(secretNum), "")
            price, _ := strconv.Atoi(secNumAsStr[len(secNumAsStr) - 1])
            
            currentPriceChangeSeq = priceChangeSeq{currentPriceChangeSeq.b, currentPriceChangeSeq.c, currentPriceChangeSeq.d, price - prevPrice}

            if i >= 3 && i <= iterations - 2{
                if !priceChangeSeqUsage[currentPriceChangeSeq] {
                    priceForPriceChangeSeq[currentPriceChangeSeq] += price
                    priceChangeSeqUsage[currentPriceChangeSeq] = true
                }
            }

            prevPrice = price
        }

        result += secretNum
    }

    maxVal := 0
    for _, val := range priceForPriceChangeSeq {
        if val > maxVal {
            maxVal = val
        }
    }

    return maxVal
}

func calcSecretNum(secretNum int) (int){
    subResult := secretNum * 64
    secretNum = subResult ^ secretNum
    secretNum = secretNum % 16777216

    subResult = secretNum / 32
    secretNum = subResult ^ secretNum
    secretNum = secretNum % 16777216

    subResult = secretNum * 2048
    secretNum = subResult ^ secretNum
    secretNum = secretNum % 16777216

    return secretNum
}