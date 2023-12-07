import os

def part(part_num):
    possible_cards = [str(i) for i in range(9, 1, -1)]
    values = [(i, []) for i in range(1,8)]
    possible_cards=["A", "K", "Q", "J", "T"] + possible_cards
    print(possible_cards)
    with open(os.path.dirname(__file__)+"/day07_input.txt", 'r') as input_text:
        while asd := input_text.readline():
            
            cards, bet = asd.split(" ")
            occurrences = []
            for i in possible_cards:
                occurrences.append(cards.count(i))

            new_order = ""
            for (card, count) in [(card, count) for (card, count) in zip(possible_cards, occurrences) if occurrences != 0]:
                new_order += card*count

            zeroes=occurrences.count(0)
            for i in range(zeroes):
                occurrences.remove(0)

            if(occurrences == [5]):
                values[6][1].append((cards, bet.rstrip()))
            elif(occurrences == [1, 4] or occurrences == [4, 1]):
                values[5][1].append((cards, bet.rstrip()))
            elif(occurrences == [2, 3] or occurrences == [3, 2]):
                values[4][1].append((cards, bet.rstrip()))
            elif(sorted(occurrences) == sorted([2, 3]) or sorted(occurrences) == sorted([1, 1, 3])):
                values[3][1].append((cards, bet.rstrip()))
            elif(sorted(occurrences) == sorted([2, 2, 1])):
                values[2][1].append((cards, bet.rstrip()))
            elif(sorted(occurrences) == sorted([2, 1, 1, 1])):
                values[1][1].append((cards, bet.rstrip()))
            elif(occurrences == [1, 1, 1, 1, 1]):
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
        print(f"day7: Python solution for part 2: {values}")

part("1")
#part("2")