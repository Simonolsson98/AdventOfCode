package main

import (
	"fmt"
	"os"
	"path/filepath"
	"slices"
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
	splitEntireInput := strings.Split(strings.TrimSpace(input), "\n")
	lenOfEntireInput := len(splitEntireInput)
	for x := range lenOfEntireInput {
		for y := x + 1; y < lenOfEntireInput; y++ {
			line := splitEntireInput[x]
			line2 := splitEntireInput[y]
			if line == line2 {
				continue
			}

			coords := strings.Split(line, ",")
			coords2 := strings.Split(line2, ",")
			x, _ := strconv.Atoi(coords[0])
			y, _ := strconv.Atoi(coords[1])
			x2, _ := strconv.Atoi(coords2[0])
			y2, _ := strconv.Atoi(coords2[1])

			xdiff := utils.CalcAbs(x - x2)
			ydiff := utils.CalcAbs(y - y2)
			if (xdiff+1)*(ydiff+1) > max {
				max = (xdiff + 1) * (ydiff + 1)
			}

			sortedByAreas = append(sortedByAreas, PairWithArea{Pair{x, y}, Pair{x2, y2}, (xdiff + 1) * (ydiff + 1)})
		}
	}
	return max
}

type Pair struct {
	x, y int
}

type PairWithArea struct {
	pair Pair
	pair2 Pair
	area int
}

var sortedByAreas []PairWithArea

func part2(input string) int {

	corners := strings.Split(strings.TrimSpace(input), "\n")
	var hSegments []HSegment
	var vSegments []VSegment

	hSegments, vSegments = ExtractSegments(corners)

	slices.SortFunc(sortedByAreas, func(a, b PairWithArea) int {
		return b.area - a.area
	})

	maxArea := 0
	for _, pairOfCornerCoordinates := range sortedByAreas { // will try each largest area first
		firstPair := pairOfCornerCoordinates.pair
		secondPair := pairOfCornerCoordinates.pair2

		x := firstPair.x
		y := firstPair.y
		x2 := secondPair.x
		y2 := secondPair.y

		xdiff := utils.CalcAbs(x - x2)
		ydiff := utils.CalcAbs(y - y2)
		xMin := min(x, x2)
		xMax := max(x, x2)
		yMin := min(y, y2)
		yMax := max(y, y2)

		if isValid(xMin, xMax, yMin, yMax, hSegments, vSegments) {
			return (xdiff + 1) * (ydiff + 1)
		}
	}

	return maxArea
}

func isValid(xMin, xMax, yMin, yMax int, hSegments []HSegment, vSegments []VSegment) bool {
	// check corners first
	if !hasPointBelow(xMin, yMin, hSegments, vSegments) || !hasPointLeft(xMin, yMin, hSegments, vSegments) {
		return false
	}
	if !hasPointBelow(xMax, yMin, hSegments, vSegments) || !hasPointRight(xMax, yMin, hSegments, vSegments) {
		return false
	}
	if !hasPointAbove(xMin, yMax, hSegments, vSegments) || !hasPointLeft(xMin, yMax, hSegments, vSegments) {
		return false
	}
	if !hasPointAbove(xMax, yMax, hSegments, vSegments) || !hasPointRight(xMax, yMax, hSegments, vSegments) {
		return false
	}

	// otherwise... check if any point of the rectangle is outside a segment => invalid
	for i := xMin + 1; i < xMax; i++ {
		if !hasPointBelow(i, yMin, hSegments, vSegments) {
			return false
		}
		if !hasPointAbove(i, yMax, hSegments, vSegments) {
			return false
		}
	}
	for j := yMin + 1; j < yMax; j++ {
		if !hasPointLeft(xMin, j, hSegments, vSegments) {
			return false
		}
		if !hasPointRight(xMax, j, hSegments, vSegments) {
			return false
		}
	}
	return true
}

type HSegment struct {
	y, x1, x2 int
}

type VSegment struct {
	x, y1, y2 int
}

func ExtractSegments(corners []string) ([]HSegment, []VSegment) {
	var hSegments []HSegment
	var vSegments []VSegment

	mapByXCoordinate := make(map[int][]int)
	mapByYCoordinate := make(map[int][]int)

	for _, corner := range corners {
		parts := strings.Split(corner, ",")
		x, _ := strconv.Atoi(parts[0])
		y, _ := strconv.Atoi(parts[1])

		//store y coordinates by x and vice versa, for potential segment extraction
		mapByXCoordinate[x] = append(mapByXCoordinate[x], y)
		mapByYCoordinate[y] = append(mapByYCoordinate[y], x)
	}

	for x, ys := range mapByXCoordinate {
		for _, y1 := range ys {
			for _, y2 := range ys {
				if y1 == y2 { continue }
				vSegments = append(vSegments, VSegment{x, min(y1, y2), max(y1, y2)})
			}
		}
	}

	for y, xs := range mapByYCoordinate {
		for _, x1 := range xs {
			for _, x2 := range xs {
				if x1 == x2 { continue }
				hSegments = append(hSegments, HSegment{y, min(x1, x2), max(x1, x2)})
			}
		}
	}
	
	return hSegments, vSegments
}

func hasPointBelow(x, y int, hSegs []HSegment, vSegs []VSegment) bool {
	for _, s := range vSegs {
		if s.x == x && s.y1 <= y {
			return true
		}
	}
	for _, s := range hSegs {
		if s.y <= y && x >= s.x1 && x <= s.x2 {
			return true
		}
	}
	return false
}

func hasPointAbove(x, y int, hSegs []HSegment, vSegs []VSegment) bool {
	for _, s := range vSegs {
		if s.x == x && s.y2 >= y {
			return true
		}
	}
	for _, s := range hSegs {
		if s.y >= y && x >= s.x1 && x <= s.x2 {
			return true
		}
	}
	return false
}

func hasPointLeft(x, y int, hSegs []HSegment, vSegs []VSegment) bool {
	for _, s := range hSegs {
		if s.y == y && s.x1 <= x {
			return true
		}
	}
	for _, s := range vSegs {
		if s.x <= x && y >= s.y1 && y <= s.y2 {
			return true
		}
	}
	return false
}

func hasPointRight(x, y int, hSegs []HSegment, vSegs []VSegment) bool {
	for _, s := range hSegs {
		if s.y == y && s.x2 >= x {
			return true
		}
	}
	for _, s := range vSegs {
		if s.x >= x && y >= s.y1 && y <= s.y2 {
			return true
		}
	}
	return false
}
