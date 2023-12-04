import os

def part(part_num):
    result = 0
    numdict={}
    with open(os.path.dirname(__file__)+"/day04_input.txt", 'r') as input_text:
        for number, line in enumerate(input_text):
            numbersplits = line.split(':')[1].split(' | ')
            winningnumbers=" ".join(numbersplits[0].split()).split(' ')
            havenumbers=" ".join(numbersplits[1].split()).split(' ')

            score=0
            numdict.update( {str(number): number })
            numberofwinningcards=0
            for num in havenumbers:
                if num in winningnumbers:
                    numberofwinningcards += 1
                    if score == 0:
                        score = 1
                    else:
                        score *= 2
            result += score

            for index in range(numberofwinningcards):
                numdict[str(number + index)] += 1


    if part_num == "1":
        print(f"day2: Python solution for part 1: {result}")
    elif part_num == "2":
        print(f"day2: Python solution for part 2: ")

part("1")
part("2")