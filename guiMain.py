from tkinter import Tk, Label
import textRes
from tkinter.font import Font
import gameLogic

autoTime = 1000

def string_replace(newString, index, replacementChar):
    newString = newString[:index] \
        + replacementChar + newString[index+1:]
    return newString


def xy_to_str_index(x, y): return y*(textRes.width + 1) + (x)


def xy_to_str_replacing(x, y, newString, charToReplace):
    """
    Pass x,y and the character to place in the position,
    and this function will do it.
    """
    locationForNewCharacter = xy_to_str_index(x, y)
    newString = string_replace(newString,
                               locationForNewCharacter,
                               charToReplace)

    return newString


def refresh_Grid(event, labelBoard):
    # Setting newString the content of labelBoard
    newString = labelBoard['text']

    if not gameLogic.boolFirstRun:
        # If this is not the first run
        # Then at tailPosition put blank
        # tailPosition contains location of tail, as per
        # last function call
        newString = xy_to_str_replacing(gameLogic.tailPosition[0],
                                        gameLogic.tailPosition[1],
                                        newString,
                                        textRes.blank)

    for x, y in gameLogic.snakeList:
        if (x, y) == gameLogic.snakeList[0]:
            newString = xy_to_str_replacing(x, y, newString, textRes.snakeHead)
        else:
            # Replace # with a vairable like textRes.snakeBody
            newString = xy_to_str_replacing(x, y, newString, textRes.snakeBody)

    '''
    if gameLogic.boolMoved:
        # Storing the tail position so as to replace # with blank,
        # in the next function call
        gameLogic.tailPosition = gameLogic.snakeList[-1]
        
        for i in reversed(range(len(gameLogic.snakeList) - 1)):
            # Passing the location of first position to the next position
            gameLogic.snakeList[i+1] = gameLogic.snakeList[i]
    '''

    # Print head location
    print("head=", gameLogic.snakeList[0][1], gameLogic.snakeList[0][0])

    if gameLogic.snakeList[0][1] < 0 or gameLogic.snakeList[0][0] < 0 \
    or (gameLogic.snakeList[0][1], gameLogic.snakeList[0][0]) in textRes.borderList:
        raise ValueError("Indices shouldn't be inside the border")

    # If snake has run into the border
    # Using the [1][0]
    # instead of the more correct [0][1]
    # since in the list it is r,c ie y,x
    # but i have used x,y
    if (gameLogic.snakeList[0][1], gameLogic.snakeList[0][0])\
       in textRes.borderList:
        print("ERROR\n"*12)


    if gameLogic.boolFirstRun:
        # if boolFirstRun is true
        # then it means now the boolFirstRun is finished
        # so we can make it False
        print("first run over")
        gameLogic.boolFirstRun = False



    # Set text of label
    labelBoard.config(text=newString)

'''
def change_position_up():
    gameLogic.tailPosition = gameLogic.snakeList[-1]
        
    for i in reversed(range(len(gameLogic.snakeList) - 1)):
        # Passing the location of first position to the next position
        gameLogic.snakeList[i+1] = gameLogic.snakeList[i]

    # Shifting head up one space, by giving it new co or dinates
    gameLogic.snakeList[0] = (gameLogic.snakeList[0][0],
                              gameLogic.snakeList[0][1] - 1)
'''

def change_position(direction):

    if direction == 'up':
        if (gameLogic.snakeList[0][0], gameLogic.snakeList[0][1] - 1) in gameLogic.snakeList:
            print("Collision")
            return
    elif direction == 'left':
        if (gameLogic.snakeList[0][0] - 1, gameLogic.snakeList[0][1]) in gameLogic.snakeList:
            print("Collision")
            return
    elif direction == 'down':
        if (gameLogic.snakeList[0][0], gameLogic.snakeList[0][1] + 1) in gameLogic.snakeList:
            print("Collision")
            return
    elif direction == 'right':
        if (gameLogic.snakeList[0][0] + 1, gameLogic.snakeList[0][1]) in gameLogic.snakeList:
            print("Collision")
            return

    gameLogic.tailPosition = gameLogic.snakeList[-1]
        
    for i in reversed(range(len(gameLogic.snakeList) - 1)):
        # Passing the location of first position to the next position
        gameLogic.snakeList[i+1] = gameLogic.snakeList[i]

    if direction == 'up':
        # Shifting head up one space, by giving it new co or dinates
        gameLogic.snakeList[0] = (gameLogic.snakeList[0][0],
                                  gameLogic.snakeList[0][1] - 1)
    elif direction == 'left':
        gameLogic.snakeList[0] = (gameLogic.snakeList[0][0] - 1,
                                  gameLogic.snakeList[0][1])
    elif direction == 'down':
        gameLogic.snakeList[0] = (gameLogic.snakeList[0][0],
                                  gameLogic.snakeList[0][1] + 1)
    elif direction == 'right':
        gameLogic.snakeList[0] = (gameLogic.snakeList[0][0] + 1,
                                  gameLogic.snakeList[0][1])

def move(event, obj, key):
    #refresh_Grid(event, obj)
    
    '''
    if event.char is 'w':
        # change_position_up()
        change_position('up')
    elif event.char is 'a':
        change_position('left')
    elif event.char is 's':
        change_position('down')
    elif event.char is 'd':
        change_position('right')
    '''

    change_position(key)

    # Updating lastKeyPosition
    gameLogic.lastKeyPosition = key

    refresh_Grid(event, obj)
        

def create_labelBoard(root):

    # Creating the labelBoard
    labelBoard = Label(root, text="Hello World", anchor='nw')
    labelBoard.pack(fill='both')

    # Setting the font(monospace)
    # Custom font
    my_font = Font(family='Consolas', size=15)
    labelBoard.config(font=my_font)

    # Setting the text
    # Works
    # labelBoard.config(text=textRes.textBoard)

    # Alternate
    labelBoard.config(text=textRes.array2D_to_string(textRes.init_list2D()))


    # Set background color as red
    labelBoard.config(bg='red')
    labelBoard.config(highlightthickness=6)
    labelBoard.config(relief='solid')

    # Setting location in grid
    labelBoard.grid(row=0, column=0)

    # Trying updating snake on grid
    # root.bind('a', lambda event, obj=labelBoard: refresh_Grid(event, obj))
    root.bind('a', lambda event, obj=labelBoard: move(event, obj, 'left'))
    root.bind('w', lambda event, obj=labelBoard: move(event, obj, 'up'))
    root.bind('s', lambda event, obj=labelBoard: move(event, obj, 'down'))
    root.bind('d', lambda event, obj=labelBoard: move(event, obj, 'right'))

    return labelBoard


def autoMoving(root, labelBo):
    '''
    Function which will keep the snake moving
    '''
    _ = ''
    print("autorun")
    change_position(gameLogic.lastKeyPosition)
    refresh_Grid(_, labelBo)
    root.after(autoTime, lambda: autoMoving(root, labelBo))


    # directly call change position


def create_root(root):
    # root = Tk()

    # Setting size
    # root.geometry("400x400+100+100")

    labelBo = create_labelBoard(root)

    global autoTime
    autoTime = 1000
    root.after(autoTime, lambda: autoMoving(root, labelBo))

    # Runs the window
    root.mainloop()


if __name__ == '__main__':

    root = Tk()
    create_root(root)
