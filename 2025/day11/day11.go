package main

import (
	"fmt"
	"maps"
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
	result = part2("svr", mapOfRoutes, make(map[string]int), map[string]bool{"dac": false, "fft": false})
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

func part2(route string, mapOfRoutes map[string][]string, visited map[string]int, visitedNecessaryRoutes map[string]bool) int {
	if val, ok := visited[route]; ok && visitedNecessaryRoutes["dac"] && visitedNecessaryRoutes["fft"] {
		// cache hit
		println("Cache hit for", route, "with value", val)
		return val
	}

	count := 0
	visitedNecessaryRoutesCopy := make(map[string]bool)
	maps.Copy(visitedNecessaryRoutesCopy, visitedNecessaryRoutes)

	for x, neighbor := range mapOfRoutes[route] {
		println(" - exploring neighbor", x, ":", neighbor, "from", route)
		if neighbor == "fft" {
			// println("Found", neighbor)
			visitedNecessaryRoutes["fft"] = true
		}
		if neighbor == "dac" {
			// println("Found", neighbor)
			visitedNecessaryRoutes["dac"] = true
		}

		if neighbor == "out" && visitedNecessaryRoutes["dac"] && visitedNecessaryRoutes["fft"] {
			// println("Valid route found through", route)
			count++
		} else {
			// recurse
			// println("recursing to", neighbor, "via", route)
			// for i := range visitedNecessaryRoutes {
			// 	println(" - visitedNecessaryRoutes:", i, "=", visitedNecessaryRoutes[i])
			// }
			count += part2(neighbor, mapOfRoutes, visited, visitedNecessaryRoutes)
			visitedNecessaryRoutes = visitedNecessaryRoutesCopy
		}
	}

	if visitedNecessaryRoutes["dac"] && visitedNecessaryRoutes["fft"] {
		visited[route] = count //save all possible routes from this node
		// println("adding to cache:", route, "with value", count)
	}
	return count
}
