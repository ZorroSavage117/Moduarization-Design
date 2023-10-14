import Rules
import Handle
import Lab05
import Misc

def display_board(board):
    print("   A B C D E F G H I")
    for row in range(9):
        if row % 3 == 0:
            print("   -----+-----+-----")

        print(row + 1, end=' ')
        for col in range(9):
            if col % 3 == 0:
                print("|", end='')
            else:
                print(" ", end='')

            cell = board[row][col]
            if cell == 0:
                print(" ", end='')
            else:
                print(cell, end='')

        print("|")

    print("   -----+-----+-----")

def place_on_board(board, filename):
    loc = get_location(board, filename)
    if loc == False:
        return False
    try:
        num = get_num(loc)
    except TypeError:
        return board
    col = loc[0]
    row = loc[1]

    # if Rules.check_row(board, col, num) and Rules.check_column(board, row, num) and Rules.check_square(board, col, row, num):
    #     board[col][row] = num
    # else:
    #     print("That number doesn't go there.")

    board[col][row] = num
    
    return board

def get_location(board, filename):
    while True:
        location = input("Enter a location (e.g., A1, B2) or 'Q' to quit: ")
        if location == "Q":
            return quit_game(board, filename) 
        elif len(location) < 2:
            print(f"ERROR: Square {location} is invalid")
        else:
            column = Misc.convert(location[0])
            row = int(location[1]) - 1

            if Rules.check_location1(row, location[0]) and Rules.check_location2(board, row, column):
                return [row, column]
            
def quit_game(board, filename):
    # print("test - quit_game")
    # print(f"quit_game.Filename2 = {filename}")
    Handle.save_file(filename, board)
    print("Do you wish to quit(1) or run a different game file(0)?")
    cont = int(input("> "))
    if cont == 1:
        return False
    else:
        Lab05.main(True)

def get_num(location):
    loc = Misc.re_convert(location[1]) + str(location[0] + 1)
    while True:
        num = input(f"What is the value at '{loc}': ")
        if Rules.valid_input(num):
            if num == "S":
                helper(location)
            else:
                return int(num)

def helper(row, column):
    print("test - helper")