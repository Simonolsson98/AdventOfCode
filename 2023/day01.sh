#!/bin/bash
input="$(dirname `which $0`)/day01_input.txt"
number=0

while IFS= read -r line
do
    length=${#line}
    firstnum=""
    lastnum=""
    for ((i = 0; i < length+1; i++)); do
        char="${line:i:1}"

        if [[ "$char" =~ ^[0-9]+$ ]]; then
            firstnum=$char
            break
        fi
    done

    for (( i = length - 2; i >= 0; i--)); do
        char="${line:i:1}"
        if [[ "$char" =~ ^[0-9]+$ ]]; then
            lastnum=$char
            break
        fi
    done

    number=$(( number + $firstnum$lastnum ))
done < "$input"

# part 1: 
printf "%s\n" "day1: bash solution for part 1: $number"

starttime=$(date +"%s")
number=0
declare -A myArray=(["one"]="1" ["two"]="2" ["three"]="3" ["four"]="4" ["five"]="5" ["six"]="6" ["seven"]="7" ["eight"]="8" ["nine"]="9")
while IFS= read -r line
do
    substr=""
    length=${#line}
    firstnum=""
    lastnum=""
    for ((i = 0; i < length+1; i++)); do
        char="${line:i:1}"

        if [[ "$char" =~ ^[0-9]+$ ]]; then
            firstnum=$char
            break
        else
            substr=$substr$char
            for key in "${!myArray[@]}"; do
                if [[ "$substr" == *"$key"* ]]; then
                    firstnum=${myArray[$key]}
                    break
                fi
            done
            if [[ $firstnum != "" ]]; then
                break
            fi
        fi
    done

    substr=""
    for (( i = length - 2; i >= 0; i--)); do
        char="${line:i:1}"
        if [[ "$char" =~ ^[0-9]+$ ]]; then
            lastnum=$char
            break
        else
            substr=$char$substr
            for key in "${!myArray[@]}"; do
                if [[ "$substr" == *"$key"* ]]; then
                    lastnum=${myArray[$key]}
                    break
                fi
            done
        fi
        if [[ $lastnum != "" ]]; then
            break
        fi
    done

    number=$(( number + $firstnum$lastnum ))
done < "$input"

# part 2: 
printf "%s\n" "day1: bash solution for part 2: $number"