package main

import (
    "fmt"
    "strings"
    "os"
    "2024/utils"
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

	start := time.Now()
	
    games := strings.Split(input, "\n\n")
    totalTokens := 0.0
    for _, game := range games {
        minres := -1.0
        splitGame := strings.Split(game, "\n")
        buttonA := extractNumbers(splitGame[0])
        buttonB := extractNumbers(splitGame[1])
        prize := extractNumbers(splitGame[2])
        for i := 0.0; i <= 100.0; i++ {
            for j := 0.0; j <= 100.0; j++ {
                calcValX := i * buttonA[0] + j * buttonB[0]
                calcValY := i * buttonA[1] + j * buttonB[1]
                if calcValX == prize[0] && calcValY == prize[1] {
                    if minres == -1.0 || minres > 3.0 * i + 1.0 * j {
                        minres = 3.0 * i + 1.0 * j
                    }
                }
            }
        }

        if minres == -1.0{
            minres = 0.0
        }
        totalTokens += minres
    } 

    fmt.Println("Day 13 Solution (Part 1):", totalTokens)
    fmt.Println("Part 1 execution time:", time.Since(start), "\n")

	start = time.Now()

    totalTokens = 0.0
    for _, game := range games {
        minres := 0.0
        splitGame := strings.Split(game, "\n")
        buttonA := extractNumbers(splitGame[0])
        buttonB := extractNumbers(splitGame[1])
        prize := extractNumbers(splitGame[2])
        prize[0] += 10000000000000
        prize[1] += 10000000000000
        coefficients := [][]float64{
            {buttonA[0], buttonB[0]},  // Coefficients of x and y in the first equation
            {buttonA[1], buttonB[1]},  // Coefficients of x and y in the second equation
        }
        x, y, err := EpicGaussElim(coefficients, []float64{prize[0], prize[1]})

        if err == nil{
            minres = 3.0 * x + 1.0 * y
        }

        totalTokens += minres
    } 
    
    fmt.Println("Day 13 Solution (Part 2):", int(totalTokens))
    fmt.Println("Part 2 execution time:", time.Since(start))
}

func EpicGaussElim(a [][]float64, b []float64) (float64, float64, error) {
    if len(a) != 2 || len(a[0]) != 2 || len(b) != 2 {
        return 0.0, 0.0, fmt.Errorf("invalid input dimensions")
    }

    a1, a2 := a[0][0], a[0][1]
    a3, a4 := a[1][0], a[1][1]
    b1, b2 := b[0], b[1]

    det := a1*a4 - a2*a3
    if det == 0 {
        return 0.0, 0.0, fmt.Errorf("equations have no unique solution")
    }

    x := (b1*a4 - b2*a2) / det
    y := (a1*b2 - a3*b1) / det

    if x != math.Floor(x) || y != math.Floor(y) || x < 0 || y < 0 {
        return 0.0, 0.0, fmt.Errorf("no non-negative integer solutions exist")
    }

    return x, y, nil
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
