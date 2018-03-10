from tkinter import Tk, Label, PhotoImage, Button, Entry, Frame, StringVar, OptionMenu, ttk
import textRes

from tkinter.font import Font
import gameLogic
from random import randint


lb = None     #Labelboard for theme changing.

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
    global lb
    lb = labelBoard
    if textRes.isthemechange:
        labelBoard.config(text=textRes.array2D_to_string(textRes.init_list2D()))
        # Set background color as red
        labelBoard.config(bg=textRes.bgColor)
        textRes.isthemechange=False

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


    #food spawning in gui        
        
    if  gameLogic.ate == True:
        (gameLogic.foodX, gameLogic.foodY) =gameLogic.generateFood()     
        newString = xy_to_str_replacing(gameLogic.foodX, gameLogic.foodY, newString, "*")
        gameLogic.ate = False

        
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
    print("food =", gameLogic.foodX, gameLogic.foodY)




    #Check if snake swallowed the food :
    if gameLogic.foodY == gameLogic.snakeList[0][1] and gameLogic.foodX == gameLogic.snakeList[0][0]:
        gameLogic.ate = True
        gameLogic.points = gameLogic.points + gameLogic.normalPoints
        gameLogic.foodCounter = gameLogic.foodCounter + 1
        print("Points:", gameLogic.points)

    print("Ate : ", gameLogic.foodCounter)
    if gameLogic.foodCounter % gameLogic.specialFoodFrequency == 0:
        if gameLogic.specialFoodGenerated == False:
            if gameLogic.foodCounter != gameLogic.lastAteCounter:
                gameLogic.splFoodX, gameLogic.splFoodY = gameLogic.generateFood()
                newString = xy_to_str_replacing(gameLogic.splFoodX, gameLogic.splFoodY, newString, "%")
                gameLogic.specialFoodGenerated = True
                gameLogic.lastAteCounter = gameLogic.foodCounter
                gameLogic.startTime = gameLogic.timer()

    
    if gameLogic.specialFoodGenerated == True :

        if gameLogic.timer()-gameLogic.startTime > gameLogic.splFoodMaxTime:
            newString = xy_to_str_replacing(gameLogic.splFoodX, gameLogic.splFoodY, newString, " ")
            gameLogic.splFoodX, gameLogic.splFoodY = -1, -1
            gameLogic.specialFoodGenerated = False
        "Check if snake ate the specialFood"
        if gameLogic.splFoodX == gameLogic.snakeList[0][0]:
            if gameLogic.splFoodY == gameLogic.snakeList[0][1]:
                print("SpecialSwallowed.")
                gameLogic.points = gameLogic.points + gameLogic.specialPoints
                print("Points :", gameLogic.points)
                gameLogic.specialFoodGenerated = False






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
        # so we can make it Falsemm
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
   # labelBoard.size()

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
    root.after(gameLogic.autoTime, lambda: autoMoving(root, labelBo))


    # directly call change position




def set_up_name():

    sc=Tk()
    sc.geometry("150x100+500+300")
    l1=Label(sc, text="Enter your Name:")
    l1.grid(row=0, column= 1)

    s = StringVar()

    e1 = ttk.Entry(sc, textvariable=s)
    e1.grid(row=1, column=1)
    #e1.bind("<OK_butt>", store_ip)

    name_label = ttk.Label(sc, text="NAME SHOULD COME HERE")
    name_label.grid(row=3, column=1)

    OK_butt = ttk.Button(sc, text="OK!", width=6, command=store_ip(e1=e1,name_label=name_label))
    OK_butt.grid(row=2, column=1)




def store_ip(e1,name_label):
    ip_name=e1.get()
    print(ip_name*5)
    name_label.config(text=ip_name)
    name_label.grid(row=3, column=1)






def new_game():
    pass

def pause_game():
    pass

def reset_game():
    pass


def gm_change_theme(args):
    textRes.isthemechange=True
    textRes.theme_change(args)
    gameLogic.ate = True
    newString = lb['text']
    (gameLogic.foodX, gameLogic.foodY) =gameLogic.generateFood()
    newString = xy_to_str_replacing(gameLogic.foodX, gameLogic.foodY, newString, "*")
        
    

def create_root(root):
    #root = Tk()

    # Setting size
    root.geometry("700x400+250+200")


    labelBo = create_labelBoard(root)

    use_x=12
    use_y=2

    frame = Frame()
    frame.grid(row=0, column=1)
    frame.config()


   # THIS IS JUST USE TO ALLIGN  (0,0)
    l1 = Label(frame,text='0,0', width=use_x )
    l1.grid(row=0, column=0, sticky='ns')


    b1 = Button(frame, text='NAME', bg='gray', width=use_x, height=use_y, command=set_up_name)# pady=8, padx=8
    b1.grid_rowconfigure(0, weight=1)
    b1.grid(row=0, column=1, sticky='ns')
    # b1.grid(columnspan=2)

    #THIS IS JUST USE TO ALLIGN (1,1)
    l1=Label(frame,text='1,1', width=use_x)
    l1.grid(row=1, column=1, sticky='ns')


    b2 = Button(frame, text='NEW GAME', bg='purple', width=use_x, height=use_y, command=new_game)# pady=8, padx=8
    b2.grid_rowconfigure(0, weight=1)
    b2.grid(row=2, column=1, sticky='ns')

   # THIS IS JUST USE TO ALLIGN(3,1)
    l1 = Label(frame, text='3,1', width=use_x)
    l1.grid(row=3, column=1, sticky='ns')



    b3 = Button(frame, text='PAUSE', bg='green', width=use_x, height=use_y, command=pause_game) # pady=8, padx=8
    b3.grid_rowconfigure(0, weight=1)
    b3.grid(row=4, column=1, sticky='ns')

   # THIS IS JUST USE TO ALLIGN(5,1)
    l1 = Label(frame, text='5,1', width=use_x)
    l1.grid(row=5, column=1, sticky='ns')


    b4 = Button(frame, text='RESET', bg='red', width=use_x, height=use_y, command=reset_game)  # pady=8, padx=8
    b4.grid_rowconfigure(0, weight=1)
    b4.grid(row=6, column=1, sticky='ns')

    # THIS IS JUST USE TO ALLIGN(7,1)
    l1 = Label(frame, text='7,1', width=use_x)
    l1.grid(row=7, column=1, sticky='ns')


    options = ['THEME :1', 'THEME :2', 'THEME :3','THEME :4']
    var = StringVar()
    var.set(options[0]) #intial theme settings

    drop = OptionMenu(frame , var, *options,  command=lambda x: gm_change_theme(x))
    drop.config(bg='yellow', width=use_x-3, height=use_y )

    #var.trace('w', textRes.theme_change)
    drop.grid(row=8 ,column=1)


    root.after(gameLogic.autoTime, lambda : autoMoving(root, labelBo))

    # Runs the window
    root.mainloop()


if __name__ == '__main__':

    root = Tk()


    create_root(root)




