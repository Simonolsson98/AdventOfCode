package utils

import (
	"fmt"
	"os"
	"path/filepath"
	"strings"
)

// ReadInput reads the input file and returns its content as a string
func ReadInput(filename string) (string, error) {
	// Try to find the input file in likely locations
	// 1. input/filename.txt (relative to CWD)
	// 2. ../input/filename.txt (relative to CWD, e.g. if running from dayXX/)

	// Ensure filename doesn't already have .txt extension, or handle it if it does
	if !strings.HasSuffix(filename, ".txt") {
		filename += ".txt"
	}

	candidates := []string{
		filepath.Join("input", filename),
		filepath.Join("..", "input", filename),
	}

	for _, path := range candidates {
		data, err := os.ReadFile(path)
		if err == nil {
			return strings.TrimSpace(string(data)), nil
		}
	}

	return "", fmt.Errorf("could not find input file %s in %v", filename, candidates)
}
