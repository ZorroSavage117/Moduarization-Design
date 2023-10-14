import Misc

def check_row(board, row, num):
    for col in range(9):
        if board[row][col] == num:
            return False
    return True

def check_column(board, column, num):
    for row in range(9):
        if board[row][column] == num:
            return False
    return True

def check_square(board, row, column, num):
    square_row = (row // 3) * 3
    square_col = (column // 3) * 3

    for i in range(square_row, square_row + 3):
        for j in range(square_col, square_col + 3):
            if board[i][j] == num:
                return False
    return True

def check_location1(row, column_a):
    column = Misc.convert(column_a)
    if row < 0 or row > 8 or column < 0 or column > 8:
        print(f"ERROR: Square {column_a}{row + 1} is invalid")
        return False
    else:
        return True

def check_location2(board, row, column):
    if board[row][column] != 0:
        print(f"ERROR: Square {Misc.re_convert(column)}{row + 1} is filled")
        return False
    else:
        return True

def valid_input(num):
    if num not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'S']:
        print(f"ERROR: The value {num} is invalid")
        return False
    else:
        return True
    
def game_done(board):
    for row in board:
        if 0 in row:
            return False
    
    return True
