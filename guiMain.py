from tkinter import Tk, Label
import textRes
from tkinter.font import Font
import gameLogic


def string_replace(newString, index, replacementChar):
    """
    Replace a single character in a string at the specified index
    :param newString: String in which the char is to be inserted
    :param index: The index in the string where character has to be inserted
    :param replacementChar: The char to be inserted
    :return:
    """
    newString = newString[:index] \
        + replacementChar + newString[index + 1:]
    return newString


def xy_to_str_index(x, y):
    """
    Convert the (x, y) grid coordinates to a string index
    :param x: x coordinate in grid
    :param y: y coordinate in grid
    :return: index in the string
    """
    return y * (textRes.width + 1) + x


def xy_to_str_replacing(x, y, newString, charToReplace):
    """
    Replace a char at (x, y) in the string newString
    :param x: x
    :param y: y
    :param newString: string where we need to replace the character
    :param charToReplace: char to be inserted in the string
    :return: the changed string
    """

    locationForNewCharacter = xy_to_str_index(x, y)
    newString = string_replace(newString,
                               locationForNewCharacter,
                               charToReplace)
    return newString


def addLocationToSnakeTail(newTailToBeAppended):
    """
    Append a new snakeBody to the existing snakeList
    :param newTailToBeAppended: (x,y) to be appended
    :return: None
    """
    gameLogic.snakeList.append(newTailToBeAppended)


def refresh_Grid(event, labelBoard, root):
    """
    Refresh the contents of the labelBoard since objects like:
    1) snake has changed position
    2) food has appeared
    3) food has disappeared
    :param event: event passed by a keypress function
    :param labelBoard: the Label object
    :return: None
    """

    # Getting the content of labelBoard in newString
    # newString will be modified accordingly, and then
    # assigned to labelBoard in the end
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
    # Food spawning in gui
    if gameLogic.ate:
        (gameLogic.foodX, gameLogic.foodY) = gameLogic.generateFood()
        newString = xy_to_str_replacing(gameLogic.foodX, gameLogic.foodY, newString, textRes.simpleFood)
        gameLogic.ate = False

    for x, y in gameLogic.snakeList:
        if (x, y) == gameLogic.snakeList[0]:
            # Insert head character at the head location
            newString = xy_to_str_replacing(x, y, newString, textRes.snakeHead)
        else:
            # Replace # with a variable like textRes.snakeBody
            newString = xy_to_str_replacing(x, y, newString, textRes.snakeBody)

    # Print head location
    print("head=", gameLogic.snakeList[0][1], gameLogic.snakeList[0][0])
    print("food =", gameLogic.foodX, gameLogic.foodY)

    # Check if snake swallowed the food :
    if gameLogic.foodY == gameLogic.snakeList[0][1] and gameLogic.foodX == gameLogic.snakeList[0][0]:
        gameLogic.ate = True

        # Food was eaten so we need to add a tail
        addLocationToSnakeTail(gameLogic.previousTailLocation)
        print("AAAAAAAAA: SNAKE INCREASED at", gameLogic.previousTailLocation)

        gameLogic.points = gameLogic.points + gameLogic.normalPoints
        gameLogic.foodCounter = gameLogic.foodCounter + 1
        print("Points:", gameLogic.points)

    print("Ate : ", gameLogic.foodCounter)
    if gameLogic.foodCounter % gameLogic.specialFoodFrequency == 0:
        if gameLogic.specialFoodGenerated == False:
            if gameLogic.foodCounter != gameLogic.lastAteCounter:
                gameLogic.splFoodX, gameLogic.splFoodY = gameLogic.generateFood()
                newString = xy_to_str_replacing(gameLogic.splFoodX, gameLogic.splFoodY, newString, textRes.specialFood)
                gameLogic.specialFoodGenerated = True
                gameLogic.lastAteCounter = gameLogic.foodCounter
                gameLogic.startTime = gameLogic.timer()

    if gameLogic.specialFoodGenerated == True:

        if gameLogic.timer() - gameLogic.startTime > gameLogic.splFoodMaxTime:
            newString = xy_to_str_replacing(gameLogic.splFoodX, gameLogic.splFoodY, newString, textRes.blank)
            gameLogic.splFoodX, gameLogic.splFoodY = -1, -1
            gameLogic.specialFoodGenerated = False

        # Check if snake ate the specialFood
        if gameLogic.splFoodX == gameLogic.snakeList[0][0]:
            if gameLogic.splFoodY == gameLogic.snakeList[0][1]:
                print("SpecialSwallowed.")

                # Food was eaten so we need to add a tail
                addLocationToSnakeTail(gameLogic.previousTailLocation)
                print("AAAAAAAAA: SNAKE INCREASED at", gameLogic.previousTailLocation)

                gameLogic.points = gameLogic.points + gameLogic.specialPoints
                print("Points :", gameLogic.points)
                gameLogic.specialFoodGenerated = False

    # If snake has run into the border
    # Using the [1][0]
    # instead of the more correct [0][1]
    # since in the list it is r,c ie y,x
    # but i have used x,y
    if gameLogic.snakeList[0][1] < 0 or gameLogic.snakeList[0][0] < 0 \
            or (gameLogic.snakeList[0][1], gameLogic.snakeList[0][0]) in textRes.borderList:
        # If the snakeList head has gone into the border,
        # or outside the bounds in negative direction
        # TODO call gameOver function
        root.destroy()
        raise ValueError("Indices shouldn't be inside the border")

    if gameLogic.boolFirstRun:
        # if boolFirstRun is true
        # then it means now the boolFirstRun is finished
        # so we can make it False
        print("first run over")
        gameLogic.boolFirstRun = False

    # Set the modified newString as the content of labelBoard
    labelBoard.config(text=newString)


