#!/bin/bash
input="$(dirname `which $0`)/day02_input.txt"

part(){
    declare -A arr=(["red"]="12" ["green"]="13" ["blue"]="14")
    saved_impossible_games=0
    total_games=0
    declare -A minarr
    
    while IFS= read -r line
    do
        minarr=(["red"]="0" ["green"]="0" ["blue"]="0")
        IFS=':' read -ra gamenumber <<< "$line"
        current_game_num=$(echo "${gamenumber[0]}" | grep -oE "[0-9]{1,3}")
        total_games=$(( total_games + current_game_num ))
        IFS=';' read -ra grabbed_colors_per_iteration <<< "${gamenumber[1]}"

        for key in "${grabbed_colors_per_iteration[@]}"; do
            IFS=', ' read -ra grabbed_colors <<< "$key"
            individual_grabbed_color=$(echo ${grabbed_colors[@]} | grep -oE "[0-9]{1,2} [a-zA-Z]{3,5}")
            IFS=$'\n' number_color_splits=($individual_grabbed_color)
            for num_cols in ${number_color_splits[@]}; do
                IFS=' ' read -ra num_col <<< "$num_cols"
                num=${num_col[0]}
                color=${num_col[1]}

                # part 1
                if [[ "$1" == "1" && ${arr[$color]} -lt $num ]]; then
                    saved_impossible_games=$(( $saved_impossible_games + $current_game_num ))
                    breakouter=yes
                    break
                fi

                # part 2:
                if [[ $1 == "2" && ${minarr[$color]} -lt $num ]]; then
                    minarr[$color]=$num
                fi
            done

            if [[ $breakouter != "" ]]; then
                breakouter=""
                break
            fi
        done

        # part 2:
        if [[ "$1" == "2" ]]; then
            subtot=1
            for i in "${minarr[@]}"; do
                subtot=$(($subtot * i))
            done
            part2result=$(( part2result + subtot ))
        fi
    done < "$input"
}

# part 1: 
part "1"
result=$(( total_games - saved_impossible_games ))
printf "%s\n" "day1: bash solution for part 1: $result"

## part 2: 
part "2"
printf "%s\n" "day1: bash solution for part 2: $part2result"