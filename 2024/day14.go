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
)

func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

    start := time.Now()

    xrange := 103
    yrange := 101
    seconds := 100
    quadrant1 := 0
    quadrant2 := 0
    quadrant3 := 0
    quadrant4 := 0
    for _, line := range strings.Split(input, "\n") {
        re := regexp.MustCompile(`-?\d+`)
        matches := re.FindAllStringSubmatch(line, -1)
        // inverse coordinates for some reason
        ypos, _ := strconv.Atoi(matches[0][0])
        xpos, _  := strconv.Atoi(matches[1][0])
        yvel, _  := strconv.Atoi(matches[2][0])
        xvel, _  := strconv.Atoi(matches[3][0])
        // extra mod to prohibit negative numbers, since % in golang allows this..
        newxPos := ((seconds * xvel + xpos) % xrange + xrange) % xrange
        newyPos := ((seconds * yvel + ypos) % yrange + yrange) % yrange

        if newxPos < xrange / 2{
            if newyPos < yrange/2 {
                // first quad
                quadrant1 += 1
            } else if newyPos > yrange/2{
                // second quad
                quadrant2 += 1
            }
        } else if newxPos > xrange/2 {
            if newyPos < yrange/2 {
                // third quad
                quadrant3 += 1
            } else if newyPos > yrange/2  {
                // fourth quad
                quadrant4 += 1
            }
        }
    }

    fmt.Println(quadrant1, quadrant2, quadrant3, quadrant4)
    fmt.Println("Day 14 Solution (Part 1):", quadrant1 * quadrant2 * quadrant3 * quadrant4)
    fmt.Println("Part 1 execution time:", time.Since(start), "\n")

	start = time.Now()
	// exec part2()
    fmt.Println("Day 14 Solution (Part 2):")
    fmt.Println("Part 2 execution time:", time.Since(start))
}
