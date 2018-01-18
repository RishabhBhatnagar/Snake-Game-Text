from tkinter import Tk, Label, Frame
from textRes import textBoard
from tkinter.font import Font

root = Tk()

def key(event):
    print("pressed", event.char)
    print("PRESSED")

# Setting size
root.geometry("400x400+100+100")

frameWorld = Frame(root)
frameWorld.pack(fill='both')
frameWorld.config(bg='blue')
frameWorld.grid(row=0,column=0)
frameWorld.config(relief='sunken')
#frameWorld.config(expand=1)

# Need to set focus before binding
frameWorld.focus_set()
frameWorld.bind('<Key>', key)

labelBoard = Label(frameWorld, text="Hello World", anchor='nw')#justify="left")
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
