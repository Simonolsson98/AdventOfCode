package main

import (
	"fmt"
	"os"
	"path/filepath"
	"sort"
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
	fmt.Println("Day 5 Solution (Part 1):", result)
	fmt.Printf("Part 1 execution time: %.2fµs\n", float64(elapsed.Nanoseconds())/1000.0)

	start = time.Now()
	result = part2(input)
	elapsed = time.Since(start)
	fmt.Println("Day 5 Solution (Part 2):", result)
	fmt.Printf("Part 2 execution time: %.2fµs\n", float64(elapsed.Nanoseconds())/1000.0)
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

type IntRange struct {
	start int
	end   int
}

func part2(input string) int {
	foo := strings.Split(input, "\n\n")
	ranges := foo[0]
	rangesList := []IntRange{}

	for _, r := range strings.Split(ranges, "\n") {
		parts := strings.Split(r, "-")
		startingIndex, _ := strconv.Atoi(parts[0])
		endingIndex, _ := strconv.Atoi(parts[1])

		rangesList = append(rangesList, IntRange{start: startingIndex, end: endingIndex})
	}

	sort.Slice(rangesList, func(i, j int) bool {
		return rangesList[i].start < rangesList[j].start
	})

	for index := 0; index < len(rangesList)-1; index++ {
		currentRange := rangesList[index]
		nextRange := rangesList[index+1]
		if currentRange.end >= nextRange.start {
			// merge overlaps
			mergedRange := IntRange{
				start: currentRange.start,
				end:   max(currentRange.end, nextRange.end),
			}
			rangesList = append(rangesList[:index], append([]IntRange{mergedRange}, rangesList[index+2:]...)...)
			index--
		}
	}

	tot := 0
	for _, r := range rangesList {
		tot += r.end - r.start + 1
	}

	return tot
}
