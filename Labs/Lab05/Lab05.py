# 1. Name:
#      Arlo Jolley
# 2. Assignment Name:
#      Lab 05 : Sudoku Draft
# 3. Assignment Description:
#      Play a game of sudoku where the rules are not in full effect, can open and save to file 
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was getting data to tranced from one file to another with out issue or passing it as 
#       a paramater but it ultimily failed and I have an idea on how to fix it but even that may not work.
# 5. How long did it take for you to complete the assignment?
#      It took me about 10 hours where most of it was spent debugging, it took about 2 hours to convert most of the 
#       code from psedocode to python and the rest trying to figgure out the data passing.
#   youtube link: https://www.youtube.com/watch?v=Afh6yi7_mlU

import Handle
import Game
import Rules

Filename = ""
Board = [[]]
Game_p = True

def main(start=True):
    global Filename
    global Board
    global Game_p
    if start:
        set_game()
        start = False

    # print(f"main.Filename = {Filename}")
    # print(f"main.Board = {Board}")

    while Game_p:
        Game.display_board(Board)
        board = Game.place_on_board(Board, Filename)
        if board == False:
            Game_p = False;
        else:
            Board = board
        if Rules.game_done(Board):
            print("The board is full")
            # add code to see if it is correct for the final
            Game_p = Game.quit_game(Board, Filename)

def set_game():
    global Filename
    global Board
    Filename = Handle.get_filename()
    Board = Handle.load_file(Filename)
    # print(f"set_game.Filename = {Filename}")

if __name__ == "__main__":
    main()