from tkinter import Tk, Label
from textBG import textBoard
from tkinter.font import Font

root = Tk()

# Setting size
root.geometry("400x400+100+100")

labelBoard = Label(root, text="Hello World", anchor='nw')#justify="left")
labelBoard.pack(fill='both')


#Custom font
my_font = Font(family='Consolas',size=15)

labelBoard.config(text='New Words')

# Setting the font(monospace)
labelBoard.config(font=my_font)

# Setting the text bg
labelBoard.config(text=textBoard)

labelBoard.config(bg='red')
labelBoard.config(highlightthickness=6)
labelBoard.config(relief='solid')


# Setting location in grid
labelBoard.grid(row=0, column=0)

root.mainloop()
