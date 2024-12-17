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

    splitInput := strings.Split(input, "\n\n")
    registerVals := splitInput[0]
    
    re := regexp.MustCompile(`\b([A-C])\b:\s+(\d+)`)
    matches := re.FindAllString(registerVals, -1)
    
    regAAndVal := strings.Split(matches[0], ": ")
    regBAndVal := strings.Split(matches[1], ": ")
    regCAndVal := strings.Split(matches[2], ": ")
    regAVal, _ := strconv.Atoi(regAAndVal[1])
    regBVal, _ := strconv.Atoi(regBAndVal[1])
    regCVal, _ := strconv.Atoi(regCAndVal[1])
    registers := map[string]int{regAAndVal[0]: regAVal, regBAndVal[0]: regBVal, regCAndVal[0]: regCVal}

    program := splitInput[1]
    opcodes := strings.Split(strings.Split(program, ": ")[1], ",")

    start := time.Now()
    printthis := ""
    for i := 0; i < len(opcodes); i+=2 {
        instr, _ := strconv.Atoi(opcodes[i])
        literaloperand, _ := strconv.Atoi(opcodes[i+1])

        combooperand := literaloperand
        if literaloperand == 4 {
            combooperand = registers["A"]
        } else if literaloperand == 5 {
            combooperand = registers["B"]
        } else if literaloperand == 6 {
            combooperand = registers["C"]
        }

        switch instr {
            case 0: // adv A / 2^literaloperand => A
                registers["A"] = int(float64(registers["A"]) / math.Pow(2.0, float64(combooperand)))
            case 1: // B xor literaloperand => B
                registers["B"] = registers["B"] ^ literaloperand
            case 2: // literaloperand % 8 => B
                registers["B"] = ((combooperand % 8) + 8) % 8
            case 3: // jump if A != 0
                if registers["A"] != 0{
                    i = literaloperand - 2
                }
            case 4: // B XOR C => B
                registers["B"] = registers["B"] ^ registers["C"]
            case 5: // 
                printthis = printthis + strconv.Itoa(((combooperand % 8) + 8) % 8) + ","
            case 6: // bdv A / 2^literaloperand => B
                registers["B"] = int(float64(registers["A"]) / math.Pow(2.0, float64(combooperand)))
            case 7: // cdv A / 2^literaloperand => C
                registers["C"] = int(float64(registers["A"]) / math.Pow(2.0, float64(combooperand)))
            default:
                panic("NOOOOOOOOOOO")
        }
    }

    printthis = strings.TrimRight(printthis, ",")
    fmt.Println("Day 17 Solution (Part 1):", printthis)
    fmt.Println("Part 1 execution time:", time.Since(start), "\n")

	start = time.Now()
	// exec part2()
    fmt.Println("Day 17 Solution (Part 2):")
    fmt.Println("Part 2 execution time:", time.Since(start))
}
