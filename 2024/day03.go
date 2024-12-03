package main

import (
    "fmt"
    "strings"
    "os"
    "2024/utils"
    "regexp"
    "strconv"
    "path/filepath"
)

func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

    sum := part1(input)
    sum2 := part2(input)

    fmt.Println("Day 3 Solution (Part 1):", sum)
    fmt.Println("Day 3 Solution (Part 2):", sum2)
}

func part1(input string) (result int) {
    re, err := regexp.Compile(`mul\(\d{1,3},\d{1,3}\)`)
    if err != nil {
        fmt.Println("wtf")
        return
    }

    var sum int;
    for _, match := range re.FindAllString(input, -1) {
        for _, nums := range regexp.MustCompile(`\d{1,3},\d{1,3}`).FindAllString(match, -1) {
            val := strings.Split(nums, ",")
            fst, _ := strconv.Atoi(val[0])
            snd, _ := strconv.Atoi(val[1])

            sum += (fst * snd)
        }
    }

    return sum
}

func part2(input string) (result int) {
    re, err := regexp.Compile(`mul\(\d{1,3},\d{1,3}\)|do(?:n't)?\(\)`)
    if err != nil {
        fmt.Println("wtf")
        return
    }

    var sum int;
    fmt.Println(re.FindAllString(input, -1))
    var include bool = true;
    for _, match := range re.FindAllString(input, -1) {
        if match == "do()" {
            include = true
            continue
        } else if match == "don't()" {
            include = false
            continue
        }

        if include {
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
