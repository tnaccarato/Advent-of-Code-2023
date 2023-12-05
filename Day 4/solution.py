import re

example = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

def points_sum(input_string):
    # Initialises a counter for the total point sum
    total_sum = 0
    # Splits the string into cards
    cards = input_string.split("\n")
    pattern = r"Card\s+\d+: ([\d\s]+) \| ([\d\s]+)"
    for card in cards:
        score = 0
        # Groups the pattern
        match = re.search(pattern, card)
        # Defines sets for winning numbers and chosen numbers
        winning_numbers = set([int(number) for number in match.group(1).split()])
        chosen_numbers = set([int(number) for number in match.group(2).split()])
        # Sums wins
        wins = sum(number in winning_numbers for number in chosen_numbers)
        if wins > 0:
            score = 2 ** (wins - 1)
        else:
            score = 0

        total_sum += score

    return total_sum


with open("input.txt", "r") as input_text:
    input_text = input_text.read()
    print(points_sum(input_text))