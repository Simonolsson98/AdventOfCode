package utils

import (
    "bufio"
    "os"
    "strings"
)

// ReadInput reads the input from a file for a given day.
func ReadInput(day string) (string, error) {
    path := "input/" + day + ".txt"
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
