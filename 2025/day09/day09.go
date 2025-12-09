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
	for _, line := range strings.Split(strings.TrimSpace(input), "\n") {
		for _, line2 := range strings.Split(strings.TrimSpace(input), "\n") {
			if line == line2 {
				continue
			}

			coords := strings.Split(line, ",")
			coords2 := strings.Split(line2, ",")
			x, _ := strconv.Atoi(coords[0])
			y, _ := strconv.Atoi(coords[1])
			x2, _ := strconv.Atoi(coords2[0])
			y2, _ := strconv.Atoi(coords2[1])

			xdiff := x - x2
			ydiff := y - y2
			if xdiff < 0 {
				xdiff = -xdiff
			}
			if ydiff < 0 {
				ydiff = -ydiff
			}
			if (xdiff+1)*(ydiff+1) > max {
				max = (xdiff + 1) * (ydiff + 1)
			}
		}
	}
	return max
}

type Pair struct {
	x, y int
}

func part2(input string) int {
	corners := strings.Split(strings.TrimSpace(input), "\n")
	var hSegments []HSegment
	var vSegments []VSegment

	for _, corner := range corners {
		currentCorner := strings.Split(corner, ",")
		currentCornerXCoord, _ := strconv.Atoi(currentCorner[0])
		currentCornerYCoord, _ := strconv.Atoi(currentCorner[1])

		corners2 := strings.Split(strings.TrimSpace(input), "\n")
		for _, corner2 := range corners2 {
			if corner2 == corner {
				continue
			}

			otherCorner := strings.Split(corner2, ",")
			otherCornerXCoord, _ := strconv.Atoi(otherCorner[0])
			otherCornerYCoord, _ := strconv.Atoi(otherCorner[1])
			if otherCornerXCoord == currentCornerXCoord { // matching x coord
				y1 := min(currentCornerYCoord, otherCornerYCoord)
				y2 := max(currentCornerYCoord, otherCornerYCoord)
				vSegments = append(vSegments, VSegment{currentCornerXCoord, y1, y2})
			} else if otherCornerYCoord == currentCornerYCoord { // matching y coord
				x1 := min(currentCornerXCoord, otherCornerXCoord)
				x2 := max(currentCornerXCoord, otherCornerXCoord)
				hSegments = append(hSegments, HSegment{currentCornerYCoord, x1, x2})
			}
		}
	}

	maxArea := 0
	for _, line := range strings.Split(strings.TrimSpace(input), "\n") {
		for _, line2 := range strings.Split(strings.TrimSpace(input), "\n") {
			if line == line2 {
				continue
			}

			coords := strings.Split(line, ",")
			coords2 := strings.Split(line2, ",")
			x, _ := strconv.Atoi(coords[0])
			y, _ := strconv.Atoi(coords[1])
			x2, _ := strconv.Atoi(coords2[0])
			y2, _ := strconv.Atoi(coords2[1])

			xdiff := x - x2
			ydiff := y - y2
			if xdiff < 0 {
				xdiff = -xdiff
			}
			if ydiff < 0 {
				ydiff = -ydiff
			}
			if (xdiff+1)*(ydiff+1) > maxArea {
				xMin := min(x, x2)
				xMax := max(x, x2)
				yMin := min(y, y2)
				yMax := max(y, y2)

				valid := true
				for i := xMin; i <= xMax; i++ {
					if !hasPointBelow(i, yMin, hSegments, vSegments) {
						valid = false
						break
					}
					if !hasPointAbove(i, yMax, hSegments, vSegments) {
						valid = false
						break
					}
				}
				if valid {
					for j := yMin; j <= yMax; j++ {
						if !hasPointLeft(xMin, j, hSegments, vSegments) {
							valid = false
							break
						}
						if !hasPointRight(xMax, j, hSegments, vSegments) {
							valid = false
							break
						}
					}
				}

				if valid {
					maxArea = (xdiff + 1) * (ydiff + 1)
				}
			}
		}
	}

	return maxArea
}

type HSegment struct {
	y, x1, x2 int
}

type VSegment struct {
	x, y1, y2 int
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

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
