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

    unsafe := 0
    safe := 0
    fmt.Println(input)

    for _, line := range strings.Split(strings.TrimSpace(input), "\n") {
        fields := strings.Fields(line)

        fst, _ := strconv.Atoi(fields[0])
        snd, _ := strconv.Atoi(fields[1])
        if fst - snd > 2 || fst - snd < -2 {
            unsafe += 1
            continue
        }

        if snd > fst{
            temp := snd
            snd = fst
            fst = temp
        }

        // FIXXXX
        increasing := false
        if fst - snd <= 3 && fst - snd > 0 {
            increasing = false
            fmt.Println("decreasing: first 2 eles: ", fst, snd)
        } else if fst - snd <= -3 && fst - snd < 0 {
            increasing = true
            fmt.Println("increasing: first 2 eles: ", fst, snd)
        } else {
            fmt.Println("unsafe: first 2 eles: ", fst, snd)
            unsafe += 1
            continue
        }

        breakOuter := false
        for i := 1; i < len(fields) - 1; i++ {
            ele1, _ := strconv.Atoi(fields[0])
            ele2, _ := strconv.Atoi(fields[1])
            if increasing && ele1 - ele2 <= 0 {
                fmt.Println("unsafe because ele1 - ele2 <= 0: ", ele1, ele2)
                unsafe += 1
                breakOuter = true
                break
            }
            if !increasing && ele1 - ele2 >= 0 {
                fmt.Println("unsafe because ele1 - ele2 >= 0: ", ele1, ele2)
                unsafe += 1
                breakOuter = true
                break
            }
        }

        if breakOuter{
            continue;
        }

        safe += 1
    }

    fmt.Println("safe: ", safe)
    fmt.Println("unsafe: ", unsafe)
}