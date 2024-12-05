package main

import (
    "fmt"
    "strings"
    "os"
    "2024/utils"
    "strconv"
    "path/filepath"
)

func main() {
    inputFile := strings.Split(filepath.Base(os.Args[0]), ".")[0] + "_input"
    input, err := utils.ReadInput(inputFile)
    if err != nil {
        fmt.Println("Error reading input:", err)
        return
    }

    // Split the input on double newlines
    parts := strings.Split(input, "\n\n")
    rules := strings.Split(parts[0], "\n")
    inputRows := strings.Split(parts[1], "\n")

    // Create root node
    var root *TreeNode = &TreeNode{Value: -1}
    for _, rule := range rules {
        res := strings.Split(rule, "|")
        firstNum, _ := strconv.Atoi(res[0])
        secondNum, _ := strconv.Atoi(res[1])

        // Find all nodes with the value of firstNum
        foundNodes := root.FindAllNodes(firstNum)

        if len(foundNodes) == 0 {
            // If no node is found with firstNum, create a new root node and add the child
            newRoot := &TreeNode{Value: firstNum}
            child := &TreeNode{Value: secondNum}
            newRoot.AddChild(child)
            root.AddChild(newRoot)
        } else {
            // Add the secondNum as a child of all found nodes with value firstNum
            for _, foundNode := range foundNodes {
                if secondNum == 53 {
                    fmt.Println("ADDING 53 to this: ", foundNode.Value)
                }
                child := &TreeNode{Value: secondNum}
                foundNode.AddChild(child)
            }
        }
    }

    var asd []string
    for _, inputRow := range inputRows {
        ok := true
        currNode := root
        nums := strings.Split(inputRow, ",")
        for _, num := range nums {
            realNum, _ := strconv.Atoi(num)
            fmt.Println("looking for node with val: ", realNum, "looking from node:", currNode.Value)
            nextNode := currNode.FindNode(realNum)
            if nextNode == nil {
                ok = false
                fmt.Println("didn't find node: ", realNum)
                break
            }

            currNode = nextNode
        }

        if ok {
            fmt.Println("ok")
            asd = append(asd, inputRow)
        }
    }

    // Print the tree structure
    root.PrintTree("")

    fmt.Println("Day 5 Solution (Part 1):")
    fmt.Println("Day 5 Solution (Part 2):")
}

// TreeNode represents a single node in the tree
type TreeNode struct {
    Value    int          // The value of the node
    Children []*TreeNode  // Slice of child nodes
}

func (n *TreeNode) AddChild(child *TreeNode) {
    n.Children = append(n.Children, child)
}

func (n *TreeNode) PrintTree(indent string) {
    fmt.Println(indent + strconv.Itoa(n.Value))
    for _, child := range n.Children {
        child.PrintTree(indent + "    ")
    }
}

// FindNode finds the first node in the tree with the specified value using BFS
func (n *TreeNode) FindNode(value int) *TreeNode {
    // Create a queue for BFS
    queue := []*TreeNode{n}

    // Process nodes in the queue
    for len(queue) > 0 {
        // Dequeue the first node
        current := queue[0]
        queue = queue[1:]

        // Check if the current node matches the value
        if current.Value == value {
            return current
        }

        // Enqueue all the children of the current node
        queue = append(queue, current.Children...)
    }

    // Return nil if the value is not found
    return nil
}

// FindAllNodes finds all nodes in the tree with the specified value using BFS
func (n *TreeNode) FindAllNodes(value int) []*TreeNode {
    var result []*TreeNode
    queue := []*TreeNode{n}

    // Process nodes in the queue
    for len(queue) > 0 {
        // Dequeue the first node
        current := queue[0]
        queue = queue[1:]

        // Check if the current node matches the value
        if current.Value == value {
            result = append(result, current)
        }

        // Enqueue all the children of the current node
        queue = append(queue, current.Children...)
    }

    // Return the list of matching nodes
    return result
}
