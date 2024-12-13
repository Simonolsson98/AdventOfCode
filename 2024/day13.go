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
    totalTokens := 0
    for _, game := range games {
        minres := -1
        splitGame := strings.Split(game, "\n")
        numsA := extractNumbers(splitGame[0])
        numsB := extractNumbers(splitGame[1])
        numsP := extractNumbers(splitGame[2])
        for i := 0; i <= 100; i++ {
            for j := 0; j <= 100; j++ {
                calcValX := i * numsA[0] + j * numsB[0]
                calcValY := i * numsA[1] + j * numsB[1]
                if calcValX == numsP[0] && calcValY == numsP[1] {
                    if minres == -1 || minres > 3 * i + 1 * j {
                        minres = 3 * i + 1 * j
                    }
                }
            }
        }

        if minres == -1{
            minres = 0
        }
        totalTokens += minres
    } 

    fmt.Println("Day 13 Solution (Part 1):", totalTokens)
    fmt.Println("Part 1 execution time:", time.Since(start), "\n")

	start = time.Now()

    totalTokens = 0
    for _, game := range games {
        minres := -1
        splitGame := strings.Split(game, "\n")
        numsA := extractNumbers(splitGame[0])
        numsB := extractNumbers(splitGame[1])
        numsP := extractNumbers(splitGame[2])

        wtf := SolveDiophantine(numsA[0], numsB[0], numsP[0])

        fmt.Println(wtf)
        return
        // for i := 0; i <= 100; i++ {
        //     for j := 0; j <= 100; j++ {
        //         calcValX := i * numsA[0] + j * numsB[0]
        //         calcValY := i * numsA[1] + j * numsB[1]
        //         if calcValX == numsP[0] && calcValY == numsP[1] {
        //             if minres == -1 || minres > 3 * i + 1 * j {
        //                 minres = 3 * i + 1 * j
        //             }
        //         }
        //     }
        // }

        if minres == -1{
            minres = 0
        }
        totalTokens += minres
    } 

    //SURELY I CAN DO MOD AND FOR EACH OVER THE HELTALRESULT, AND CHECK INDICES FOR Y?
    
    fmt.Println("Day 13 Solution (Part 2):")
    fmt.Println("Part 2 execution time:", time.Since(start))
}

// ExtendedGCD computes gcd(a, b) and finds x, y such that ax + by = gcd(a, b)
func ExtendedGCD(a, b int) (gcd, x, y int) {
    if b == 0 {
        return a, 1, 0
    }
    gcd, x1, y1 := ExtendedGCD(b, a%b)
    x = y1
    y = x1 - (a/b)*y1
    return
}

// SolveDiophantine finds solutions to ax + by = N with positive x, y
func SolveDiophantine(a, b, N int) (res []int){
    // Step 1: Compute gcd and check if solvable
    gcd, x0, y0 := ExtendedGCD(a, b)
    if N%gcd != 0 {
        fmt.Printf("No solution exists for %d*%d + %d*%d = %d\n", a, x0, b, y0, N)
        return
    }

    // Step 2: Scale the solution
    scale := N / gcd
    x0 *= scale
    y0 *= scale

    // Step 3: Determine step sizes
    stepX := b / gcd
    stepY := a / gcd

    // Step 4: Find range of k for positive solutions
    // x > 0: x0 + k * stepX > 0 --> k > -x0 / stepX
    // y > 0: y0 - k * stepY > 0 --> k < y0 / stepY
    kMin := int(math.Ceil(float64(-x0) / float64(stepX)))
    kMax := int(math.Floor(float64(y0) / float64(stepY)))

    fmt.Printf("Particular solution: x = %d, y = %d\n", x0, y0)
    fmt.Println("Positive integer solutions:")

    // Step 5: Generate solutions within the range
    for k := kMin; k <= kMax; k++ {
        x := x0 + k*stepX
        //y := y0 - k*stepY
        
        res = append(res, x) 
        //fmt.Printf("x = %d, y = %d\n", x, y)
    }
    return res
}

func extractNumbers(input string) ([]int) {
    re := regexp.MustCompile(`[+=](\d+)`)

    // Find all matches
    matches := re.FindAllStringSubmatch(input, -1)

    // Extract the numbers
    var numbers []int
    for _, match := range matches {
        if len(match) > 1 {
            num, err := strconv.Atoi(match[1])
            if err == nil {
                numbers = append(numbers, num)
            }
        }
    }

    return numbers
}
