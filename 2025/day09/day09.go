package main

import (
	"fmt"
	"os"
	"path/filepath"
	"strconv"
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

	start := time.Now()
	result := part1(input)
	elapsed := time.Since(start)
	fmt.Println("Day 9 Solution (Part 1):", result)
	fmt.Printf("Part 1 execution time: %.2fµs\n", float64(elapsed.Nanoseconds())/1000.0)

	start = time.Now()
	result = part2(input)
	elapsed = time.Since(start)
	fmt.Println("Day 9 Solution (Part 2):", result)
	fmt.Printf("Part 2 execution time: %.2fµs\n", float64(elapsed.Nanoseconds())/1000.0)
}

func part1(input string) int {
	max := 0
	for _, line := range strings.Split(strings.TrimSpace(input), "\n") {
		for _, line2 := range strings.Split(strings.TrimSpace(input), "\n") {
			if line == line2 {
				continue
			}

			coords := strings.Split(line, ",")
			coords2 := strings.Split(line2, ",")
			x, _ := strconv.Atoi(coords[0])
			y, _ := strconv.Atoi(coords[1])
			x2, _ := strconv.Atoi(coords2[0])
			y2, _ := strconv.Atoi(coords2[1])

			xdiff := x - x2
			ydiff := y - y2
			if xdiff < 0 {
				xdiff = -xdiff
			}
			if ydiff < 0 {
				ydiff = -ydiff
			}
			if (xdiff+1)*(ydiff+1) > max {
				max = (xdiff + 1) * (ydiff + 1)
			}
		}
	}
	return max
}

func part2(input string) int {

	return 0
}
