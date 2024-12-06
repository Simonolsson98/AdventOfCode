package main

import (
    "fmt"
    "2024/utils"
    "os"
    "path/filepath"
    "sort"
    "strconv"
    "strings"
    "time"
)

func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

    list1, list2, err := parseInput(input)
    if err != nil {
        fmt.Println("Error parsing input:", err)
        return
    }

    start := time.Now()
    fmt.Println("Day 1 Solution (Part 1):", part1(list1, list2))
    fmt.Println("Part 1 execution time:", time.Since(start), "\n")
    start = time.Now()
    fmt.Println("Day 1 Solution (Part 2):", part2(list1, list2))
    fmt.Println("Part 2 execution time:", time.Since(start))
}

func parseInput(input string) ([]int, []int, error) {
    list1 := []int{}
    list2 := []int{}
    for _, line := range strings.Split(strings.TrimSpace(input), "\n") {
        fields := strings.Fields(line)
        if len(fields) < 2 {
            return nil, nil, fmt.Errorf("invalid input line: %s", line)
        }
        fst, err1 := strconv.Atoi(fields[0])
        snd, err2 := strconv.Atoi(fields[1])
        if err1 != nil || err2 != nil {
            return nil, nil, fmt.Errorf("failed to parse integers: %v, %v", err1, err2)
        }
        list1 = append(list1, fst)
        list2 = append(list2, snd)
    }
    return list1, list2, nil
}

func part1(list1, list2 []int) int {
    sort.Ints(list1)
    sort.Ints(list2)

    diff := 0
    for i := 0; i < len(list1); i++ {
        res := list1[i] - list2[i]
        if res < 0 {
            res = -res
        }
        diff += res
    }
    return diff
}

func part2(list1, list2 []int) int {
    counter := map[int]int{} // Use a map for counting occurrences in list2
    for _, val := range list2 {
        counter[val]++
    }

    total := 0
    for _, val := range list1 {
        total += counter[val] * val
    }
    return total
}