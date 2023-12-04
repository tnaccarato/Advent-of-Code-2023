def part_sum(input_string):
    # Convert the input string into a 2D array (grid) of characters
    grid = [list(line) for line in input_string.split("\n")]

    # Initialize the sum of part numbers
    total_sum = 0

    # Iterate over each cell in the grid
    for row in range(len(grid)):
        col = 0
        while col < len(grid[row]):
            cell = grid[row][col]
            # Check if the cell contains a digit and is the start of a number
            if cell.isdigit() and (col == 0 or not grid[row][col - 1].isdigit()):
                # Form the number and get its length
                number, length = form_number(grid, col, row)
                # Check if the number is adjacent to any symbol
                if check_adjacent(grid, col, row, length):
                    # Add the number to the total sum
                    total_sum += number
                # Skip the cells that form the current number
                col += length
            else:
                # Move to the next cell
                col += 1

    return total_sum


def gear_sum(input_string):
    grid = [list(line) for line in input_string.split("\n")]

    total_gear_sum = 0

    def is_digit(cell):
        return cell.isdigit()

    # Find the entire number starting from a given cell
    def find_whole_number(grid, col, row):
        number = ""
        # Move left to the start of the number
        while col >= 0 and is_digit(grid[row][col]):
            col -= 1
        col += 1  # Move back to the first digit of the number
        # Form the whole number
        while col < len(grid[row]) and is_digit(grid[row][col]):
            number += grid[row][col]
            col += 1
        return int(number) if number else None

    def find_adjacent_numbers(grid, gear_col, gear_row):
        """Find distinct part numbers adjacent to a gear."""
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        adjacent_numbers = set()

        for dr, dc in directions:
            new_row, new_col = gear_row + dr, gear_col + dc
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and is_digit(grid[new_row][new_col]):
                number = find_whole_number(grid, new_col, new_row)
                if number is not None:
                    adjacent_numbers.add(number)

        return adjacent_numbers

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "*":
                adjacent_numbers = find_adjacent_numbers(grid, col, row)
                if len(adjacent_numbers) == 2:
                    gear_ratio = 1
                    for num in adjacent_numbers:
                        gear_ratio *= num
                    total_gear_sum += gear_ratio

    return total_gear_sum


def is_symbol(cell):
    """Check if a cell is a symbol (any character that is not a digit or a ".")"""
    return not cell.isdigit() and cell != "."


# Function to form a number starting from a given cell
def form_number(grid, start_col, row):
    """Form a number starting from a given cell"""
    number = ""
    col = start_col
    # Iterate horizontally to form the complete number
    while col < len(grid[row]) and grid[row][col].isdigit():
        number += grid[row][col]
        col += 1
    return int(number), col - start_col


def check_adjacent(grid, start_col, row, length):
    """Function to check if any part of a number is adjacent to a symbol"""
    # Directions relative to cell (up, down, left, right, diagonals)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for i in range(length):
        col = start_col + i
        for direction_row, direction_col in directions:
            new_row, new_col = row + direction_row, col + direction_col
            # Check if the adjacent cell is within grid bounds and is a symbol
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and is_symbol(grid[new_row][new_col]):
                return True
    return False


with open("input.txt", "r") as input_text:
    input_text = input_text.read()
    # print(part_sum(input_text))
    print(gear_sum(input_text))
