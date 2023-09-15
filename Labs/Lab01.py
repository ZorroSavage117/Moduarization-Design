# 1. Name:
#      Arlo Jolley
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was the saving to and reading from a json file. The rest of it whent fine.
# 5. How long did it take for you to complete the assignment?
#      5 hours
# Youtube video link: https://www.youtube.com/watch?v=P_mhaZ62Qe4

import json

def main():
    # The characters used in the Tic-Tac-Too board.
    # These are constants and therefore should never have to change.
    X = 'X'
    O = 'O'
    BLANK = ' '

    # A blank Tic-Tac-Toe board. We should not need to change this board;
    # it is only used to reset the board to blank. This should be the format
    # of the code in the JSON file.
    blank_board = {  
                "board0": [
                    BLANK, BLANK, BLANK,
                    BLANK, BLANK, BLANK,
                    BLANK, BLANK, BLANK ]
            }
    try:
        with open("data.json", 'r') as json_file:
            works = json.load(json_file)
    except FileNotFoundError:
        with open("data.json", "w") as json_file:
            json.dump(blank_board, json_file)

    def read_board(filename):
        '''Read the previously existing board from the file if it exists.'''
        # Put file reading code here.
        with open(filename, "r") as game_file:
            data_content = game_file.read()
        game_board = json.loads(data_content)
        # print(game_board)
        try:
            if game_done(game_board['board1']):
                return game_board['board0']
            else:
                return game_board['board1']
        except KeyError:
            return game_board['board0']

    def save_board(filename, board):
        '''Save the current game to a file.'''
        # Put file writing code here.
        with open(filename, "r") as json_file:
            existing_data = json.load(json_file)
        
        existing_data["board1"] = board

        with open(filename, "w") as json_file:
            json.dump(existing_data, json_file)


    def display_board(board):
        '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
        # print(board)
        print(f" {board[0]} | {board[1]} | {board[2]} ")
        print("---+---+---")
        print(f" {board[3]} | {board[4]} | {board[5]} ")
        print("---+---+---")
        print(f" {board[6]} | {board[7]} | {board[8]} ")
        

    def is_x_turn(round):
        '''Determine whose turn it is.'''
        # Put code here determining if it is X's turn.
        
        if round % 2 == 0:
            return False
        else:
            return True

    def board_update(board, location, player):
        '''Updates the list/distonary with the new location of X or O'''
        location -= 1
        board[location] = player

    def play_game(board):
        '''Play the game of Tic-Tac-Toe.'''
        # Put game play code here. Return False when the user has indicated they are done.
        # Varables
        game_run = True
        round = 0
        location = 0

        # Game loop
        while(game_run):
            display_board(board)
            round += 1
            if is_x_turn(round):
                location = input("X> ")
                player = X
            else:
                location = input("O> ")
                player = O
            
            if location == "q":
                break
            else:
                board_update(board, int(location), player)
            # print(board)
            
            game_run = not(game_done(board, True))

        save_board("data.json", board)
            
        return False

    def game_done(board, message=False):
        '''Determine if the game is finished.
        Note that this function is provided as-is.
        You do not need to edit it in any way.
        If message == True, then we display a message to the user.
        Otherwise, no message is displayed. '''

        # Game is finished if someone has completed a row.
        for row in range(3):
            if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
                if message:
                    print("The game was won by", board[row * 3])
                return True

        # Game is finished if someone has completed a column.
        for col in range(3):
            if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
                if message:
                    print("The game was won by", board[col])
                return True

        # Game is finished if someone has a diagonal.
        if board[4] != BLANK and (board[0] == board[4] == board[8] or
                                board[2] == board[4] == board[6]):
            if message:
                print("The game was won by", board[4])
            return True

        # Game is finished if all the squares are filled.
        tie = True
        for square in board:
            if square == BLANK:
                tie = False
        if tie:
            if message:
                print("The game is a tie!")
            return True


        return False

    # These user-instructions are provided and do not need to be changed.
    print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
    print("where the following numbers correspond to the locations on the grid:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 \n")
    print("The current board is:")

    # The file read code, game loop code, and file close code goes here.
    game = read_board("data.json")

    play_game(game)
    print()
    again = int(input("Continue? (0/1): "))
    if again == 1:
        main()
    

if __name__ == "__main__":
    main()