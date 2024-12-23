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

func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

    yes := make(map[string][]string, 0)

    for _, line := range strings.Split(input, "\n") {
        split := strings.Split(line, "-")
        _, exists := yes[split[0]]
        _, exists2 := yes[split[1]]
        if exists {
            yes[split[0]] = append(yes[split[0]], split[1])
        } else {
            yes[split[0]] = []string{split[1]}
        }
        if exists2 {
            yes[split[1]] = append(yes[split[1]], split[0])
        } else {
            yes[split[1]] = []string{split[0]}
        }
    }

    start := time.Now()
    count := part1(yes)
    

    fmt.Println("Day 23 Solution (Part 1):", count/6)
    fmt.Println("Part 1 execution time:", time.Since(start), "\n")

    start = time.Now()
    var mostConnectedComputers []string
    for key, val := range yes{
        stuff := []string{}
        for _, asd := range val {
            if !slices.Contains(stuff, key){
                stuff = append(stuff, key)
            }
            for _, otherVal := range yes[asd] {
                if slices.Contains(val, otherVal) {
                    if !slices.Contains(stuff, asd){
                        willAppend := true
                        for _, inStuff := range stuff {
                            if !slices.Contains(yes[inStuff], asd){
                                willAppend = false
                                break
                            }
                        }
                        if willAppend{
                            stuff = append(stuff, asd)
                        }
                    }
                }
            }
        }
        
        if len(stuff) > len(mostConnectedComputers){
            mostConnectedComputers = stuff
        }   
    }

    slices.Sort(mostConnectedComputers)
    fmt.Println("Day 23 Solution (Part 2):", strings.Join(mostConnectedComputers, ","))
    fmt.Println("Part 2 execution time:", time.Since(start))
}

func part1(yes map[string][]string) (int){
    var count int
    for key, val := range yes {
        for i := 0; i < len(val); i++ {
            for j := 0; j < len(val); j++ {
                if i == j {
                    continue
                }

                if (strings.HasPrefix(key, "t") || strings.HasPrefix(val[i], "t") || strings.HasPrefix(val[j], "t")) && 
                    (slices.Contains(yes[val[i]], val[j]) || slices.Contains(yes[val[j]], val[i])) {
                    count++
                }
            }
        }
    }

    return count
}