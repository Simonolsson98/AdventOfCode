package main

import (
    "fmt"
    "strings"
    "os"
    "2024/utils"
    "path/filepath"
    "time"
    "slices"
    "sort"
)

type field struct {
    xpos int
    ypos int
}

var visitedfield = []field{}
func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

	start := time.Now()

    rows := strings.Split(input, "\n")
    total := 0
    for i := 0; i < len(rows); i++ {
        row := strings.Split(rows[i], "")
        for j := 0; j < len(row); j++ {
            r, p := DFS(rows, i, j, 0, 0)
            total += (r * p)
        }
    }
    fmt.Println("Day 12 Solution (Part 1):", total)
    fmt.Println("Part 1 execution time:", time.Since(start), "\n")

    start = time.Now()
    visitedfield = []field{}

    rows = strings.Split(input, "\n")
    total = 0
    for i := 0; i < len(rows); i++ {
        row := strings.Split(rows[i], "")
        for j := 0; j < len(row); j++ {
            uniqueMap := make(map[field]bool)
            uniqueSlice := []field{}
            
            r, perim := DFSWithPerimeter(rows, i, j, 0, []field{})
            sort.Slice(perim, func(i, j int) bool {
                return perim[i].xpos < perim[j].xpos
            })


            for _, item := range perim {
                if !uniqueMap[item] {
                    uniqueMap[item] = true
                    uniqueSlice = append(uniqueSlice, item)
                } 
            }

            count = len(uniqueSlice)
            total += (r * count)
        }
    }

    fmt.Println("Day 12 Solution (Part 2):", total)
    fmt.Println("Part 2 execution time:", time.Since(start))
}

func DFS(rows []string, x int, y int, regionCount int, perimeterCount int) (int, int) {
    if slices.Contains(visitedfield, field{xpos: x, ypos: y}){
        return regionCount, perimeterCount
    }

    regionCount += 1
    actualField := strings.Split(rows[x], "")[y]

    visitedfield = append(visitedfield, field{xpos: x, ypos: y})
    if x + 1 < len(rows) && strings.Split(rows[x+1], "")[y] == actualField{
        r, p := DFS(rows, x + 1, y, regionCount, perimeterCount)
        regionCount = r; perimeterCount = p
    } else {
        perimeterCount += 1
    }
    if x - 1 >= 0 && strings.Split(rows[x-1], "")[y] == actualField {
        r, p := DFS(rows, x-1, y, regionCount, perimeterCount)
        regionCount = r; perimeterCount = p
    } else {
        perimeterCount += 1
    }
    if y + 1 < len(rows[x]) && strings.Split(rows[x], "")[y+1] == actualField {
        r, p := DFS(rows, x, y+1, regionCount, perimeterCount)
        regionCount = r; perimeterCount = p
    } else {
        perimeterCount += 1
    }
    if y - 1 >= 0  && strings.Split(rows[x], "")[y-1] == actualField {
        r, p := DFS(rows, x, y - 1, regionCount, perimeterCount)
        regionCount = r; perimeterCount = p
    } else {
        perimeterCount += 1
    }

    return regionCount, perimeterCount
}

func DFSWithPerimeter(rows []string, x int, y int, regionCount int, perimeterSlice []field) (int, []field) {
    if slices.Contains(visitedfield, field{xpos: x, ypos: y}){
        return regionCount, perimeterSlice
    }

    regionCount += 1
    actualField := strings.Split(rows[x], "")[y]

    visitedfield = append(visitedfield, field{xpos: x, ypos: y})
    if x + 1 < len(rows) && strings.Split(rows[x+1], "")[y] == actualField{
        r, p := DFSWithPerimeter(rows, x + 1, y, regionCount, perimeterSlice)
        regionCount = r; perimeterSlice = p
    } else {
        perimeterSlice = append(perimeterSlice, field{xpos: x + 1, ypos: y})
    }
    if x - 1 >= 0 && strings.Split(rows[x-1], "")[y] == actualField {
        r, p := DFSWithPerimeter(rows, x-1, y, regionCount, perimeterSlice)
        regionCount = r; perimeterSlice = p
    } else {
        perimeterSlice = append(perimeterSlice, field{xpos: x - 1, ypos: y})
    }
    if y + 1 < len(rows[x]) && strings.Split(rows[x], "")[y+1] == actualField {
        r, p := DFSWithPerimeter(rows, x, y+1, regionCount, perimeterSlice)
        regionCount = r; perimeterSlice = p
    } else {
        perimeterSlice = append(perimeterSlice, field{xpos: x, ypos: y + 1})
    }
    if y - 1 >= 0  && strings.Split(rows[x], "")[y-1] == actualField {
        r, p := DFSWithPerimeter(rows, x, y - 1, regionCount, perimeterSlice)
        regionCount = r; perimeterSlice = p
    } else {
        perimeterSlice = append(perimeterSlice, field{xpos: x, ypos: y - 1})
    }

    return regionCount, perimeterSlice
}
