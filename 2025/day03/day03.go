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
	fmt.Println("Day 3 Solution (Part 1):", result)
	fmt.Println("Part 1 execution time:", time.Since(start))

	start = time.Now()
	result = part2(input)
	fmt.Println("Day 3 Solution (Part 2):", result)
	fmt.Println("Part 2 execution time:", time.Since(start))
}

func part1(input string) int {
	batteryCount := 0
	for _, line := range strings.Split(input, "\n") {
		maxBattery := 0
		secondMaxBattery := 0
		for index, battery := range strings.Split(line, "") {
			val, _ := strconv.Atoi(battery)
			if val > maxBattery && index < len(line)-1 {
				maxBattery = val
				secondMaxBattery = 0
			} else if val > secondMaxBattery {
				secondMaxBattery = val
			}
		}

		tempCount, _ := strconv.Atoi(strconv.Itoa(maxBattery) + strconv.Itoa(secondMaxBattery))
		batteryCount += tempCount
	}

	return batteryCount
}

func part2(input string) int {
	batteryCount := 0
	for _, line := range strings.Split(input, "\n") {
		maxBatteries := make([]int, 12)
		for index, battery := range strings.Split(line, "") {
			joltage, _ := strconv.Atoi(battery)

			// new max for the "most significant" battery
			for i := 0; i < len(maxBatteries); i++ {
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

		var temp string
		for _, b := range maxBatteries {
			temp += strconv.Itoa(b)
		}
		tempCount, _ := strconv.Atoi(temp)
		batteryCount += tempCount
	}

	return batteryCount
}
