# Import modules
import sys, pygame, time, math, PIL
from time import sleep
from pygame.locals import *
from PIL import *
from PIL import Image
import timing
from init import *

# Initialize
img = Image.open(maze)
change = 3
width = img.width * change
height = img.height * change
background = [img]
screen = pygame.display.set_mode((width,height))
background = pygame.image.load(maze).convert()
newscreen = pygame.transform.scale(background, (width, height))

#Colors
color = (0, 188, 0)
white = (255, 255, 255)
black = (255, 255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 188, 0)

pix = img.load()
list = []

# Locate the starting coordinate
for x in range(0,180):
    if pix[x,179] == (255, 255, 255, 255):
        list.append(x)

xvalueOfStart = list[0] * change
blockSize = len(list) * change
yvalueOfStart = height - blockSize

list = []

# Locate the ending coordinate
for x in range(0,180):
    if pix[x,0] == (255, 255, 255, 255):
        list.append(x)

xvalueOfEnd = list[0] * change

pygame.draw.rect(newscreen, color, pygame.Rect(xvalueOfStart, yvalueOfStart, blockSize, blockSize))
screen.blit(newscreen, (0, 0))
pygame.display.update()
time.sleep(0.1)

# Function to move forward
# Function to move forward
def moveUp(x, y, blocksize, newcolor, sleep):
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blocksize, blocksize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x, y - blocksize, blocksize, blocksize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentY
    global currentX
    currentY = y - blocksize
    currentX = x
    time.sleep(sleep)

# Function to move left
def moveDown(x, y, blocksize, newcolor, sleep):
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blocksize, blocksize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x, y + blocksize, blocksize, blocksize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentY
    global currentX    
    currentY = y + blocksize
    currentX = x
    time.sleep(sleep)
    
# Function to move left  
def moveLeft(x, y, blocksize, newcolor, sleep):
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blocksize, blocksize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x - blocksize, y, blocksize, blocksize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentX
    global currentY        
    currentX = x - blocksize
    currentY = y
    time.sleep(sleep)

# Function to move right
def moveRight(x, y, blocksize, newcolor, sleep):
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blocksize, blocksize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x + blocksize, y, blocksize, blocksize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentX
    global currentY        
    currentX = x + blocksize
    currentY = y
    time.sleep(sleep)

moveUp(xvalueOfStart, yvalueOfStart, blockSize, white, sleep)

while 0 != currentY:
    if newscreen.get_at((currentX,currentY - blockSize)) == (255, 255, 255, 255):#up        
        moveUp(currentX, currentY, blockSize, blue, sleep)
    elif newscreen.get_at((currentX + blockSize,currentY)) == (255, 255, 255, 255):#right
        moveRight(currentX, currentY, blockSize, blue, sleep)
    elif newscreen.get_at((currentX - blockSize,currentY)) == (255, 255, 255, 255):#left
        moveLeft(currentX, currentY, blockSize, blue, sleep)
    elif newscreen.get_at((currentX,currentY + blockSize)) == (255, 255, 255, 255):#down
        moveDown(currentX, currentY, blockSize, blue, sleep)
    else:
        if newscreen.get_at((currentX,currentY + blockSize)) == (0, 0, 255, 255):#down
            moveDown(currentX, currentY, blockSize, (0, 255, 255), sleep)
        elif newscreen.get_at((currentX + blockSize,currentY)) == (0, 0, 255, 255):#right
            moveRight(currentX, currentY, blockSize, (0, 255, 255), sleep)
        else:
            if newscreen.get_at((currentX - blockSize,currentY)) == (0, 0, 255, 255):#left
                moveLeft(currentX, currentY, blockSize, (0, 255, 255), sleep)
            elif newscreen.get_at((currentX,currentY - blockSize)) == (0, 0, 255, 255):#up        
                moveUp(currentX, currentY, blockSize, (0, 255, 255), sleep)