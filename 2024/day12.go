package main

import (
    "fmt"
    "strings"
    "os"
    "2024/utils"
    "path/filepath"
    "time"
    "slices"
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
            r, corners := DFSWithPerimeter(rows, i, j, 0, 0)

            fmt.Println(r, corners * 2)
            total += (r * corners * 2)
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

func DFSWithPerimeter(rows []string, x int, y int, regionCount int, corners int) (int, int) {
    if slices.Contains(visitedfield, field{xpos: x, ypos: y}){
        return regionCount, corners
    }

    regionCount += 1
    actualField := strings.Split(rows[x], "")[y]

    east := false
    west := false
    north := false
    south := false
    visitedfield = append(visitedfield, field{xpos: x, ypos: y})
    if x + 1 < len(rows) && strings.Split(rows[x+1], "")[y] == actualField{
        south = true
        r, core := DFSWithPerimeter(rows, x + 1, y, regionCount, corners)
        regionCount = r
        corners = core
    } 
    if x - 1 >= 0 && strings.Split(rows[x-1], "")[y] == actualField {
        north = true
        r, core := DFSWithPerimeter(rows, x-1, y, regionCount, corners)
        regionCount = r
        corners = core
    } 
    if y + 1 < len(rows[x]) && strings.Split(rows[x], "")[y+1] == actualField {
        east = true
        r, core := DFSWithPerimeter(rows, x, y+1, regionCount, corners)
        regionCount = r
        corners = core
    } 
    if y - 1 >= 0  && strings.Split(rows[x], "")[y-1] == actualField {
        west = true
        r, core := DFSWithPerimeter(rows, x, y - 1, regionCount, corners)
        regionCount = r
        corners = core
    }

    if  (!west && !north && !south && east) || 
        (!west && !north && south && !east) || 
        (!west && north && !south && !east) || 
        (west && !north && !south && !east) {
        corners += 1
        fmt.Println("tripl:", west, north, east, south, x, y)
    } else if 
        ((west && north) || 
        (north && east) || 
        (east && south) || 
        (south && west)) {
        fmt.Println("wut:", west, north, east, south, x, y)
        corners += 1
    } else if !west && !east && !north && !south {
        corners += 2
    }

    return regionCount, corners
}
