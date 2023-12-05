import re
from collections import defaultdict

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


def total_scratchcards(input_string):
    cards_data = []
    pattern = r"Card\s+\d+: ([\d\s]+) \| ([\d\s]+)"

    # Parse the input string to get card data
    for line in input_string.split("\n"):
        match = re.search(pattern, line)
        if match:
            winning_numbers = set(int(num) for num in match.group(1).split())
            chosen_numbers = set(int(num) for num in match.group(2).split())
            matches = len(winning_numbers.intersection(chosen_numbers))
            cards_data.append(matches)

    # Initialize counters for total cards and cards to be processed
    total_cards = len(cards_data)
    cards_to_process = defaultdict(int)  # Dict to store the number of times each card needs to be processed

    # Initial population of the cards_to_process dictionary
    for i, matches in enumerate(cards_data):
        for j in range(1, matches + 1):
            if i + j < len(cards_data):
                cards_to_process[i + j] += 1

    # Process the cards
    i = 0
    while i < len(cards_data):
        # If this card needs to be processed
        if cards_to_process[i] > 0:
            total_cards += cards_to_process[i]  # Add the number of copies
            matches = cards_data[i]

            # Schedule further copies based on matches
            for j in range(1, matches + 1):
                if i + j < len(cards_data):
                    cards_to_process[i + j] += cards_to_process[i]

            cards_to_process[i] = 0  # Reset the counter for this card

        i += 1

    return total_cards


with open("input.txt", "r") as input_text:
    input_text = input_text.read()
    print(total_scratchcards(input_text))
