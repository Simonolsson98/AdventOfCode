package main

import (
    "fmt"
    "strings"
    "os"
    "github.com/simonolsson98/adventofcode/utils"
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

    connections := parseInput(input)

    start := time.Now()
    count := part1(connections)
    fmt.Println("Day 23 Solution (Part 1):", count)
    fmt.Println("Part 1 execution time:", time.Since(start))

    start = time.Now()
    mostConnectedComputers := part2(connections)
    slices.Sort(mostConnectedComputers)
    fmt.Println("Day 23 Solution (Part 2):", strings.Join(mostConnectedComputers, ","))
    fmt.Println("Part 2 execution time:", time.Since(start))
}

func part1(connections map[string][]string) (int){
    var count int
    for key, val := range connections {
        for i := 0; i < len(val); i++ {
            for j := 0; j < len(val); j++ {
                if i == j {
                    continue
                }

                if (strings.HasPrefix(key, "t") || strings.HasPrefix(val[i], "t") || strings.HasPrefix(val[j], "t")) && 
                    (slices.Contains(connections[val[i]], val[j]) || slices.Contains(connections[val[j]], val[i])) {
                    count++
                }
            }
        }
    }

    return count/6
}

func part2(connections map[string][]string) ([]string) {
    var mostConnectedComputers []string 
    for key, val := range connections{
        currentConnections := []string{}
        for _, currentComputer := range val {
            if !slices.Contains(currentConnections, key){
                currentConnections = append(currentConnections, key)
            }
            for _, otherVal := range connections[currentComputer] {
                if slices.Contains(val, otherVal) {
                    if !slices.Contains(currentConnections, currentComputer){
                        connectedToAllOthers := true
                        for _, inStuff := range currentConnections {
                            if !slices.Contains(connections[inStuff], currentComputer){
                                connectedToAllOthers = false
                                break
                            }
                        }
                        if connectedToAllOthers{
                            currentConnections = append(currentConnections, currentComputer)
                        }
                    }
                }
            }
        }
        
        if len(currentConnections) > len(mostConnectedComputers){
            mostConnectedComputers = currentConnections
        }   
    }

    return mostConnectedComputers
}

func parseInput(input string) (map[string][]string){
    connections := make(map[string][]string, 0)
    for _, line := range strings.Split(input, "\n") {
        split := strings.Split(line, "-")
        _, exists := connections[split[0]]
        _, exists2 := connections[split[1]]
        if exists {
            connections[split[0]] = append(connections[split[0]], split[1])
        } else {
            connections[split[0]] = []string{split[1]}
        }
        if exists2 {
            connections[split[1]] = append(connections[split[1]], split[0])
        } else {
            connections[split[1]] = []string{split[0]}
        }
    }
    
    return connections
}