def change_position(direction, root):
    """
    Shift the positions of the snakeList in the specified direction
    :param direction: Takes values 'up', 'left', 'right', 'down'
    :return: None
    """

    # If elif ladder checks if head will travel into an already occupied location by a snakeBody
    if direction == 'up':
        if (gameLogic.snakeList[0][0], gameLogic.snakeList[0][1] - 1) in gameLogic.snakeList:
            # TODO call gameOver function
            print("Collision")
            root.destroy()
            return
    elif direction == 'left':
        if (gameLogic.snakeList[0][0] - 1, gameLogic.snakeList[0][1]) in gameLogic.snakeList:
            # TODO call gameOver function
            print("Collision")
            root.destroy()
            return
    elif direction == 'down':
        if (gameLogic.snakeList[0][0], gameLogic.snakeList[0][1] + 1) in gameLogic.snakeList:
            # TODO call gameOver function
            print("Collision")
            root.destroy()
            return
    elif direction == 'right':
        if (gameLogic.snakeList[0][0] + 1, gameLogic.snakeList[0][1]) in gameLogic.snakeList:
            # TODO call gameOver function
            print("Collision")
            root.destroy()
            return

    gameLogic.tailPosition = gameLogic.snakeList[-1]

    for i in reversed(range(len(gameLogic.snakeList) - 1)):
        # Passing the location of n position to the n+1 position
        # This way all positions will effectively "move" ahead
        # and this will give the illusion that snake is moving
        gameLogic.snakeList[i + 1] = gameLogic.snakeList[i]

    # The location of the snake's tail before shifting is held by tailPosition
    # We assign it to previousTailLocation
    # We will use this variable to increase the length of the snake
    # in the addLocationToSnakeTail function
    gameLogic.previousTailLocation = gameLogic.tailPosition

    # In the previous for loop, position of head hasn't changed
    # Hence, depending on the key ie direction
    # we change the position of head
    if direction == 'up':
        # Shifting the head one place above it's current position
        gameLogic.snakeList[0] = (gameLogic.snakeList[0][0],
                                  gameLogic.snakeList[0][1] - 1)
    elif direction == 'left':
        # Shifting the head one place to the left
        gameLogic.snakeList[0] = (gameLogic.snakeList[0][0] - 1,
                                  gameLogic.snakeList[0][1])
    elif direction == 'down':
        # # Shifting the head one place below it's current position
        gameLogic.snakeList[0] = (gameLogic.snakeList[0][0],
                                  gameLogic.snakeList[0][1] + 1)
    elif direction == 'right':
        # Shifting the head one place to the right
        gameLogic.snakeList[0] = (gameLogic.snakeList[0][0] + 1,
                                  gameLogic.snakeList[0][1])


def move(event, obj, key):
    """
    Calls change_position and
    sets lastKeyPosition with the value of the last key that was pressed
    :param event: Event object
    :param obj: Refers to the Label object, ie labelBoard
    :param key: key which was pressed
    :return: None
    """

    # Updating the positions in the snakeList
    # in the specified direction
    change_position(key, root)

    # Updating lastKeyPosition
    gameLogic.lastKeyPosition = key

    # Refresh the text contents of labels, after snake has been moved
    refresh_Grid(event, obj, root)


def create_labelBoard(root):
    """
    Creates the label which contains the text elements for the board.
    :param root: Tk object, which should be the parent of the returned Label
    :return: Label object, with the correct text elements
    """

    # Creating the labelBoard
    labelBoard = Label(root, text="Hello World", anchor='nw')
    labelBoard.pack(fill='both')

    # Setting the font(monospace)
    # Monospace font is needed since all text elements need
    # to be of the same size so that the board looks proper
    # Defining a custom font

    my_font = Font(family='Consolas', size=15)
    # Consolas is available on Windows
    # Linux, Mac users may need to change this parameter

    labelBoard.config(font=my_font)

    # Initializing the empty grid
    labelBoard.config(text=textRes.array2D_to_string(textRes.init_list2D()))

    # Set background color
    labelBoard.config(bg=textRes.bgColor)
    # Set the text color
    labelBoard.config(foreground=textRes.fgColor)

    # Border settings
    labelBoard.config(highlightthickness=6)
    labelBoard.config(relief='solid')

    # Setting location in grid
    labelBoard.grid(row=0, column=0)

    # Binding keyboard to their move commands
    root.bind('a', lambda event, obj=labelBoard: move(event, obj, 'left'))
    root.bind('w', lambda event, obj=labelBoard: move(event, obj, 'up'))
    root.bind('s', lambda event, obj=labelBoard: move(event, obj, 'down'))
    root.bind('d', lambda event, obj=labelBoard: move(event, obj, 'right'))

    return labelBoard


def autoMoving(root, labelBo):
    """
    Function which recurses to keep the snake moving,
    based on the last key pressed by the user
    :param root:
    :param labelBo:
    :return: None
    """
    _ = ''
    print("autorun")
    # lastKeyPosition refers to the last key pressed by the user
    change_position(gameLogic.lastKeyPosition, root)

    # _ is passed as an argument since refresh_Grid takes a event object
    # as the first argument. Since the event object is not used in the
    # function, we can pass a placeholder variable
    refresh_Grid(_, labelBo, root)

    # root.after has to be recursively called,
    # it should be the last statement to be called.
    root.after(gameLogic.autoTime, lambda: autoMoving(root, labelBo))


def create_root(root):
    """
    Create and configure the root
    :param root: Tk object
    :return: Tk object
    """

    labelBo = create_labelBoard(root)

    root.after(gameLogic.autoTime, lambda: autoMoving(root, labelBo))

    # Runs the window
    root.mainloop()


if __name__ == '__main__':

    # Trial call
    textRes.setTheme(2)

    root = Tk()
    create_root(root)
