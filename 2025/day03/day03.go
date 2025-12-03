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
	result := bothParts(input, 2)
	fmt.Println("Day 3 Solution (Part 1):", result)
	fmt.Println("Part 1 execution time:", time.Since(start))

	start = time.Now()
	result = bothParts(input, 12)
	fmt.Println("Day 3 Solution (Part 2):", result)
	fmt.Println("Part 2 execution time:", time.Since(start))
}

func bothParts(input string, numOfBatteries int) int {
	totalJoltageOutput := 0
	for _, line := range strings.Split(input, "\n") {
		maxBatteries := make([]int, numOfBatteries)
		for index, battery := range strings.Split(line, "") {
			joltage, _ := strconv.Atoi(battery)

			for i := range len(maxBatteries) {
				// new max for the "most significant" battery
				if joltage > maxBatteries[i] && (len(line)-1-index) >= (len(maxBatteries)-1-i) {
					maxBatteries[i] = joltage

					// clear all indices that come after the changed max battery joltage
					for j := i + 1; j < len(maxBatteries); j++ {
						maxBatteries[j] = 0
					}
					break
				}
			}
		}

		var tempJoltage string
		for _, b := range maxBatteries {
			tempJoltage += strconv.Itoa(b)
		}
		tempJoltageCount, _ := strconv.Atoi(tempJoltage)
		totalJoltageOutput += tempJoltageCount
	}

	return totalJoltageOutput
}
