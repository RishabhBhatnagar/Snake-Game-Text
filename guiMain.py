from tkinter import Tk, Label
import textRes
from tkinter.font import Font
import gameLogic

labelBoard = ''

def keyA(event, labelBoard):
    print("a pressed")
    
    print('\nsnakeList\n', gameLogic.snakeList, '\n')

    lent_before_newline = labelBoard['text'].index('\n') + 1
    # +1 since if width is x, counting the newline, it becomes x+1

    print("lent_before_newline=", lent_before_newline)
    # check image
    # since newline index will directly give the correct leng of row
    newString = labelBoard['text']

    def xy_to_str_replacing(x, y, newString, charToReplace):
        locationForNewCharacter = int(y*lent_before_newline + (x+1))
        print(locationForNewCharacter)
        '''
        # original
        newString = newString[:locationForNewCharacter] \
            + "#" + newString[locationForNewCharacter+1:]
        '''

        newString = newString[:locationForNewCharacter] \
            + charToReplace + newString[locationForNewCharacter+1:]
        

        return newString
        # pass


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
        # Replacing the correct location with snake character '#'


        # Replace # with a vairable like textRes.snakeBody
        newString = xy_to_str_replacing(x, y, newString, textRes.snakeBody)
        """
        # Original works try
        locationForNewCharacter = int(y*lent_before_newline + (x+1))
        print(locationForNewCharacter)
        newString = newString[:locationForNewCharacter] \
            + "#" + newString[locationForNewCharacter+1:]
        """


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

    # Shifting head up one space, by giving it new co or dinates
    gameLogic.snakeList[0] = (gameLogic.snakeList[0][0],
                              gameLogic.snakeList[0][1] - 1)

    # If snake has run into the border
    print("textRes.borderList", textRes.borderList)
    print("head is at ", gameLogic.snakeList[0])
    if gameLogic.snakeList[0] in textRes.borderList:
        print("ERROR\n"*6)


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
