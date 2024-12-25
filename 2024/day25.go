package main

import (
    "fmt"
    "strings"
    "os"
    "2024/utils"
    //"strconv"
    "path/filepath"
    "time"
    "slices"
)

type keyOrLock struct {
    col1 int
    col2 int
    col3 int
    col4 int
    col5 int
}

var totalLength int

func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

    start := time.Now()

    var keys []keyOrLock
    var locks []keyOrLock
    for _, in := range strings.Split(input, "\n\n") {
        var current keyOrLock
        checkedYs := []int{}
        rows := strings.Split(in, "\n")
        totalLength = len(rows)
        if strings.Split(rows[0], "")[0] == "#"{ // lock
            for x, row := range rows {
                for y, item := range strings.Split(row, "") {
                    if item == "#" || slices.Contains(checkedYs, y){
                        continue
                    }
                    checkedYs = append(checkedYs, y)

                    switch y {
                        case 0:
                            current.col1 = x - 1
                        case 1:
                            current.col2 = x - 1
                        case 2:
                            current.col3 = x - 1
                        case 3:
                            current.col4 = x - 1
                        case 4:
                            current.col5 = x - 1
                        default:
                            panic("should not be here")
                    }
                }
            }

            locks = append(locks, current)
        } else { // key
            checkedYs := []int{}
            for i := len(rows) - 1; i >= 0; i-- {
                row := rows[i]
                for y, item := range strings.Split(row, "") {
                    if item == "#" || slices.Contains(checkedYs, y){
                        continue
                    }
                    checkedYs = append(checkedYs, y)

                    switch y {
                        case 0:
                            current.col1 = len(rows) - i - 2
                        case 1:
                            current.col2 = len(rows) - i - 2
                        case 2:
                            current.col3 = len(rows) - i - 2
                        case 3:
                            current.col4 = len(rows) - i - 2
                        case 4:
                            current.col5 = len(rows) - i - 2
                        default:
                            panic("should not be here")
                    }
                }
            }
            
            keys = append(keys, current)
        }
    }

    fmt.Println("Day 25 Solution (Part 1):", countKeyLockMatches(keys, locks))
    fmt.Println("Part 1 execution time:", time.Since(start), "\n")

    start = time.Now()
    // exec part 2
    fmt.Println("Day 25 Solution (Part 2):")
    fmt.Println("Part 2 execution time:", time.Since(start))
}

func countKeyLockMatches(keys []keyOrLock, locks []keyOrLock) (int) {
    matches := 0   
    for _, key := range keys {
        for _, lock := range locks {
            if 
            lock.col1 + key.col1 >= totalLength - 1 ||
            lock.col2 + key.col2 >= totalLength - 1 ||
            lock.col3 + key.col3 >= totalLength - 1 ||
            lock.col4 + key.col4 >= totalLength - 1 ||
            lock.col5 + key.col5 >= totalLength - 1 {
                continue // overlap
            } else {
                matches++
            }
        }
    }

    return matches
}