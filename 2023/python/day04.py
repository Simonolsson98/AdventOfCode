import os

def part(part_num):
    result = 0
    part2res = 0
    numdict={"1": 1}
    with open(os.path.dirname(__file__)+"/day04_input.txt", 'r') as input_text:
        for card, line in enumerate(input_text, 1):
            try:
                number_of_cards = numdict[str(card)] # iterate over copies if we have
            except:
                number_of_cards = 1 # we only have original card
            
            numbersplits = line.split(':')[1].split(' | ')
            winningnumbers=" ".join(numbersplits[0].split()).split(' ')
            havenumbers=" ".join(numbersplits[1].split()).split(' ')

            if(part_num == "1"):
                for _ in range(number_of_cards):
                    score=0
                    for num in havenumbers:
                        if num in winningnumbers:
                            if score == 0:
                                score = 1
                            else:
                                score *= 2
                    result += score

            if(part_num == "2"):
                part2res += number_of_cards # save cards
                numberofwinningcards=0
                for num in havenumbers:
                    if num in winningnumbers:
                        numberofwinningcards += 1

                for index in range(1, numberofwinningcards + 1):
                    maxlines=198
                    if card + index <= maxlines: # not really needed since it stops at the end of the input data anyways
                        try: 
                            numdict.update( {str(card + index): numdict[str(card + index)] + number_of_cards} ) #
                        except KeyError: 
                            numdict.update( {str(card + index): number_of_cards + 1 } ) # save copies + original card

    if part_num == "1":
        print(f"day4: Python solution for part 1: {result}")
    elif part_num == "2":
        print(f"day4: Python solution for part 2: {part2res}")

part("1")
part("2")