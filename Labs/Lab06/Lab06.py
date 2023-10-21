# 1. Name:
#      Arlo Jolley
# 2. Assignment Name:
#      Lab 06 : Sudoku Project
# 3. Assignment Description:
#      Play a game of sudoku where the rules are in full effect, can open and save to file 
# 4. What was the hardest part? Be as specific as possible.
#      Figuring out the global varables but I had an idea that I deside to try after playing around 
#       with other things and the debuger, which was to create a new file that they stayed in and 
#       they were updated in and the at is all that it does. Then I was playing around with my quit
#       game function and was having trouble getting it to kill the game, so I went online and looked 
#       up a way to kill the python script from deep with in. But I do know for sure that I am better 
#       at building code as I go and am terable at planing for every thing I may need to use or have.
# 5. How long did it take for you to complete the assignment?
#      About 6 hours
#   youtube link: https://www.youtube.com/watch?v=jebqQkTGRKA

import Game
import Rules
import Globals

def main(start=True):
    if start:
        Globals.set_game()
        start = False

    while True:
        Game.display_board()
        Game.place_on_board()
        if Rules.game_done():
            print("The board is full")
            if Rules.game_correct():
                print("The board has no errors and all rules where followed.")
            else:
                print("Somehow the board is full and it has not completely followed the rules.")
            Game.quit_game()

if __name__ == "__main__":
    main()