import textRes
from random import randint

autoTime = 1000

points = 0

foodCounter = 0
specialFoodFrequency = 3
specialFoodGenerated = False
lastAteCounter = 0
ate = True

normalPoints = 10
specialPoints = 50
snakeList = []

w, h = textRes.width, textRes.height
start_location = (int(w/2), int(h/2))

# Snake head is at start_location
snakeList.append(start_location)

# Here, [0] is x, [1] is y
# But, rows are y, cols are x, but that means
# those are the ones which are wrong ordered.
# Snake body of head + 2
snakeList.append((start_location[0], start_location[1] + 1))
snakeList.append((start_location[0], start_location[1] + 2))
snakeList.append((start_location[0], start_location[1] + 3))
snakeList.append((start_location[0], start_location[1] + 4))

tailPosition = snakeList[-1]

boolFirstRun = True

autoRun = True
lastKeyPosition = 'up'

#Generating food location :
def foodLocation(w, h):
    def food():
        x = randint(2, w-2)
        y = randint(2, h-2)
        return (x, y)
    return food
generateFood = foodLocation(w, h)
(foodX, foodY) = (0,0)

splFoodX, splFoodY = 0, 0
