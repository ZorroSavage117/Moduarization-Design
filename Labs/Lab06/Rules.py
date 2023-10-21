import Misc
import Globals

def check_row(row, num, error_message=False):
    for col in range(9):
        if Globals.Board[row][col] == num:
            if error_message:
                print(f"That '{num}' is alread in that row.")
            return False
    return True

def check_column(column, num, error_message=False):
    for row in range(9):
        if Globals.Board[row][column] == num:
            if error_message:
                print(f"That '{num}' is alread in that column.")
            return False
    return True

def check_square(row, column, num, error_message=False):
    square_row = (row // 3) * 3
    square_col = (column // 3) * 3

    for i in range(square_row, square_row + 3):
        for j in range(square_col, square_col + 3):
            if Globals.Board[i][j] == num:
                if error_message:
                    print(f"That '{num}' is alread in that square.")
                return False
    return True

def check_location1(row, column):
    column_a = Misc.re_convert(column)
    if row < 0 or row > 8 or column < 0 or column > 8:
        print(f"ERROR: Square '{column_a}{row + 1}' is invalid")
        return False
    else:
        return True

def check_location2(row, column):
    if Globals.Board[row][column] != 0:
        print(f"ERROR: Square '{Misc.re_convert(column)}{row + 1}' is filled")
        return False
    else:
        return True

def valid_input(num):
    if num not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'S', 's']:
        print(f"ERROR: The value '{num}' is invalid")
        return False
    else:
        return True
    
def game_done():
    for row in Globals.Board:
        if 0 in row:
            return False
    
    return True

def game_correct():
    for row in range(9):
        for col in range(9):
            num = Globals.Board[row][col]
            if not check_row(row, num) or not check_column(col, num) or not check_square(row, col, num):
                return False
    return True
                