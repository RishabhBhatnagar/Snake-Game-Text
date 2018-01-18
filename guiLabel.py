from tkinter import Tk, Label
root = Tk()

# Setting size
root.geometry("400x400+100+100")

my_text = Label(root, text="Hello World", anchor='nw')#justify="left")
my_text.pack(fill='both')

root.mainloop()