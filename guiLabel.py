from tkinter import Tk, Label
from textBG import textBoard
from tkinter.font import Font

root = Tk()

# Setting size
root.geometry("400x400+100+100")

my_text = Label(root, text="Hello World", anchor='nw')#justify="left")
my_text.pack(fill='both')


#Custom font
my_font = Font(family='Consolas',size=15)

my_text.config(text='New Words')

# Setting the font(monospace)
my_text.config(font=my_font)

# Setting the text bg
my_text.config(text=textBoard)

my_text.config(bg='red')
my_text.config(highlightthickness=6)
my_text.config(relief='solid')


# Setting location in grid
my_text.grid(row=0, column=0)

root.mainloop()
