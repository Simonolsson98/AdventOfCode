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
	result = part2("svr", mapOfRoutes, make(map[Part2State]int), false, false)
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

type Part2State struct {
	Route  string
	HasDac bool
	HasFft bool
}

func part2(route string, mapOfRoutes map[string][]string, visited map[Part2State]int, hasDac, hasFft bool) int {
	if route == "dac" {
		hasDac = true
	}
	if route == "fft" {
		hasFft = true
	}

	state := Part2State{Route: route, HasDac: hasDac, HasFft: hasFft}
	if val, ok := visited[state]; ok {
		return val
	}

	if route == "out" {
		if hasDac && hasFft {
			return 1
		}
		return 0
	}

	count := 0
	for _, neighbor := range mapOfRoutes[route] {
		count += part2(neighbor, mapOfRoutes, visited, hasDac, hasFft)
	}

	visited[state] = count
	return count
}
