def part_sum(input_string):
    # Convert the input string into a 2D array (grid) of characters
    grid = [list(line) for line in input_string.split("\n")]

    # Initialize the sum of part numbers
    total_sum = 0

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


with open("input.txt", "r") as input_text:
    input_text = input_text.read()
    print(part_sum(input_text))
