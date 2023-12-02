import os

def part(part_num):
    arr = {"red": 12, "green": 13, "blue": 14}
    saved_impossible_games = 0
    total_games = 0
    part2result = 0

    with open(os.path.dirname(__file__)+"/day02_input.txt", 'r') as input_text:
        for line in input_text:
            minarr = {"red": 0, "green": 0, "blue": 0}
            gamenumber = line.split(':')
            current_game_num = int(''.join(filter(str.isdigit, gamenumber[0])))
            total_games += current_game_num
            grabbed_colors_per_iteration = gamenumber[1].split(';')

            for key in grabbed_colors_per_iteration:
                grabbed_colors = key.split(', ')
                for individual_grabbed_color in grabbed_colors:
                    num, color = individual_grabbed_color.split()
                    num = int(num)

                    # part 1
                    if part_num == "1" and arr[color] < num:
                        saved_impossible_games += current_game_num
                        break

                    # part 2
                    if part_num == "2" and minarr[color] < num:
                        minarr[color] = num

                if part_num == "1" and arr[color] < num:
                    break

            # part 2
            if part_num == "2":
                subtot = 1
                for i in minarr.values():
                    subtot *= i
                part2result += subtot

    if part_num == "1":
        result = total_games - saved_impossible_games
        print(f"day1: Python solution for part 1: {result}")
    elif part_num == "2":
        print(f"day1: Python solution for part 2: {part2result}")

part("1")
part("2")