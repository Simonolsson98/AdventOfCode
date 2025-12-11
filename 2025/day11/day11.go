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

	mapOfRoutes := make(map[string][]string)
	for _, line := range strings.Split(input, "\n") {
		parts := strings.Split(line, " ")
		source := strings.ReplaceAll(parts[0], ":", "")
		otherParts := parts[1:]
		mapOfRoutes[source] = otherParts
	}

	start := time.Now()
	result := part1("you", mapOfRoutes, make(map[string]int))
	elapsed := time.Since(start)
	fmt.Println("Day 11 Solution (Part 1):", result)
	fmt.Printf("Part 1 execution time: %.2fµs\n", float64(elapsed.Nanoseconds())/1000.0)

	start = time.Now()
	result = part2(input)
	elapsed = time.Since(start)
	fmt.Println("Day 11 Solution (Part 2):", result)
	fmt.Printf("Part 2 execution time: %.2fµs\n", float64(elapsed.Nanoseconds())/1000.0)
}

func part1(route string, mapOfRoutes map[string][]string, visited map[string]int) int {
	if val, ok := visited[route]; ok {
		// cache hit
		return val
	}

	count := 0
	for _, neighbor := range mapOfRoutes[route] {
		if neighbor == "out" {
			count++
		} else {
			// recurse
			count += part1(neighbor, mapOfRoutes, visited)
		}
	}

	visited[route] = count //save all possible routes from this node
	return count
}

func part2(input string) int {

	return 0
}
