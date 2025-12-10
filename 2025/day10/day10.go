package main

import (
	"fmt"
	"math"
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
	fmt.Println("Day 10 Solution (Part 1):", result)
	fmt.Printf("Part 1 execution time: %.2fµs\n", float64(elapsed.Nanoseconds())/1000.0)

	start = time.Now()
	result = part2(input)
	elapsed = time.Since(start)
	fmt.Println("Day 10 Solution (Part 2):", result)
	fmt.Printf("Part 2 execution time: %.2fµs\n", float64(elapsed.Nanoseconds())/1000.0)
}

func part1(input string) int {
	totalButtonPresses := 0

	for _, line := range strings.Split(input, "\n") {
		buttonPresses := 0
		parts := strings.Split(line, " ")
		lightConfigRune := []rune(parts[0])
		lightConfig := strings.ReplaceAll(string(lightConfigRune), "[", "")
		lightConfig = strings.ReplaceAll(lightConfig, "]", "")
		buttons := parts[1 : len(parts)-1]
		tenConfig := 0
		for i, ch := range lightConfig {
			if ch == '#' {
				tenConfig += int(math.Pow(2, float64(i)))
			}
		}
		tenButtons := []int{}
		for _, btn := range buttons {
			btn = strings.ReplaceAll(btn, "(", "")
			btn = strings.ReplaceAll(btn, ")", "")
			btnParts := strings.Split(btn, ",")
			var val int
			for _, ch := range btnParts { // interpret as binary and convert to decimal base
				num, _ := strconv.Atoi(ch)
				val += int(math.Pow(2, float64(num)))
			}

			tenButtons = append(tenButtons, val)
		}

		states := []int{tenConfig}
		newStates := []int{}
		buttonPresses = 0
		for keepGoing := true; keepGoing; {
			newStates = []int{}
			for _, state := range states {
				for i := 0; i < len(tenButtons); i++ {
					current := state ^ tenButtons[i]
					newStates = append(newStates, current)
					if current == 0 {
						keepGoing = false
						totalButtonPresses += buttonPresses + 1
						break
					}
				}

				if !keepGoing {
					break
				}
			}
			if !keepGoing {
				break
			}

			states = newStates
			buttonPresses++
		}
	}

	return totalButtonPresses
}

func part2(input string) int {
	totalButtonPresses := 0
	for _, line := range strings.Split(input, "\n") {
		parts := strings.Split(line, " ")

		buttons := []string{}
		for i := 1; i < len(parts)-1; i++ {
			parts[i] = strings.ReplaceAll(parts[i], "(", "")
			parts[i] = strings.ReplaceAll(parts[i], ")", "")
			buttons = append(buttons, parts[i])
		}

		// Pre-parse buttons to avoid repeated string splitting
		parsedButtons := [][]int{}
		for _, btnStr := range buttons {
			btnParts := strings.Split(btnStr, ",")
			btn := []int{}
			for _, p := range btnParts {
				if p == "" {
					continue
				}
				val, _ := strconv.Atoi(p)
				btn = append(btn, val)
			}
			parsedButtons = append(parsedButtons, btn)
		}

		joltages := strings.Split(parts[len(parts)-1], ",")
		joltageTargets := []int{}
		joltageInitial := [][]int{{}}
		for _, j := range joltages {
			j = strings.ReplaceAll(j, "{", "")
			j = strings.ReplaceAll(j, "}", "")
			joltage, _ := strconv.Atoi(j)
			joltageTargets = append(joltageTargets, joltage)
			joltageInitial[0] = append(joltageInitial[0], 0)
		}

		// solve using Parametric Gaussian Elimination
        totalButtonPresses += GaussElimination(parsedButtons, joltageTargets)
	}

	return totalButtonPresses
}

func GaussElimination(buttons [][]int, targets []int) int {
	rows := len(targets)
	cols := len(buttons)

	// augmented matrix
	matrix := make([][]float64, rows)
	for i := 0; i < rows; i++ {
		matrix[i] = make([]float64, cols+1)
		matrix[i][cols] = float64(targets[i])
	}

	for j := 0; j < cols; j++ {
		for _, targetIdx := range buttons[j] {
			matrix[targetIdx][j]++
		}
	}

	// Gaussian Elimination to reduced row echelon form
	pivotRow := 0
	pivots := make(map[int]int) // col -> row
	
	for col := 0; col < cols && pivotRow < rows; col++ {
		// find pivot
		sel := -1
		for i := pivotRow; i < rows; i++ {
			if math.Abs(matrix[i][col]) > 1e-9 {
				sel = i
				break
			}
		}

		if sel == -1 {
			continue
		}

		matrix[pivotRow], matrix[sel] = matrix[sel], matrix[pivotRow]

		// normalize pivot
		pivotVal := matrix[pivotRow][col]
		for j := col; j <= cols; j++ {
			matrix[pivotRow][j] /= pivotVal
		}

		// eliminate column
		for i := 0; i < rows; i++ {
			if i != pivotRow {
				factor := matrix[i][col]
				if math.Abs(factor) > 1e-9 {
					for j := col; j <= cols; j++ {
						matrix[i][j] -= factor * matrix[pivotRow][j]
					}
				}
			}
		}

		pivots[col] = pivotRow
		pivotRow++
	}

	// identify free variables
	freeVars := []int{}
	for j := 0; j < cols; j++ {
		if _, ok := pivots[j]; !ok {
			freeVars = append(freeVars, j)
		}
	}
	
	minTotal := -1

	var solve func(idx int, currentFreeValues []int)
	solve = func(idx int, currentFreeValues []int) {
		if idx == len(freeVars) {
			// all free vars assigned, check pivots.
			currentTotal := 0
			for _, val := range currentFreeValues {
				currentTotal += val
			}
			
			valid := true
			for col := 0; col < cols; col++ {
				if _, isPivot := pivots[col]; isPivot {
					row := pivots[col]
					val := matrix[row][cols]
					
					// subtract free var contributions
					for k, freeCol := range freeVars {
						coeff := matrix[row][freeCol]
						val -= coeff * float64(currentFreeValues[k])
					}
					
					// check if integer and non-negative
					if val < 0 || math.Abs(val - math.Round(val)) > 1e-9 {
						valid = false
						break
					}
					currentTotal += int(math.Round(val))
				}
			}
			
			if valid {
				if minTotal == -1 || currentTotal < minTotal {
					minTotal = currentTotal
				}
			}
			return
		}

		freeCol := freeVars[idx]
		maxVal := math.MaxInt32
		
		// check original constraints for this column
		for _, targetIdx := range buttons[freeCol] {
			// count how many times it hits this target
			count := 0
			for _, t := range buttons[freeCol] {
				if t == targetIdx {
					count++
				}
			}
			b := targets[targetIdx] / count
			if b < maxVal {
				maxVal = b
			}
		}
		
		for val := 0; val <= maxVal; val++ {
			currentFreeValues[idx] = val
			solve(idx+1, currentFreeValues)
		}
	}
	
	solve(0, make([]int, len(freeVars)))

	return minTotal
}
