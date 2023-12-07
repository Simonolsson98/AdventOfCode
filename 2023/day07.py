import os

def part(part_num):
    possible_cards = [str(i) for i in range(9, 1, -1)]
    values = [(i, []) for i in range(1,8)]
    if(part_num == "1"):
        possible_cards=["A", "K", "Q", "J", "T"] + possible_cards
    else:
        possible_cards=["A", "K", "Q", "T"] + possible_cards + ["J"]
    with open(os.path.dirname(__file__)+"/day07_input.txt", 'r') as input_text:
        while asd := input_text.readline():
            cards, bet = asd.split(" ")
            
            occurrences = []
            for i in possible_cards:
                if(cards.count(i) == 0):
                    continue
                occurrences.append(cards.count(i))

            if(occurrences == [5]):
                if(part_num == "2" and (jokers := cards.count("J")) > 0):
                    values[6][1].append(("AAAAA", bet.rstrip()))
                else:
                    values[6][1].append((cards, bet.rstrip()))

            elif(occurrences == [1, 4] or occurrences == [4, 1]):
                if(part_num == "2" and (jokers := cards.count("J")) > 0):
                    if(jokers == 1):
                        specific_card = [card for card in cards if card != 'J']
                        cards = "".join(specific_card[0]*5)
                    else: #jokers == 4
                        specific_card = [card for card in cards if card != 'J']
                        cards = "".join(specific_card*5)
                else:
                    values[5][1].append((cards, bet.rstrip()))

            elif(occurrences == [2, 3] or occurrences == [3, 2]):
                if(part_num == "2" and (jokers := cards.count("J")) > 0):
                    if (jokers != 3):
                        specific_card = [card for card in cards if cards.count(card) == 3]
                        cards = cards.replace('J', specific_card[0])
                    elif (jokers == 3):
                        specific_card = [card for card in cards if cards.count(card) != 3]
                        cards = cards.replace('J', specific_card[0])
                else:
                    values[4][1].append((cards, bet.rstrip()))

            elif(sorted(occurrences) == sorted([1, 1, 3])):
                if(part_num == "2" and (jokers := cards.count("J")) > 0):
                    if(jokers == 1 or jokers == 2):
                        specific_card = [card for card in cards if cards.count(card) == 3]
                        cards = cards.replace('J', specific_card[0])
                    if(jokers == 3): # none of this in input data so idc
                        pass
                else:
                    values[3][1].append((cards, bet.rstrip()))

            elif(sorted(occurrences) == sorted([2, 2, 1])):
                if(part_num == "2" and (jokers := cards.count("J")) > 0):
                    if(jokers == 1):

                    elif (jokers == 2):
                        print(cards)
                        specific_card = [card for card in cards if cards.count(card) == 2 and card != 'J']
                        print(specific_card)
                        cards = cards.replace('J', specific_card[0])
                        print(cards)
                else:
                    values[2][1].append((cards, bet.rstrip()))

            elif(sorted(occurrences) == sorted([2, 1, 1, 1])):
                if(part_num == "2" and (jokers := cards.count("J")) > 0):
                    pass
                else:
                    values[1][1].append((cards, bet.rstrip()))

            elif(occurrences == [1, 1, 1, 1, 1]):
                if(part_num == "2" and (jokers := cards.count("J")) > 0):
                    pass
                else:
                    values[0][1].append((cards, bet.rstrip()))


        rank = 1
        result = []
        for index, val_bids in values:
            order = "".join(possible_cards[::-1])
            asd = [bids for bids in val_bids]
            sorted_ranks = sorted(asd, key=lambda word: [order.index(c) for c in word[0]])
            for val, bid in sorted_ranks:
                result.append(int(bid) * rank)
                rank += 1

    if part_num == "1":
        print(f"day7: Python solution for part 1: {sum(result)}")
    elif part_num == "2":
        print(f"day7: Python solution for part 2: {sum(result)}")

part("1")
part("2")