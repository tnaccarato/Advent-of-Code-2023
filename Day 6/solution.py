import re

example = """Time:      7  15   30
Distance:  9  40  200"""


def ways_to_beat_record(string):
    # Declares a variable for storing the product of all the permutations
    total_ways = 1

    # Splits the string into time and distances
    times, record_distances = string.split("\n")
    # Defines a regex pattern for matching the numbers
    pattern = r'\d+'
    # Extracts numbers from each line and casts them to int
    times = [int(number) for number in re.findall(pattern, times)]
    record_distances = [int(number) for number in re.findall(pattern, record_distances)]

    # Maps each race time to a record distance
    races = list(zip(times, record_distances))

    for race in races:
        beat_record_time = 0  # Initialises counter for ways to beat record
        time = race[0]
        record = race[1]
        for hold_duration in range(time):  # Iterate through possible hold durations
            boat_speed = hold_duration
            travel_time = time - hold_duration
            distance_traveled = boat_speed * travel_time
            if distance_traveled > record:  # Check if the boat beats the record
                beat_record_time += 1
        total_ways *= beat_record_time  # Multiply the ways for this race with the total

    return total_ways


with open("input.txt", "r") as input_string:
    print(ways_to_beat_record(input_string.read()))
