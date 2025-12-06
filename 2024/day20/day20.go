package main

import (
    "fmt"
    "strings"
    "os"
    "github.com/simonolsson98/adventofcode/utils"
    //"strconv"
    "path/filepath"
    "time"
    "slices"
)

type position struct {
    x int
    y int
}

type beforeend struct{
    before position
    after position
}

var (
    grid [][]string
    currPos position
    visited map[position]int
    xlength int
    ylength int
    DFSDoneValue int
    potentialCheatPaths []position
    posBeforeCheating position
    posAfterCheating position
    savedEndPositions map[beforeend]bool
    timeNoCheating int = 84 // CHANGE HERE
)

func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

    rows := strings.Split(input, "\n")
    xlength = len(rows)
    ylength = len(rows[0])

    for x, row := range rows {
        for y, char := range row {
            if char == 'S' {
                currPos = position{x, y}
            }

        }
        grid = append(grid, strings.Split(row, ""))
    }

    visited = make(map[position]int)
    for x := 0; x < len(grid); x++ {
        for y := 0; y < len(grid[x]); y++ {
            visited[position{x, y}] = 100000
            
            if grid[x][y] == "#" {
                if ((x-1 >= 0 && x + 1 < xlength) && (grid[x-1][y] == "." || grid[x-1][y] == "S" || grid[x-1][y] == "E") && 
                    (grid[x+1][y] == "." || grid[x+1][y] == "S" || grid[x+1][y] == "E")){
                    potentialCheatPaths = append(potentialCheatPaths, position{x, y})
                }

                if ((y-1 >= 0 && y + 1 < ylength) && (grid[x][y+1] == "." || grid[x][y+1] == "S" || grid[x][y+1] == "E") && 
                    (grid[x][y-1] == "." || grid[x][y-1] == "S" || grid[x][y-1] == "E")){
                    potentialCheatPaths = append(potentialCheatPaths, position{x, y})
                }
            }
        }
    }

    start := time.Now()
    
    DFS(0, currPos)
    timeNoCheating := DFSDoneValue
    savedAtleast100 := 0
    for _, potentialCheatPath := range potentialCheatPaths {
        x := potentialCheatPath.x
        y := potentialCheatPath.y

        for x := 0; x < len(grid); x++ {
            for y := 0; y < len(grid[x]); y++ {
                visited[position{x, y}] = 100000
            }
        }

        grid[x][y] = "."
        DFS(0, currPos)
        if (timeNoCheating - DFSDoneValue) >= 100{
            savedAtleast100 += 1
        }
        grid[x][y] = "#"
    }

    fmt.Println("Day 20 Solution (Part 1):", savedAtleast100)
    fmt.Println("Part 1 execution time:", time.Since(start))

    start = time.Now()

    origCurrPos := currPos
    savedEndPositions = make(map[beforeend]bool, 0)
    Part2DFS(0, origCurrPos, 0, false, []position{currPos}, currPos)

    // exec part 2
    fmt.Println("Day 20 Solution (Part 2):", len(savedEndPositions))
    fmt.Println("Part 2 execution time:", time.Since(start))
}

func DFS(count int, currPos position) {
    if grid[currPos.x][currPos.y] == "E" {
        if count < visited[position{currPos.x, currPos.y}] {
            visited[position{currPos.x, currPos.y}] = count
            DFSDoneValue = count
        }

        return
    }
    
    if visited[position{currPos.x, currPos.y}] <= count{
        return
    }

    visited[position{currPos.x, currPos.y}] = count
    neighbours := []position{
        position{currPos.x-1, currPos.y}, 
        position{currPos.x, currPos.y+1}, 
        position{currPos.x+1, currPos.y}, 
        position{currPos.x, currPos.y-1}}

    for _, neighbour := range neighbours {
        if  neighbour.x > xlength - 1 ||
            neighbour.x < 0 ||
            neighbour.y > ylength - 1 ||
            neighbour.y < 0 ||
            grid[neighbour.x][neighbour.y] == "#"{
            continue
        }
        
        DFS(count + 1, neighbour)
    }
}

func Part2DFS(count int, currPos position, cheatsUsed int, currentlyCheating bool, sliceVisited []position, posAfterCheating position) {
    // fmt.Println("for currPos:", currPos, "with count: ", count)
    // time.Sleep(10*time.Millisecond)
    if count > timeNoCheating - 72 {
        // fmt.Println("EARLY RETURN: ", currPos)
        return
    }

    if grid[currPos.x][currPos.y] == "E" {
        if currentlyCheating{
            posAfterCheating = currPos
        }
        DFSDoneValue = count
        fmt.Println("wut:", count, "pos:", posBeforeCheating, posAfterCheating)
        savedEndPositions[beforeend{posBeforeCheating, posAfterCheating}] = true

        return
    }

    neighbours := []position{
        position{currPos.x+1, currPos.y}, 
        position{currPos.x, currPos.y+1}, 
        position{currPos.x-1, currPos.y}, 
        position{currPos.x, currPos.y-1}}

    for _, neighbour := range neighbours {
        if slices.Contains(sliceVisited, position{neighbour.x, neighbour.y}) || 
            neighbour.x > xlength - 1 ||
            neighbour.x < 0 ||
            neighbour.y > ylength - 1 ||
            neighbour.y < 0 {
            continue
        }

        if grid[neighbour.x][neighbour.y] == "#"{
            if cheatsUsed > 20 {
                continue
            }

            if !currentlyCheating {
                posBeforeCheating = currPos
            }

            Part2DFS(count + 1, neighbour, cheatsUsed + 1, true, append(sliceVisited, neighbour), posAfterCheating)
        } else {
            if cheatsUsed <= 20{
                if !currentlyCheating {
                    posBeforeCheating = neighbour
                }

                Part2DFS(count + 1, neighbour, cheatsUsed + 1, true, append(sliceVisited, neighbour), posAfterCheating)
            }

            if currentlyCheating {
                posAfterCheating = position{neighbour.x, neighbour.y}
                cheatsUsed = 420
            }

            Part2DFS(count + 1, neighbour, cheatsUsed, false, append(sliceVisited, neighbour), posAfterCheating)
        }
    }

    // fmt.Println("DONE FOR:", currPos)
}