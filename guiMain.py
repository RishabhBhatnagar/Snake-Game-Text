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

    for x, y in gameLogic.snakeList:
        # labelBoard['text'][y*lent_before_newline + (x+1)] = "#"
        locationForNewCharacter = int(y*lent_before_newline + (x+1))
        print(locationForNewCharacter)
        newString = newString[:locationForNewCharacter] \
            + "#" + newString[locationForNewCharacter+1:]

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
