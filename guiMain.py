from tkinter import Tk, Label
from textRes import textBoard
from tkinter.font import Font


def create_labelBoard(root):

    # Creating the labelBoard
    labelBoard = Label(root, text="Hello World", anchor='nw')
    labelBoard.pack(fill='both')

    # Setting the font(monospace)
    # Custom font
    my_font = Font(family='Consolas', size=15)
    labelBoard.config(font=my_font)

    # Setting the text
    labelBoard.config(text=textBoard)

    # Set background color as red
    labelBoard.config(bg='red')
    labelBoard.config(highlightthickness=6)
    labelBoard.config(relief='solid')

    # Setting location in grid
    labelBoard.grid(row=0, column=0)


def create_root():
    root = Tk()

    # Setting size
    root.geometry("400x400+100+100")

    create_labelBoard(root)

    # Runs the window
    root.mainloop()


if __name__ == '__main__':

    create_root()
