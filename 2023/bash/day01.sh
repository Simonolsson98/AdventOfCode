#!/bin/bash
input="./day01_input.txt"

starttime=$(date +"%s")
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

echo $number
echo "elapsed time in seconds: $(($(date +"%s")-$starttime))"

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

echo $number
echo "elapsed time in seconds: $(($(date +"%s")-$starttime))"