import re

example = """Time:      7  15   30
Distance:  9  40  200"""


def ways_to_beat_record(string):
    # Splits the string into time and distances
    time, record_distance = string.split("\n")
    # Defines a regex pattern for matching the numbers
    pattern = r'\d+'
    # Extracts numbers from each line and casts them to int
    time = int("".join([number for number in re.findall(pattern, time)]))
    record_distance = int("".join([number for number in re.findall(pattern, record_distance)]))

    beat_record_time = 0  # Initialises counter for ways to beat record
    for hold_duration in range(time):  # Iterate through possible hold durations
        boat_speed = hold_duration
        travel_time = time - hold_duration
        distance_traveled = boat_speed * travel_time
        if distance_traveled > record_distance:  # Check if the boat beats the record
            beat_record_time += 1

    return beat_record_time


with open("input.txt", "r") as input_string:
    print(ways_to_beat_record(input_string.read()))
