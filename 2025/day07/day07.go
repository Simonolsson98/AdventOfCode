package main

import (
	"fmt"
	"os"
	"path/filepath"
	"slices"
	"strings"
	"time"

	"github.com/simonolsson98/adventofcode/utils"
)

type pos struct {
    x int
    y int
}

var visited []pos = []pos{}
var totalSplits int = 0
func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

    var startingPos pos
    var grid [][]rune
    startingPosFound := false
	for _, line := range strings.Split(input, "\n") {
        if !startingPosFound {
            for j, char := range line {
                if char == 'S' {
                    startingPos = pos{x: len(grid), y: j}
                    startingPosFound = true
                }
            }
        }
		grid = append(grid, []rune(line))
	}
    visited = []pos{startingPos}
    
    start := time.Now()
    part1(grid, startingPos.x, startingPos.y)
    fmt.Println("Day 7 Solution (Part 1):", totalSplits)
    fmt.Println("Part 1 execution time:", time.Since(start))

    start = time.Now()
    result := part2(grid, startingPos.x, startingPos.y)
    fmt.Println("Day 7 Solution (Part 2):", result)
    fmt.Println("Part 2 execution time:", time.Since(start))
}

func part1(grid [][]rune, startX int, startY int) {
    x := startX + 1
    y := startY
    currentPos := pos{x, y}
    if slices.Contains(visited, currentPos) {
        return
    }
    visited = append(visited, pos{x, y})
    if x > len(grid) - 1 {
        return
    }
    
    if grid[x][y] == '.'{
        part1(grid, x, y)
    } else {
        totalSplits++
        part1(grid, x, y - 1)
        part1(grid, x, y + 1)
    }
}

var memoizedRoutes = make(map[pos]int)
func part2(grid [][]rune, startX int, startY int) int {
    x := startX + 1
    y := startY

    // hit the bottom => return 1 valid route
    if x > len(grid) - 1 {
        return 1
    }

    // cache hit, wooo
    if storedNumOfRoutes, exists := memoizedRoutes[pos{x, y}]; exists {
        return storedNumOfRoutes
    }
    
    if grid[x][y] == '.'{
        return part2(grid, x, y)
    } else {
        // split route in two
        result := part2(grid, x, y - 1) + part2(grid, x, y + 1)

        // store in cache
        memoizedRoutes[pos{x, y}] = result
        return result
    }
}