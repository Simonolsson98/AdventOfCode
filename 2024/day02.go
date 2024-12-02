package main

import (
    "fmt"
    "strings"
    "os"
    "2024/utils"
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
    
    safe := 0
    safe2 := 0
    for _, line := range strings.Split(strings.TrimSpace(input), "\n") {
        safetemp := part1(line)
        safe += safetemp

        safetemp2 := part2(line, false)
        safe2 += safetemp2
    }

    fmt.Println("Day 1 Solution (Part 1):", safe)
    fmt.Println("Day 1 Solution (Part 2):", safe2)
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
        return 0 // Unsafe case, directly return 0 for safety
    }

    for i := 1; i < len(fields)-1; i++ {
        ele1, _ := strconv.Atoi(fields[i])
        ele2, _ := strconv.Atoi(fields[i+1])
        if increasing && (ele1-ele2 >= 0 || ele1-ele2 < -3) {
            return 0 // Unsafe case, directly return 0 for safety
        }
        if !increasing && (ele1-ele2 <= 0 || ele1-ele2 > 3) {
            return 0 // Unsafe case, directly return 0 for safety
        }
    }

    return 1 // If none of the unsafe conditions are met, it's safe
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

        safe := part2(strings.Join(excludeFirstElement, " "), true)
        safe2 := part2(strings.Join(excludeSecondElement, " "), true)

        if safe == 1 || safe2 == 1 {
            return 1
        } else {
            return 0
        }
    } else {
        return 0
    }

    for i := 1; i < len(fields)-1; i++ {
        ele1, _ := strconv.Atoi(fields[i])
        ele2, _ := strconv.Atoi(fields[i+1])
        if increasing && (ele1-ele2 >= 0 || ele1-ele2 < -3) {
            if !alreadyFailedOnce {
                excludePrevElement := append(append([]string{}, fields[:i-1]...), fields[i:]...)
                excludeCurrElement := append(append([]string{}, fields[:i]...), fields[i+1:]...)
                excludeNextElement := append(append([]string{}, fields[:i+1]...), fields[i+2:]...)

                safe := part2(strings.Join(excludePrevElement, " "), true)
                safe2 := part2(strings.Join(excludeCurrElement, " "), true)
                safe3 := part2(strings.Join(excludeNextElement, " "), true)

                if safe == 1 || safe2 == 1 || safe3 == 1 {
                    return 1
                } else {
                    return 0
                }
            } else {
                return 0
            }
        }
        if !increasing && (ele1-ele2 <= 0 || ele1-ele2 > 3) {
            if !alreadyFailedOnce {
                excludePrevElement := append(append([]string{}, fields[:i-1]...), fields[i:]...)
                excludeCurrElement := append(append([]string{}, fields[:i]...), fields[i+1:]...)
                excludeNextElement := append(append([]string{}, fields[:i+1]...), fields[i+2:]...)

                prevElementSafe := part2(strings.Join(excludePrevElement, " "), true)
                currentElementSafe := part2(strings.Join(excludeCurrElement, " "), true)
                nextElementSafe := part2(strings.Join(excludeNextElement, " "), true)

                if prevElementSafe == 1 || currentElementSafe == 1 || nextElementSafe == 1 {
                    return 1
                } else {
                    return 0
                }
            } else {
                return 0
            }
        }
    }

    return 1
}

