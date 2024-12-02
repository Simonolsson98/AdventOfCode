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
    unsafe := 0
    safe2 := 0
    unsafe2 := 0
    for _, line := range strings.Split(strings.TrimSpace(input), "\n") {
        safetemp, unsafetemp := part1(line)
        safe += safetemp
        unsafe += unsafetemp 

        safetemp2, unsafetemp2 := part2(line, false)
        safe2 += safetemp2
        unsafe2 += unsafetemp2
    }

    fmt.Println("Day 1 Solution (Part 1):", safe)
    fmt.Println("Day 1 Solution (Part 2):", safe2)
}

func part1(line string) (safe, unsafe int) {
    fields := strings.Fields(line)
    fst, _ := strconv.Atoi(fields[0])
    snd, _ := strconv.Atoi(fields[1])

    var increasing bool
    if fst - snd <= 3 && fst - snd > 0 {
        increasing = false
    } else if fst-snd >= -3 && fst-snd < 0 {
        increasing = true
    } else {
        return 0, 1
    }

    for i := 1; i < len(fields)-1; i++ {
        ele1, _ := strconv.Atoi(fields[i])
        ele2, _ := strconv.Atoi(fields[i+1])
        if increasing && (ele1-ele2 >= 0 || ele1-ele2 < -3) {
            return 0, 1
        }
        if !increasing && (ele1-ele2 <= 0 || ele1-ele2 > 3) {
            return 0, 1
        }
    }
    
    return 1, 0
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
                temp1 := append(append([]string{}, fields[:i-1]...), fields[i:]...)
                temp2 := append(append([]string{}, fields[:i]...), fields[i+1:]...)
                temp3 := append(append([]string{}, fields[:i+1]...), fields[i+2:]...)

                safe := part2(strings.Join(temp1, " "), true)
                safe2 := part2(strings.Join(temp2, " "), true)
                safe3 := part2(strings.Join(temp3, " "), true)

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
                excludingPrevElement := append(append([]string{}, fields[:i-1]...), fields[i:]...)
                excludingCurrElement := append(append([]string{}, fields[:i]...), fields[i+1:]...)
                excludingNextElement := append(append([]string{}, fields[:i+1]...), fields[i+2:]...)

                prevElementSafe := part2(strings.Join(excludingPrevElement, " "), true)
                currentElementSafe := part2(strings.Join(excludingCurrElement, " "), true)
                nextElementSafe := part2(strings.Join(excludingNextElement, " "), true)

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
