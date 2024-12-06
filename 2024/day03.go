package main

import (
    "fmt"
    "strings"
    "os"
    "2024/utils"
    "regexp"
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
    sum := part1(input)
    fmt.Println("Day 3 Solution (Part 1):", sum)
    fmt.Println("Part 1 execution time:", time.Since(start), "\n")

    start = time.Now()
    sum2 := part2(input)
    fmt.Println("Day 3 Solution (Part 2):", sum2)
    fmt.Println("Part 2 execution time:", time.Since(start))
}

func part1(input string) (result int) {
    var sum int;
    for _, match := range regexp.MustCompile(`mul\((\d{1,3}),(\d{1,3})\)`).FindAllStringSubmatch(input, -1) {
        fst, _ := strconv.Atoi(match[1])
        snd, _ := strconv.Atoi(match[2])

        sum += (fst * snd)
    }

    return sum
}

func part2(input string) (result int) {
    var sum int;
    var include bool = true;
    for _, match := range regexp.MustCompile(`mul\(\d{1,3},\d{1,3}\)|do(?:n't)?\(\)`).FindAllString(input, -1) {
        if match == "do()" {
            include = true
        } else if match == "don't()" {
            include = false
        } else if include {
            for _, nums := range regexp.MustCompile(`\d{1,3},\d{1,3}`).FindAllString(match, -1) {
                val := strings.Split(nums, ",")
                fst, _ := strconv.Atoi(val[0])
                snd, _ := strconv.Atoi(val[1])

                sum += (fst * snd)
            }
        }
    }

    return sum
}
