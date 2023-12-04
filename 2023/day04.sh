#!/bin/bash

result=0
part2res=0
numdict=(["1"]=1)
input="$(dirname `which $0`)/day04_input.txt"
line_number=1
part(){
    while IFS= read -r line || [[ -n "$line" ]]; do
        if [ "${numdict[$line_number]+abc}" ]; then
            number_of_cards=${numdict[$line_number]}
        else
            number_of_cards=1
        fi

        IFS=':' read -ra splits <<< "$line"
        IFS='|' read -ra numbersplits <<< "${splits[1]}"
        read -ra winningnumbers <<< "$(sed 's/^[[:space:]]*//;s/[[:space:]]*$//' <<< "${numbersplits[0]}")"
        read -ra havenumbers <<< "$(sed 's/^[[:space:]]*//;s/[[:space:]]*$//' <<< "${numbersplits[1]}")"

        if [ "$1" = "1" ]; then
            for ((i = 0; i < number_of_cards; i++)); do
                score=0
                for num in "${havenumbers[@]}"; do
                    found=0
                    for winnum in "${winningnumbers[@]}"; do
                        if [ "$num" = "$winnum" ]; then
                            found=1
                            break
                        fi
                    done
                    if [ "$found" -eq 1 ]; then
                        if [ "$score" -eq 0 ]; then
                            score=1
                        else
                            score=$((score * 2))
                        fi
                    fi
                done
                result=$((result + score))
            done
        fi
        if [ "$1" = "2" ]; then
            part2res=$((part2res + number_of_cards))

            numberofwinningcards=0
            for winnum in "${winningnumbers[@]}"; do
                for num in "${havenumbers[@]}"; do
                    if [ "$winnum" = "$num" ]; then
                        ((numberofwinningcards++))
                        break  # Breaks inner loop if match found
                    fi
                done
            done

            for ((index = 1; index <= numberofwinningcards; index++)); do
                next_card=$((line_number + index))
                if [ "${numdict[$next_card]+abc}" ]; then
                    numdict[$next_card]=$((numdict[$next_card] + number_of_cards))
                else
                    numdict[$next_card]=$((number_of_cards + 1))
                fi
            done

        fi
        ((line_number++))

    done < "$input"

    if [ "$1" = "1" ]; then
        echo "day4: Bash solution for part 1: $result"
    elif [ "$1" = "2" ]; then
        echo "day4: Bash solution for part 2: $part2res"
    fi
}

part "1"
part "2"
