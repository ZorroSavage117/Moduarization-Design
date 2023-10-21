import Handle

Filename = ""
Board = [[]]

def set_game():
    global Filename
    global Board
    Filename = Handle.get_filename()
    Board = Handle.load_file(Filename)