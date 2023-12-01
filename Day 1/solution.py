import re


def sum_first_last_digit(file_path):
    total_sum = 0
    # Dictionary mapping number words to their digit equivalents
    numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    # Open the file and read it line by line
    with open(file_path, 'r') as file:
        for line in file:
            # Finds all the numbers
            nums = re.findall(r'(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))', line)
            # Assigns variables to first and last
            first = numbers.get(nums[0], nums[0])
            last = numbers.get(nums[-1], nums[-1])
            # Adds the integer value of the first and last digit of the line concatenated to the total_sum
            total_sum += int(first + last)

    # After looping through all the lines, returns the total_sum
    return total_sum


# Example usage
print(sum_first_last_digit("input.txt"))
