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
    for _, line := range strings.Split(strings.TrimSpace(input), "\n") {
        safetemp, unsafetemp := part1(line)
        safe += safetemp
        unsafe += unsafetemp 
    }
    fmt.Println("safe: ", safe)
    fmt.Println("unsafe: ", unsafe)
}

func part1(line string) (safe, unsafe int) {
    fields := strings.Fields(line)
    fst, _ := strconv.Atoi(fields[0])
    snd, _ := strconv.Atoi(fields[1])

    var increasing bool
    if fst - snd <= 3 && fst - snd > 0 {
        increasing = false
        fmt.Println("decreasing: first 2 elems: ", fst, snd)
    } else if fst-snd >= -3 && fst-snd < 0 {
        increasing = true
        fmt.Println("increasing: first 2 elems: ", fst, snd)
    } else {
        fmt.Println("unsafe: first 2 elems: ", fst, snd)
        return 0, 1
    }

    for i := 1; i < len(fields)-1; i++ {
        ele1, _ := strconv.Atoi(fields[i])
        ele2, _ := strconv.Atoi(fields[i+1])
        if increasing && (ele1-ele2 >= 0 || ele1-ele2 < -3) {
            fmt.Println("unsafe because ele1 - ele2 >= 0 or ele1 - ele2 < -3: ", ele1, ele2)
            return 0, 1
        }
        if !increasing && (ele1-ele2 <= 0 || ele1-ele2 > 3) {
            fmt.Println("unsafe because ele1 - ele2 <= 0 or ele1 - ele2 > 3: ", ele1, ele2)
            return 0, 1
        }
    }
    
    return 1, 0
}