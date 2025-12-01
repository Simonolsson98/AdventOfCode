package main

import (
    "fmt"
    "strings"
    "os"
    "github.com/simonolsson98/adventofcode/utils"
    "strconv"
    "path/filepath"
    "time"
    "regexp"
    "math"
)

func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

    games := strings.Split(input, "\n\n")
	start := time.Now()
    fmt.Println("Day 13 Solution (Part 1):", part(1, games))
    fmt.Println("Part 1 execution time:", time.Since(start), "\n")

	start = time.Now()
    fmt.Println("Day 13 Solution (Part 2):", part(2, games))
    fmt.Println("Part 2 execution time:", time.Since(start))
}

func part(part int, games []string) (int) {
    totalTokens := 0
    for _, game := range games {
        splitGame := strings.Split(game, "\n")
        buttonA := extractNumbers(splitGame[0])
        buttonB := extractNumbers(splitGame[1])
        prize := extractNumbers(splitGame[2])
        if part == 2{
            prize[0] += 10000000000000
            prize[1] += 10000000000000
        }

        x, y, err := EpicGaussElim(
            [][]float64{{buttonA[0], buttonB[0]},{buttonA[1], buttonB[1]},}, 
            []float64{prize[0], prize[1]})

        if err == nil{
            totalTokens += (3 * x + 1 * y)
        }
    } 

    return int(totalTokens)
}

func EpicGaussElim(a [][]float64, b []float64) (int, int, error) {
    a1, a2 := a[0][0], a[0][1]
    a3, a4 := a[1][0], a[1][1]
    b1, b2 := b[0], b[1]

    det := a1*a4 - a2*a3
    // if det == 0 { literally not needed since inputs are tailored to have only one solution lol
    //     return 0.0, 0.0, fmt.Errorf("equations have no unique solution")
    // }

    x := (b1*a4 - b2*a2) / det
    y := (a1*b2 - a3*b1) / det

    if x != math.Floor(x) || y != math.Floor(y) {
        return 0.0, 0.0, fmt.Errorf("no solutions")
    }

    return int(x), int(y), nil
}

func extractNumbers(input string) ([]float64) {
    re := regexp.MustCompile(`[+=](\d+)`)
    matches := re.FindAllStringSubmatch(input, -1)
    var numbers []float64
    for _, match := range matches {
        if len(match) > 1 {
            num, err := strconv.Atoi(match[1])
            if err == nil {
                numbers = append(numbers, float64(num))
            }
        }
    }

    return numbers
}
