def display_board(board):
    print("   A B C D E F G H I")
    for row in range(9):
        if row % 3 == 0:
            print("   -----+-----+-----")

        print(row + 1, end=' ')  # Print row number
        for col in range(9):
            if col % 3 == 0:
                print("|", end='')  # Adjusted spacing for vertical separator within 3x3 subgrid
            else:
                print(" ", end='')  # Adjusted spacing for cell content

            cell = board[row][col]
            if cell == ' ':
                print(" ", end='')  # Adjusted spacing for empty cell
            else:
                print(cell, end='')  # Adjusted spacing for the cell value

        print("|")  # Print vertical separator at the end of the row

    print("   -----+-----+-----")

# Example usage:
# Replace this with your actual Sudoku board
sample_board = [
    ['7', '2', '3', ' ', ' ', ' ', '1', '5', '9'],
    ['6', ' ', ' ', '3', ' ', '2', ' ', ' ', '8'],
    ['8', ' ', ' ', '1', ' ', ' ', ' ', ' ', '2'],
    [' ', ' ', '7', '6', '5', '4', ' ', '2', ' '],
    [' ', ' ', '4', '2', ' ', '7', '3', ' ', ' '],
    [' ', ' ', '5', '9', '3', '1', ' ', '4', ' '],
    ['5', ' ', ' ', '7', ' ', ' ', ' ', ' ', '3'],
    ['4', ' ', ' ', '1', ' ', '3', ' ', ' ', '6'],
    ['9', '3', '2', ' ', ' ', ' ', '7', '1', '4']
]

display_board(sample_board)
