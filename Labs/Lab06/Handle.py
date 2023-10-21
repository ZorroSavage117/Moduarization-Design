import json
import os
import Globals

def get_filename():
    while True:
        print("What file is the game saved to? (ends in .json)")
        filename = input("> ")
        try:
            with open(filename, "r") as f:
                return filename  # If the file exists, return its name
        except FileNotFoundError:
            print("File does not exist. Please check spelling.")
        print(f"Debug: file variable contains '{filename}'")

def load_file(filename):
    with open(filename, "r") as file_data:
        data = json.load(file_data)
    board = data.get("board")
    return board

def save_file():
    filename = Globals.Filename
    board = Globals.Board
    print("<Save Game Menu>")
    print(f"Current save file is '{filename}'")
    print("Do you wish to save here(1) or to a diffent file(0)?")
    cont = int(input("> "))
    if cont == 1:
        data = {"board": board} 
        with open(filename, "w") as file_data:
            json.dump(data, file_data)
    else:
        print("Enter a file name that you wish to save to. (Please have it end in .json)")
        filename = input("> ")
        try:
            with open(filename, "r") as f:
                print("This file alread exist. Do you wish to overwite it?(1/0)")
                cont = int(input("> "))
                if cont == 1:
                    data = {"board": board} 
                    with open(filename, "w") as file_data:
                        json.dump(data, file_data)
        except FileNotFoundError:
            file_new = filename.split('.')[0]
            data = {"board": board}
            with open(file_new, "w") as file_data:
                json.dump(data, file_data)
            filename = file_new + ".json"
    
    print(f"File saved to '{filename}'")

script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)