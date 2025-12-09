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
var verticalSegmentsByXCoord map[int][]VSegment
var horizontalSegmentsByYCoord map[int][]HSegment
var verticalSegments []VSegment
var horizontalSegments []HSegment
func part2(input string) int {
	corners := strings.Split(strings.TrimSpace(input), "\n")

	ExtractSegments(corners)

	verticalSegmentsByXCoord = make(map[int][]VSegment)
	for _, s := range verticalSegments {
		verticalSegmentsByXCoord[s.x] = append(verticalSegmentsByXCoord[s.x], s)
	}
	horizontalSegmentsByYCoord = make(map[int][]HSegment)
	for _, s := range horizontalSegments {
		horizontalSegmentsByYCoord[s.y] = append(horizontalSegmentsByYCoord[s.y], s)
	}

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

		if isValid(xMin, xMax, yMin, yMax, horizontalSegments, verticalSegments) {
			return (xdiff + 1) * (ydiff + 1)
		}
	}

	return maxArea
}

func isValid(xMin, xMax, yMin, yMax int, horizontalSegments []HSegment, verticalSegments []VSegment) bool {
	// check corners first
	if !hasPointBelow(xMin, yMin) || !hasPointLeft(xMin, yMin) {
		return false
	}
	if !hasPointBelow(xMax, yMin) || !hasPointRight(xMax, yMin) {
		return false
	}
	if !hasPointAbove(xMin, yMax) || !hasPointLeft(xMin, yMax) {
		return false
	}
	if !hasPointAbove(xMax, yMax) || !hasPointRight(xMax, yMax) {
		return false
	}

	for i := xMin + 1; i < xMax; i++ {
		if !hasPointBelow(i, yMin) {
			return false
		}
		if !hasPointAbove(i, yMax) {
			return false
		}
	}
	for j := yMin + 1; j < yMax; j++ {
		if !hasPointLeft(xMin, j) {
			return false
		}
		if !hasPointRight(xMax, j) {
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

func ExtractSegments(corners []string){
	byX := make(map[int][]int)
	byY := make(map[int][]int)

	for _, corner := range corners {
		parts := strings.Split(corner, ",")
		x, _ := strconv.Atoi(parts[0])
		y, _ := strconv.Atoi(parts[1])
		byX[x] = append(byX[x], y)
		byY[y] = append(byY[y], x)
	}

	for x, ys := range byX {
		for _, y1 := range ys {
			for _, y2 := range ys {
				if y1 == y2 { continue }
				verticalSegments = append(verticalSegments, VSegment{x, min(y1, y2), max(y1, y2)})
			}
		}
	}

	for y, xs := range byY {
		for _, x1 := range xs {
			for _, x2 := range xs {
				if x1 == x2 { continue }
				horizontalSegments = append(horizontalSegments, HSegment{y, min(x1, x2), max(x1, x2)})
			}
		}
	}
}

func hasPointBelow(x, y int) bool {
	// for each vertical segment at x, check if our point is below any of them
	if verticalSegments, ok := verticalSegmentsByXCoord[x]; ok {
		for _, verticalSegment := range verticalSegments {
			if verticalSegment.y1 <= y {
				return true
			}
		}
	}
	// for each horizontal segment, check if our point is below any of them (while also within the x1 and x2 bounds of the segment)
	for _, horizontalSegment := range horizontalSegments {
		if horizontalSegment.y <= y && x >= horizontalSegment.x1 && x <= horizontalSegment.x2 {
			return true
		}
	}
	return false
}

func hasPointAbove(x, y int) bool {
	// for each vertical segment at x, check if our point is above any of them
	if verticalSegments, ok := verticalSegmentsByXCoord[x]; ok {
		for _, verticalSegment := range verticalSegments {
			if verticalSegment.y2 >= y {
				return true
			}
		}
	}
	// for each horizontal segment, check if our point is above any of them (while also within the x1 and x2 bounds of the segment)
	for _, horizontalSegment := range horizontalSegments {
		if horizontalSegment.y >= y && x >= horizontalSegment.x1 && x <= horizontalSegment.x2 {
			return true
		}
	}
	return false
}

func hasPointLeft(x, y int) bool {
	// for each horizontal segment at y, check if our point is left of any of them
	if horizontalSegments, ok := horizontalSegmentsByYCoord[y]; ok {
		for _, horizontalSegment := range horizontalSegments {
			if horizontalSegment.x1 <= x {
				return true
			}
		}
	}
	// for each vertical segment, check if our point is left of any of them (while also within the y1 and y2 bounds of the segment)
	for _, verticalSegment := range verticalSegments {
		if verticalSegment.x <= x && y >= verticalSegment.y1 && y <= verticalSegment.y2 {
			return true
		}
	}
	return false
}

func hasPointRight(x, y int) bool {
	// for each horizontal segment at y, check if our point is right of any of them
	if horizontalSegments, ok := horizontalSegmentsByYCoord[y]; ok {
		for _, s := range horizontalSegments {
			if s.x2 >= x {
				return true
			}
		}
	}
	// for each vertical segment, check if our point is right of any of them (while also within the y1 and y2 bounds of the segment)
	for _, verticalSegment := range verticalSegments {
		if verticalSegment.x >= x && y >= verticalSegment.y1 && y <= verticalSegment.y2 {
			return true
		}
	}
	return false
}
