import os

def part(part_num):
    result = 0
    numdict={"1": 1}
    with open(os.path.dirname(__file__)+"/day04_input.txt", 'r') as input_text:
        maxlines=198
        for card, line in enumerate(input_text, 1):
            try:
                number_of_iter = numdict[str(card)]
            except:
                number_of_iter = 1

            for _number_of_cards in range(number_of_iter):
                numbersplits = line.split(':')[1].split(' | ')
                winningnumbers=" ".join(numbersplits[0].split()).split(' ')
                havenumbers=" ".join(numbersplits[1].split()).split(' ')

                score=0
                numberofwinningcards=0
                for num in havenumbers:
                    if num in winningnumbers:
                        numberofwinningcards += 1
                        if score == 0:
                            score = 1
                        else:
                            score *= 2
                result += score

                if(numberofwinningcards == 0 and str(card) not in numdict):
                    print(f"NOT IN {str(card)}")
                    numdict.update( {str(card): 1 } )
                    break

                #print(f"numberofwinningcards: {numberofwinningcards} for {card}")
                for index in range(1, numberofwinningcards + 1):
                    if card + index <= maxlines + 1:
                        try: 
                            numdict.update( {str(card + index): numdict[str(card + index)] + 1} )
                        except KeyError: 
                            numdict.update( {str(card + index): 2 } )

    if part_num == "1":
        print(f"day2: Python solution for part 1: {result}")
    elif part_num == "2":
        print(f"day2: Python solution for part 2: {sum(numdict.values())}")

#part("1")
part("2")
# too low: 8477777
