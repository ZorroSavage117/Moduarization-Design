import Rules
import Handle
import Lab06
import Misc
import Globals
import sys

def display_board():
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

            cell = Globals.Board[row][col]
            if cell == 0:
                print(" ", end='')
            else:
                print(cell, end='')

        print("|")

    print("   -----+-----+-----")

def place_on_board():
    loc = get_location()
    
    num = get_num(loc)
    
    col = loc[1]
    row = loc[0]

    if Rules.check_row(row, num) and Rules.check_column(col, num) and Rules.check_square(row, col, num):
        Globals.Board[row][col] = num
    else:
        print("That number doesn't go there.")
    
def get_location():
    while True:
        location = input("Enter a location (e.g., A1, B2) or 'Q' to quit: ")
        if location.upper() == "Q":
            quit_game() 
        elif len(location) != 2:
            print(f"ERROR: Square '{location}' is invalid")
        else:
            try:
                row = int(location[0]) - 1
                column = Misc.convert(location[1])
            except ValueError:
                column = Misc.convert(location[0])
                row = int(location[1]) - 1

            if Rules.check_location1(row, column) and Rules.check_location2(row, column):
                return [row, column]
            
def quit_game():
    Handle.save_file()
    print("Do you wish to quit(1) or run a different game file(0)?")
    cont = int(input("> "))
    if cont == 1:
        sys.exit()
    else:
        Lab06.main(True)

def get_num(location):
    loc = Misc.re_convert(location[1]) + str(location[0] + 1)
    while True:
        num = input(f"What is the value at '{loc}': ")
        if Rules.valid_input(num):
            if num.upper() == "S":
                helper(location)
            else:
                num = int(num)
                row = location[0]
                col = location[1]
                if Rules.check_square(row, col, num, True) and Rules.check_column(col, num, True) and Rules.check_row(row, num, True):
                    return num

def helper(location):
    row = location[0]
    col = location[1]
    possible = []
    print("<Helper>")
    for num in range(1, 10):
        if Rules.check_row(row, num) and Rules.check_column(col, num) and Rules.check_square(row, col, num):
            possible.append(num)
    print(f"Possible numbers: {possible}")