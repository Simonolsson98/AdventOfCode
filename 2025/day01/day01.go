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
	fmt.Println("Day 1 Solution (Part 1):", result)
	fmt.Println("Part 1 execution time:", time.Since(start))

	start = time.Now()
	result = part2(input)
	fmt.Println("Day 1 Solution (Part 2):", result)
	fmt.Println("Part 2 execution time:", time.Since(start))
}

func part1(input string) int {
	zeropointers := 0
	current := 50

	for _, line := range strings.Split(strings.TrimSpace(input), "\n") {
		rotation := line[0]
		ticksStr := line[1:]
		ticks, _ := strconv.Atoi(ticksStr)

		if rotation == 'R' {
			current = (current + ticks) % 100
		} else {
			current = (current - ticks) % 100
		}

		if current == 0 {
			zeropointers += 1
		}
	}

	return zeropointers
}

func part2(input string) int {
	zeropointers := 0
	current := 50

	for _, line := range strings.Split(strings.TrimSpace(input), "\n") {
		rotation := line[0]
		ticksStr := line[1:]
		ticks, _ := strconv.Atoi(ticksStr)

		if rotation == 'R' {
			if current+ticks >= 100 {
				zeropointers += (current + ticks) / 100
			}

			current = utils.PythonMod(current+ticks, 100)
		} else {
			newVal := (current - ticks)
			if newVal <= 0 {
				posVal := newVal * -1

				if current == 0 {
					zeropointers += (posVal / 100)
				} else {
					zeropointers += 1 + (posVal / 100)
				}
			}

			current = utils.PythonMod(current-ticks, 100)
		}
	}

	return zeropointers
}
