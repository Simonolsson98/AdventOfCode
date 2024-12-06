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
    var safe int
    var safe2 int
    for _, line := range strings.Split(strings.TrimSpace(input), "\n") {
        safe += part1(line)
        safe2 += part2(line, false)
    }

    fmt.Println("Day 1 Solution (Part 1):", safe)
    fmt.Println("Day 1 Solution (Part 2):", safe2)
    fmt.Println("Part 1 + 2 execution time:", time.Since(start).Microseconds(), "microseconds")
}

func part1(line string) (safe int) {
    fields := strings.Fields(line)
    fst, _ := strconv.Atoi(fields[0])
    snd, _ := strconv.Atoi(fields[1])

    var increasing bool
    if fst-snd <= 3 && fst-snd > 0 {
        increasing = false
    } else if fst-snd >= -3 && fst-snd < 0 {
        increasing = true
    } else {
        return 0
    }

    for i := 1; i < len(fields)-1; i++ {
        ele1, _ := strconv.Atoi(fields[i])
        ele2, _ := strconv.Atoi(fields[i+1])
        if ( increasing && (ele1-ele2 >= 0 || ele1-ele2 < -3)) || 
           (!increasing && (ele1-ele2 <= 0 || ele1-ele2 > 3)) {
            return 0
        }
    }

    return 1
}

func part2(line string, alreadyFailedOnce bool) (safe int) {
    fields := strings.Fields(line)
    fst, _ := strconv.Atoi(fields[0])
    snd, _ := strconv.Atoi(fields[1])

    var increasing bool
    if fst-snd <= 3 && fst-snd > 0 {
        increasing = false
    } else if fst-snd >= -3 && fst-snd < 0 {
        increasing = true
    } else if !alreadyFailedOnce {
        excludeFirstElement := append(append([]string{}, fields[:0]...), fields[1:]...)
        excludeSecondElement := append(append([]string{}, fields[:1]...), fields[2:]...)

        if safe := part2(strings.Join(excludeFirstElement, " "), true); safe == 1 {
            return 1
        } else if safe := part2(strings.Join(excludeSecondElement, " "), true); safe == 1 {
            return 1
        }
        return 0
    } else {
        return 0
    }

    for i := 1; i < len(fields)-1; i++ {
        ele1, _ := strconv.Atoi(fields[i])
        ele2, _ := strconv.Atoi(fields[i+1])
        if increasing && (ele1-ele2 >= 0 || ele1-ele2 < -3) {
            if alreadyFailedOnce {
                return 0
            }

            excludePrevElement := append(append([]string{}, fields[:i-1]...), fields[i:]...)
            excludeCurrElement := append(append([]string{}, fields[:i]...), fields[i+1:]...)
            excludeNextElement := append(append([]string{}, fields[:i+1]...), fields[i+2:]...)
            safeExcludingPrev := part2(strings.Join(excludePrevElement, " "), true)
            safeExcludingCurr := part2(strings.Join(excludeCurrElement, " "), true)
            safeExcludingNext := part2(strings.Join(excludeNextElement, " "), true)

            if safeExcludingPrev == 1 || safeExcludingCurr == 1 || safeExcludingNext == 1 {
                return 1
            } 
            return 0
        }
        if !increasing && (ele1-ele2 <= 0 || ele1-ele2 > 3) {
            if alreadyFailedOnce{
                return 0
            }

            excludePrevElement := append(append([]string{}, fields[:i-1]...), fields[i:]...)
            excludeCurrElement := append(append([]string{}, fields[:i]...), fields[i+1:]...)
            excludeNextElement := append(append([]string{}, fields[:i+1]...), fields[i+2:]...)
            safeExcludingPrev := part2(strings.Join(excludePrevElement, " "), true)
            safeExcludingCurr := part2(strings.Join(excludeCurrElement, " "), true)
            safeExcludingNext := part2(strings.Join(excludeNextElement, " "), true)

            if safeExcludingPrev == 1 || safeExcludingCurr == 1 || safeExcludingNext == 1 {
                return 1
            }
            return 0
        }
    }

    return 1
}

