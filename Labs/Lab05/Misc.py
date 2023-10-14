def convert(location):
    column = location[0]
    if column == 'A':
        return 0
    elif column == 'B':
        return 1
    elif column == 'C':
        return 2
    elif column == 'D':
        return 3
    elif column == 'E':
        return 4
    elif column == 'F':
        return 5
    elif column == 'G':
        return 6
    elif column == 'H':
        return 7
    elif column == 'I':
        return 8
    else:
        return 9

def re_convert(column):
    if column == 0:
        return 'A'
    elif column == 1:
        return 'B'
    elif column == 2:
        return 'C'
    elif column == 3:
        return 'D'
    elif column == 4:
        return 'E'
    elif column == 5:
        return 'F'
    elif column == 6:
        return 'G'
    elif column == 7:
        return 'H'
    elif column == 8:
        return 'I'
    else:
        return 'Invalid'
