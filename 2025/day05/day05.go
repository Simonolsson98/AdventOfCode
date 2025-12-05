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
	fmt.Println("Day 5 Solution (Part 1):", result)
	fmt.Println("Part 1 execution time:", time.Since(start))

	start = time.Now()
	result = part2(input)
	fmt.Println("Day 5 Solution (Part 2):", result)
	fmt.Println("Part 2 execution time:", time.Since(start))
}

func part1(input string) int {
	foo := strings.Split(input, "\n\n")
	ranges := foo[0]
	ingredients := foo[1]
	validIngredients := 0
	for _, ingredient := range strings.Split(ingredients, "\n") {
		ingredient, _ := strconv.Atoi(ingredient)
		for _, r := range strings.Split(ranges, "\n") {
			parts := strings.Split(r, "-")
			minRange, _ := strconv.Atoi(parts[0])
			maxRange, _ := strconv.Atoi(parts[1])
			if ingredient >= minRange && ingredient <= maxRange {
				validIngredients++
				break
			}
		}
	}
	return validIngredients
}

func part2(input string) int {

	return 0
}
