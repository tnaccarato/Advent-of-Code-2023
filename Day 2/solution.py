import re

example = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


def possible_games_sum(string):
    # Gets a dictionary of the maximum colours of each game
    game_max_colours = get_max_colours(string)

    # Initialises a sum of the game IDs
    id_sum = 0

    # If the maximum colours in the game are less than or equal to the values given, adds the ID to the sum
    for game, max_colours in game_max_colours.items():
        if (
                max_colours["red"] <= 12 and
                max_colours["green"] <= 13 and
                max_colours["blue"] <= 14
        ):
            id_sum += game

    # Returns the sum of the ids after loop completes
    return id_sum


def sum_minimum_game_powers(string):
    game_max_colours = get_max_colours(string)

    # Initialises a sum of the game powers
    power_sum = 0
    # For each game sum, finds the power of the set and adds it to the sum
    for game, max_colours in game_max_colours.items():
        power = max_colours["red"] * max_colours["blue"] * max_colours["green"]
        power_sum += power

    # Returns the sum of the powers of each game
    return power_sum


def get_max_colours(string):
    # Splits the input into lines
    games = string.split("\n")
    # Defines a regex pattern to match the game number and then match everything after the colon
    pattern = r'Game (\d+): (.+?)(?=Game|$)'
    # Declares a dictionary storing the rounds
    game_max_colours = {}
    # Extracts the game number and the rounds
    for game in games:
        match = re.search(pattern, game)
        # Handles if no match can be found
        if match:
            # print(match)
            game_number = int(match.group(1))
            # print(game_number)
            game_data = match.group(2)
            colour_counts = re.findall(r'(\d+) (\w+)', game_data)
            max_colours = {}

            # Find the highest value of each colour
            for count, colour in colour_counts:
                count = int(count)
                if colour in max_colours:
                    max_colours[colour] = max(max_colours[colour], count)
                else:
                    max_colours[colour] = count

            # Adds the max values to the game dictionary
            game_max_colours[game_number] = max_colours
    return game_max_colours


# Testing examples
# print(possible_games_sum(example))
# print(sum_minimum_game_powers(example))

with open("input.txt", "r") as input_text:
    input_text = input_text.read()
    # print(possible_games_sum(input_text))
    print(sum_minimum_game_powers(input_text))