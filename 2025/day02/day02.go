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
	fmt.Println("Day 2 Solution (Part 1):", result)
	fmt.Println("Part 1 execution time:", time.Since(start))

	start = time.Now()
	result = part2(input)
	fmt.Println("Day 2 Solution (Part 2):", result)
	fmt.Println("Part 2 execution time:", time.Since(start))
}

func part1(input string) int {
	invalid_ids := 0
	for _, line := range strings.Split(input, ",") {
		actualRange := strings.Split(line, "-")
		first_half := actualRange[0]
		second_half := actualRange[1]

		if len(first_half) == len(second_half) && (len(first_half)%2 != 0 && len(second_half)%2 != 0) {
			continue
		}

		start, _ := strconv.Atoi(first_half)
		end, _ := strconv.Atoi(second_half)
		for i := start; i <= end; i++ {
			strRange := strconv.Itoa(i)
			if len(strRange)%2 != 0 {
				continue
			}

			if strRange[:len(strRange)/2] == strRange[len(strRange)/2:] {
				value, _ := strconv.Atoi(strRange)
				invalid_ids += value
			}
		}
	}
	return invalid_ids
}

func part2(input string) int {

	return 0
}
