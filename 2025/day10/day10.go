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

	return 0
}
