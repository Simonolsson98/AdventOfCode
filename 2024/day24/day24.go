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

var (
    values map[string]int = make(map[string]int, 0)
    maxZ int = 45
)

func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

    splitInput := strings.Split(input, "\n\n")
    re := regexp.MustCompile(`([a-z0-9]{3})\s+(XOR|OR|AND)\s+([a-z0-9]{3})\s+->\s+([a-z0-9]{3})`)
    matches := re.FindAllStringSubmatch(splitInput[1], -1)
    for _, val := range strings.Split(splitInput[0], "\n") {
        splitVal := strings.Split(val, ": ")
        realValue, _ := strconv.Atoi(splitVal[1])
        values[splitVal[0]] = realValue
    }

    start := time.Now()
    for {
        var breakOuter bool = true
        for _, match := range matches {
            op1Val, firstOperand := values[match[1]]
            op2Val, secondOperand := values[match[3]]

            if !firstOperand || !secondOperand{
                continue
            }
            
            switch match[2] {
                case "AND":
                    if op1Val == 1 && op2Val == 1 {
                        values[match[4]] = 1    
                    } else {
                        values[match[4]] = 0
                    }
                case "OR":
                    if op1Val == 1 || op2Val == 1 {
                        values[match[4]] = 1    
                    } else {
                        values[match[4]] = 0
                    }
                case "XOR":
                    if op1Val + op2Val == 1 {
                        values[match[4]] = 1    
                    } else {
                        values[match[4]] = 0
                    }
                default:
                    panic("should not reach here")
            }       

            for i := 0; i <= maxZ; i++ { //z45 max
                var newVal string
                if i < 10 {
                    newVal = "0" + strconv.Itoa(i)
                } else {
                    newVal = strconv.Itoa(i)
                }

                _, exists := values["z" + newVal] 
                if !exists {
                    breakOuter = false
                    break
                }
            }

            if breakOuter{
                break
            }
        }

        if breakOuter{
            break
        }
    }


    res := ""
    for i := 0; i <= maxZ; i++ {
        var newVal string
        if i < 10 {
            newVal = "0" + strconv.Itoa(i)
        } else {
            newVal = strconv.Itoa(i)
        }

        res += strconv.Itoa(values["z" + newVal])
    }

    total := 0
    for i, bit := range strings.Split(res, "") {
        if bit == "1"{
            total += int(math.Pow(2, float64(i)))
        }
    }

    fmt.Println("Day 24 Solution (Part 1):", total)
    fmt.Println("Part 1 execution time:", time.Since(start))

    start = time.Now()
    // exec part 2
    fmt.Println("Day 24 Solution (Part 2):")
    fmt.Println("Part 2 execution time:", time.Since(start))
}