

width = 40
height = 17
border = '='
blank = ' '
snakeBody = '#'
snakeHead = '@'
simpleFood = "*"
specialFood = "%"
bgColor = 'red'
fgColor = 'black'

borderList = []

def init_list2D():
    '''
    Creates a 2D list with characters placed at correct indices
    '''

    wholeList = []
    # append rowLists to this to create 2D array

    # border = '='

    for r in range(height):
        row = []
        for c in range(width):
            """
            Inside this for loop, set conditions
            on the characters when starting the game
            """
            if r == 0 or r == height-1:
                # first row, and last row
                row.append(border)
                borderList.append((r, c))
            elif c == 0 or c == width-1:
                # first column and last column
                row.append(border)
                borderList.append((r, c))

            else:
                # middle empty space
                row.append(' ')
        wholeList.append(row)
    return wholeList

# Original
# Multiline definition
textBoard = \
 """\
======================
=--------------------=
=                    =
=                    =
=                    =
=                    =
======================\
"""

# Proof that newline is same as manual enter key
textBoard = \
 """======================\n=--------------------=\n=                    =\n=                    =\n=                    =\n=                    =\n======================"""


def array2D_to_string(list2d):
    """
    Converts a 2D list into a single string object
    """
    string2D = ""
    for r in range(len(list2d)):
        for c in range(len(list2d[r])):
            string2D += list2d[r][c]
        string2D += "\n"

    # Using the [:-1] since we don't want the last new line
    return string2D[:-1]
