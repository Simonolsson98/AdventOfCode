package main

import (
	"fmt"
	"os"
	"path/filepath"
	"strings"
	"time"

	"github.com/simonolsson98/adventofcode/utils"
)

func main() {
	inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
	input, err := utils.ReadInput(inputFile)
	if err != nil {
		fmt.Println("Error reading input:", err)
		return
	}

	var grid [][]rune
	for _, line := range strings.Split(input, "\n") {
		grid = append(grid, []rune(line))
	}

	start := time.Now()
	result := part1(grid)
	elapsed := time.Since(start)
	fmt.Println("Day 4 Solution (Part 1):", result)
	fmt.Printf("Part 1 execution time: %.2fµs\n", float64(elapsed.Nanoseconds())/1000.0)

	start = time.Now()
	result = part2(grid)
	elapsed = time.Since(start)
	fmt.Println("Day 4 Solution (Part 2):", result)
	fmt.Printf("Part 2 execution time: %.2fµs\n", float64(elapsed.Nanoseconds())/1000.0)
}

func part1(grid [][]rune) int {
	var sum int
	for i, row := range grid {
		for j, char := range row {
			var neighbours int = 0
			if char == '.' {
				continue
			}

			neighbours = countNeighbours(grid, i, j)

			if neighbours < 4 {
				sum += 1
			}
		}
	}
	return sum
}

func part2(grid [][]rune) int {
	var totalRemovedRolls int = 0
	var rollWasRemoved bool = true
	for rollWasRemoved {
		rollWasRemoved = false

		for i, row := range grid {
			for j, char := range row {
				var neighbours int = 0
				if char == '.' {
					continue
				}

				neighbours = countNeighbours(grid, i, j)

				if neighbours < 4 {
					totalRemovedRolls++
					grid[i][j] = '.'
					rollWasRemoved = true
				}
			}
		}
	}

	return totalRemovedRolls
}

func countNeighbours(grid [][]rune, i, j int) int {
	var neighbours int = 0
	row := grid[i]
	if i-1 >= 0 { // up
		if grid[i-1][j] == '@' {
			neighbours++
		}
		if j-1 >= 0 && grid[i-1][j-1] == '@' {
			neighbours++
		}
		if j+1 < len(row) && grid[i-1][j+1] == '@' {
			neighbours++
		}
	}
	if i+1 < len(grid) { // down
		if grid[i+1][j] == '@' {
			neighbours++
		}
		if j-1 >= 0 && grid[i+1][j-1] == '@' {
			neighbours++
		}
		if j+1 < len(row) && grid[i+1][j+1] == '@' {
			neighbours++
		}
	}
	if j-1 >= 0 && grid[i][j-1] == '@' { // left
		neighbours++
	}
	if j+1 < len(row) && grid[i][j+1] == '@' { // right
		neighbours++
	}

	return neighbours
}
