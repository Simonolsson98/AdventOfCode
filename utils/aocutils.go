package utils

import (
	"bufio"
	"math"
	"os"
	"path/filepath"
	"runtime"
	"strings"
)

// ReadInput reads the input from a file for a given day.
func ReadInput(day string) (string, error) {
	// Get the caller's file path (the dayXX.go file)
	_, callerFile, _, _ := runtime.Caller(1)
	
	// The caller file is expected to be in .../AdventOfCode/YYYY/dayXX/dayXX.go
	// So we go up two levels to get to .../AdventOfCode/YYYY
	yearDir := filepath.Dir(filepath.Dir(callerFile))
	
	path := filepath.Join(yearDir, "input", day+".txt")

	file, err := os.Open(path)
	if err != nil {
		return "", err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		return "", err
	}

	return strings.Join(lines, "\n"), nil
}

func CalcAbs(value int) int {
	if value < 0 {
		return -value
	}
	return value
}

func CalcFloor(a, b int) int {
	return int(math.Floor(float64(a) / float64(b)))
}

func PythonMod(a, b int) int {
	return (a%b + b) % b
}
