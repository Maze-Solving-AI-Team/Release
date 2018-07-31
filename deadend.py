# Import modules
import sys, pygame, time, math
from time import sleep
from pygame.locals import *
from PIL import Image
import timing
from init import *

# Initialize
img = Image.open(maze)
change = 3
blockSize = 5 * change
width = img.width * change
height = img.height * change
screen = pygame.display.set_mode((width,height))
background = pygame.image.load(maze).convert()
newscreen = pygame.transform.scale(background, (width, height))

#Colors
color = (0, 188, 0)
white = (255, 255, 255, 255)
black = (0, 0, 0, 255)
blue = (0, 0, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0, 255)

# Recognizing black/white
size = [img.size]
colors = img.getcolors()
pix = img.load()
list = []

# Locate the starting coordinate
for x in range(0,180):
    if pix[x,179] == (255, 255, 255, 255):
        list.append(x)

xvalueOfStart = list[0] * change
#print(xvalueOfStart)

blockSize = len(list) * change

yvalueOfStart = height - blockSize

list = []

# Locate the ending coordinate
for x in range(0,180):
    if pix[x,0] == (255, 255, 255, 255):
        list.append(x)

xvalueOfEnd = list[0] * change
#print(xvalueOfEnd)

pygame.draw.rect(newscreen, color, pygame.Rect(xvalueOfStart, yvalueOfStart, blockSize, blockSize))
screen.blit(newscreen, (0,0))
pygame.display.update()
time.sleep(0.1)

# Function to move forward
def moveUp(x, y, blocksize, newcolor, sleep):
    global direction
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blocksize, blocksize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x, y - blocksize, blocksize, blocksize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentY
    global currentX
    currentY = y - blocksize
    currentX = x
    direction = 1
    time.sleep(sleep)

# Function to move left
def moveDown(x, y, blocksize, newcolor, sleep):
    global direction
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blocksize, blocksize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x, y + blocksize, blocksize, blocksize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentY
    global currentX    
    currentY = y + blocksize
    currentX = x
    direction = 4
    time.sleep(sleep)
    
# Function to move left  
def moveLeft(x, y, blocksize, newcolor, sleep):
    global direction
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blocksize, blocksize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x - blocksize, y, blocksize, blocksize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentX
    global currentY        
    currentX = x - blocksize
    currentY = y
    direction = 3
    time.sleep(sleep)

# Function to move right
def moveRight(x, y, blocksize, newcolor, sleep):
    global direction
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blocksize, blocksize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x + blocksize, y, blocksize, blocksize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentX
    global currentY        
    currentX = x + blocksize
    currentY = y
    direction = 2
    time.sleep(sleep)

#Initialization of currentX and currentY
def varsInit(x, y):
    global currentX
    global currentY
    global direction
    currentX = x
    currentY = y
    direction = 1

#Function to determine direction to move if facing up
def up(replace):
    if newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace, sleep)
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace, sleep)
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace, sleep)
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace, sleep)
    
#Function to determine direction to move if facing right
def right(replace):
    if newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace, sleep)
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace, sleep)
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace, sleep)
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace, sleep)
    
#Function to determine direction to move if facing left
def left(replace):
    if newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace, sleep)
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace, sleep)
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace, sleep)
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace, sleep)

#Function to determine direction to move if facing down
def down(replace):
    if newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace, sleep)
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace, sleep)
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace, sleep)
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace, sleep)

varsInit(xvalueOfStart, yvalueOfStart)

direction = 1
currentX = blockSize
currentY = blockSize
whiteListX = []
whiteListY = []
deadEnds = 1

#-------------DEAD END FILLER------------
while deadEnds != 0:
    #Define variables
    deadEnds = 0
    intersection = 0
    #Check the color of each and add location to list if white
    while currentY <= (height - blockSize):
        getCur = newscreen.get_at((currentX, currentY))
        if getCur == white:
            whiteListX.append(currentX)
            whiteListY.append(currentY)
        currentX = currentX + blockSize
        if currentX >= (width - blockSize + 1):
            currentX = 0
            currentY = currentY + blockSize
    whiteListLength = len(whiteListX)
    #Determine if each white space is a deadend
    for x in range (0, whiteListLength):
        count = 0
        if newscreen.get_at((whiteListX[x], whiteListY[x])) != white or newscreen.get_at((whiteListX[x] - blockSize, whiteListY[x])) == black or newscreen.get_at((whiteListX[x] - blockSize, whiteListY[x])) == blue:
            count = count + 1
        if newscreen.get_at((whiteListX[x], whiteListY[x])) != white or newscreen.get_at((whiteListX[x] + blockSize, whiteListY[x])) == black or newscreen.get_at((whiteListX[x] + blockSize, whiteListY[x])) == blue:
            count = count + 1
        if newscreen.get_at((whiteListX[x], whiteListY[x])) != white or newscreen.get_at((whiteListX[x], whiteListY[x] - blockSize)) == black or newscreen.get_at((whiteListX[x], whiteListY[x] - blockSize)) == blue:
            count = count + 1
        if newscreen.get_at((whiteListX[x], whiteListY[x])) != white or newscreen.get_at((whiteListX[x], whiteListY[x] + blockSize)) == black or newscreen.get_at((whiteListX[x], whiteListY[x] + blockSize)) == blue:
            count = count + 1
        if count == 3:
            deadEnds = deadEnds + 1
            pygame.draw.rect(newscreen, blue, pygame.Rect(whiteListX[x], whiteListY[x], blockSize, blockSize))
        if count < 3:
            intersection == 1
    #Break the while loop once all dead ends are filled
    if deadEnds == intersection:
        break

    screen.blit(newscreen, (0,0))
    pygame.display.update()

varsInit(xvalueOfStart, yvalueOfStart)

moveUp(currentX, currentY, blockSize, white, sleep)

#Right turn movement through the solution
while 0 != currentY:
    if direction == 1:#up
        up(white)
    elif direction == 2:
        right(white)
    elif direction == 3:
        left(white)
    elif direction == 4:
        down(white)