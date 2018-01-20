from tkinter import Tk, Label
import textRes
from tkinter.font import Font
import gameLogic

labelBoard = ''

def string_replace(newString, index, replacementChar):
    newString = newString[:index] \
        + replacementChar + newString[index+1:]
    return newString

def keyA(event, labelBoard):
    print("a pressed")
    
    print('\nsnakeList\n', gameLogic.snakeList, '\n')

    lent_before_newline = labelBoard['text'].index('\n') + 1
    # +1 since if width is x, counting the newline, it becomes x+1

    print("lent_before_newline=", lent_before_newline)
    # check image
    # since newline index will directly give the correct leng of row
    newString = labelBoard['text']

    def xy_to_str_index(x, y): return y*lent_before_newline + (x)

    x1, y1 = 0, 0
    x1y1Loc = xy_to_str_index(x1, y1)
    print("x1,y1", (x1, y1), "strI", )
    print("type(x1y1Loc)", type(x1y1Loc))
    newString = newString[:x1y1Loc] \
        + "$" + newString[x1y1Loc+1:]
    
    x2, y2 = 0, 1
    x2y2Loc = xy_to_str_index(x2, y2)
    print("x2,y2", (x2, y2), "strI", )
    newString = newString[:x2y2Loc] \
        + "$" + newString[x2y2Loc+1:]

    def xy_to_str_replacing(x, y, newString, charToReplace):
        """
        Pass x,y and the character to place in the position,
        and this function will do it.
        """
        locationForNewCharacter = xy_to_str_index(x, y)
        print(locationForNewCharacter)
        newString = string_replace(newString,
                                   locationForNewCharacter,
                                   charToReplace)

        return newString


    if not gameLogic.boolFirstRun:
        # If this is not the first run
        # Then at tailPosition put blank
        # tailPosition contains location of tail, as per
        # last function call
        print('tailreplace')
        newString = xy_to_str_replacing(gameLogic.tailPosition[0],
                                        gameLogic.tailPosition[1],
                                        newString,
                                        textRes.blank)

    for x, y in gameLogic.snakeList:
        # Replace # with a vairable like textRes.snakeBody
        newString = xy_to_str_replacing(x, y, newString, textRes.snakeBody)



    # Storing the tail position so as to replace # with blank,
    # in the next function call
    print("original:tail", gameLogic.tailPosition)
    gameLogic.tailPosition = gameLogic.snakeList[-1]
    print("new:     tail", gameLogic.tailPosition)

    print("Original:", gameLogic.snakeList)
    # Making the snake go up, as standard game start position
    for i in reversed(range(len(gameLogic.snakeList) - 1)):
        # Passing the location of first position to the next position
        # Last position will be lost
        print("i=", i)
        print("snakeList[i+1]", gameLogic.snakeList[i+1])
        print("snakeList[i]", gameLogic.snakeList[i])
        gameLogic.snakeList[i+1] = gameLogic.snakeList[i]


    # If snake has run into the border
    print("textRes.borderList", textRes.borderList)
    print("head is at ", (gameLogic.snakeList[0][1], gameLogic.snakeList[0][0]))

    # Using the [1][0]
    # instead of the more correct [0][1]
    # since in the list it is r,c ie y,x
    # but i have used x,y
    if (gameLogic.snakeList[0][1], gameLogic.snakeList[0][0])\
       in textRes.borderList:
        print("ERROR\n"*12)

    # Shifting head up one space, by giving it new co or dinates
    gameLogic.snakeList[0] = (gameLogic.snakeList[0][0],
                              gameLogic.snakeList[0][1] - 1)



    print("New:", gameLogic.snakeList)

    if gameLogic.boolFirstRun:
        # if boolFirstRun is true
        # then it means now the boolFirstRun is finished
        # so we can make it False
        print("first run over")
        gameLogic.boolFirstRun = False



    # Set text of label
    labelBoard.config(text=newString)

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
    root.bind('a', lambda event, obj=labelBoard: keyA(event, obj))


    return labelBoard


def create_root(root):
    # root = Tk()

    # Setting size
    # root.geometry("400x400+100+100")

    create_labelBoard(root)

    # Runs the window
    root.mainloop()


if __name__ == '__main__':

    root = Tk()
    create_root(root)
