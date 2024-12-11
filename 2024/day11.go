package main

import (
    "fmt"
    "strings"
    "os"
    "2024/utils"
    "strconv"
    "path/filepath"
    "time"
    "slices"
    "reflect"
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
func test(iters int, nums []string) (res int){
    prevnums := nums
    for i := 0; i < iters; i++ {
        fmt.Println(i)
        for j := 0; j < len(nums); j++ {
            numAsStr := nums[j]
            if numAsStr == "0" {
                nums[j] = "1"
            } else if (len(numAsStr) % 2 == 0){
                //trims leading zeroes
                firstNum, _ := strconv.Atoi(numAsStr[0:len(numAsStr)/2])
                secondNum, _ := strconv.Atoi(numAsStr[len(numAsStr)/2:])
                
                nums[j] = strconv.Itoa(firstNum)
                nums = slices.Insert(nums, j + 1, strconv.Itoa(secondNum))
                j += 1
            } else {
                parsedNum, _ := strconv.Atoi(nums[j])
                parsedNum *= 2024
                nums[j] = strconv.Itoa(parsedNum)
            }
        }    

        if reflect.DeepEqual(nums, prevnums) {
            break
        }
        prevnums = nums
    }

    return len(nums)
}
