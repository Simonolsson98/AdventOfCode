package main

import (
    "fmt"
    "log"
    "github.com/Simonolsson98/AdventOfCode/tree/main/2024/Utils/readinput"  // Import the utils package
)

func main() {
    input, err := utils.ReadInput("day01_input")  // Call ReadInput from utils
    if err != nil {
        log.Fatalf("Error reading input: %v", err)
    }
    fmt.Println("Day 1 Solution:")
    // Solution logic here...
}