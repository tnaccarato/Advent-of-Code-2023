example = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


def lowest_location_number(input_string):
    # Splits the input string into categories
    input_string = input_string.split("\n\n")

    # Declares variables for storing a list each of the categories
    seeds = [int(seed) for seed in input_string[0][7:].split(" ")]
    seed_to_soil = [[int(num) for num in row.split(" ")] for row in input_string[1].split("\n")[1:]]
    soil_to_fert = [[int(num) for num in row.split(" ")] for row in input_string[2].split("\n")[1:]]
    fert_to_water = [[int(num) for num in row.split(" ")] for row in input_string[3].split("\n")[1:]]
    water_to_light = [[int(num) for num in row.split(" ")] for row in input_string[4].split("\n")[1:]]
    light_to_temp = [[int(num) for num in row.split(" ")] for row in input_string[5].split("\n")[1:]]
    temp_to_humid = [[int(num) for num in row.split(" ")] for row in input_string[6].split("\n")[1:]]
    humid_to_loc = [[int(num) for num in row.split(" ")] for row in input_string[7].split("\n")[1:]]

    # Declares a set for storing the location numbers
    location_numbers = set()

    # Loops through the seeds, getting the location number
    for seed in seeds:
        soil = convert_number(seed, seed_to_soil)
        fertilizer = convert_number(soil, soil_to_fert)
        water = convert_number(fertilizer, fert_to_water)
        light = convert_number(water, water_to_light)
        temperature = convert_number(light, light_to_temp)
        humidity = convert_number(temperature, temp_to_humid)
        location = convert_number(humidity, humid_to_loc)
        location_numbers.add(location)

    return min(location_numbers)



def convert_number(number, mapping):
    for destination_start, source_start, range_length in mapping:
        # Check if the number is within the current source range
        if source_start <= number < source_start + range_length:
            # Calculate the offset of the number from the start of the source range
            offset = number - source_start
            # Apply the same offset to the destination range
            return destination_start + offset
    # If the number does not fall within any source range, it maps to itself
    return number

with open("input.txt", "r") as input_string:
    input_string = input_string.read()
    print(lowest_location_number(input_string))