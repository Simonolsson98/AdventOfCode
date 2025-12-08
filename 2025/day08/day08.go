package main

import (
	"fmt"
	"os"
	"sort"
	"strings"

	"github.com/simonolsson98/adventofcode/utils"

	"path/filepath"
	"strconv"
	"time"
)

type Point struct {
	x, y, z int
}

type Pair struct {
	p1, p2 Point
	distSq int
}

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
	fmt.Println("Day 8 Solution (Part 1):", result)
	fmt.Printf("Part 1 execution time: %.2fµs\n", float64(elapsed.Nanoseconds())/1000.0)

	start = time.Now()
	result = part2(input)
	elapsed = time.Since(start)
	fmt.Println("Day 8 Solution (Part 2):", result)
	fmt.Printf("Part 2 execution time: %.2fµs\n", float64(elapsed.Nanoseconds())/1000.0)
}

func part1(input string) int {
	lines := strings.Split(strings.TrimSpace(input), "\n")
	var points []Point
	for _, line := range lines {
		parts := strings.Split(line, ",")
		x, _ := strconv.Atoi(parts[0])
		y, _ := strconv.Atoi(parts[1])
		z, _ := strconv.Atoi(parts[2])
		points = append(points, Point{x, y, z})
	}

	var pairs []Pair = GenerateEuclidianDistances(points)

	sort.Slice(pairs, func(i, j int) bool {
		return pairs[i].distSq < pairs[j].distSq
	})

	var mapOfConnectedCircuits map[int][]Point = make(map[int][]Point)
	nextCircuit := 0
	for i := 0; i < len(points); i++ { // len(points) is the same as 1000
		p1IsConnected := false
		p2IsConnected := false
		currIndexp1 := -1
		currIndexp2 := -1
		for k, v := range mapOfConnectedCircuits {
			for j := range v {
				currValue := v[j]
				if pairs[i].p1 == currValue {
					currIndexp1 = k
					p1IsConnected = true
				}
				if pairs[i].p2 == currValue {
					currIndexp2 = k
					p2IsConnected = true
				}

				if p1IsConnected && p2IsConnected {
					break
				}
			}
		}

		if p1IsConnected && p2IsConnected && (currIndexp1 == currIndexp2) { // both points are in the same circuit
			continue
		} else if p1IsConnected && p2IsConnected && (currIndexp1 != currIndexp2) { // both points are in different circuits - merge them
			mapOfConnectedCircuits[currIndexp1] = append(mapOfConnectedCircuits[currIndexp1], mapOfConnectedCircuits[currIndexp2]...)
			delete(mapOfConnectedCircuits, currIndexp2)
		} else if p1IsConnected { // only p1 is connected, so add p2 to p1's circuit
			mapOfConnectedCircuits[currIndexp1] = append(mapOfConnectedCircuits[currIndexp1], pairs[i].p2)
		} else if p2IsConnected { // only p2 is connected, so add p1 to p2's circuit
			mapOfConnectedCircuits[currIndexp2] = append(mapOfConnectedCircuits[currIndexp2], pairs[i].p1)
		} else { // neither point is connected, so create a new circuit
			mapOfConnectedCircuits[nextCircuit] = append(mapOfConnectedCircuits[currIndexp1], pairs[i].p1, pairs[i].p2)
			nextCircuit++
		}
	}

	largestCircuitSize := 0
	secondLargestCircuitSize := 0
	thirdLargestCircuitSize := 0
	for i := range mapOfConnectedCircuits {
		circuitSize := len(mapOfConnectedCircuits[i])
		if circuitSize > largestCircuitSize {
			thirdLargestCircuitSize = secondLargestCircuitSize
			secondLargestCircuitSize = largestCircuitSize
			largestCircuitSize = circuitSize
		} else if circuitSize > secondLargestCircuitSize {
			thirdLargestCircuitSize = secondLargestCircuitSize
			secondLargestCircuitSize = circuitSize
		} else if circuitSize > thirdLargestCircuitSize {
			thirdLargestCircuitSize = circuitSize
		}
	}

	return largestCircuitSize * secondLargestCircuitSize * thirdLargestCircuitSize
}

func GenerateEuclidianDistances(points []Point) []Pair {
	var pairs []Pair
	for i := 0; i < len(points); i++ {
		for j := i + 1; j < len(points); j++ {
			p1 := points[i]
			p2 := points[j]

			dx := p1.x - p2.x
			dy := p1.y - p2.y
			dz := p1.z - p2.z

			distSq := dx*dx + dy*dy + dz*dz

			pairs = append(pairs, Pair{p1, p2, distSq})
		}
	}
	return pairs
}

func part2(input string) int {
	lines := strings.Split(strings.TrimSpace(input), "\n")
	var points []Point
	for _, line := range lines {
		parts := strings.Split(line, ",")
		x, _ := strconv.Atoi(parts[0])
		y, _ := strconv.Atoi(parts[1])
		z, _ := strconv.Atoi(parts[2])
		points = append(points, Point{x, y, z})
	}

	var pairs []Pair = GenerateEuclidianDistances(points)

	sort.Slice(pairs, func(i, j int) bool {
		return pairs[i].distSq < pairs[j].distSq
	})

	var mapOfConnectedCircuits map[int][]Point = make(map[int][]Point)
	nextCircuit := 0
	for i := 0; i > -1; i++ {
		p1IsConnected := false
		p2IsConnected := false
		currIndexp1 := -1
		currIndexp2 := -1
		for k, v := range mapOfConnectedCircuits {
			for j := range v {
				currValue := v[j]
				if pairs[i].p1 == currValue {
					currIndexp1 = k
					p1IsConnected = true
				}
				if pairs[i].p2 == currValue {
					currIndexp2 = k
					p2IsConnected = true
				}

				if p1IsConnected && p2IsConnected {
					break
				}
			}
		}

		if p1IsConnected && p2IsConnected && (currIndexp1 == currIndexp2) { // both points are in the same circuit
			continue
		} else if p1IsConnected && p2IsConnected && (currIndexp1 != currIndexp2) { // both points are in different circuits - merge them
			mapOfConnectedCircuits[currIndexp1] = append(mapOfConnectedCircuits[currIndexp1], mapOfConnectedCircuits[currIndexp2]...)
			delete(mapOfConnectedCircuits, currIndexp2)
		} else if p1IsConnected { // only p1 is connected, so add p2 to p1's circuit
			mapOfConnectedCircuits[currIndexp1] = append(mapOfConnectedCircuits[currIndexp1], pairs[i].p2)
		} else if p2IsConnected { // only p2 is connected, so add p1 to p2's circuit
			mapOfConnectedCircuits[currIndexp2] = append(mapOfConnectedCircuits[currIndexp2], pairs[i].p1)
		} else { // neither point is connected, so create a new circuit
			mapOfConnectedCircuits[nextCircuit] = append(mapOfConnectedCircuits[currIndexp1], pairs[i].p1, pairs[i].p2)
			nextCircuit++
		}

		if len(mapOfConnectedCircuits) == 1 && i > 1 { // one circuit left, as long as it isnt the first iteration (the first circuit created)
			return pairs[i].p1.x * pairs[i].p2.x
		}
	}

	return -1
}
