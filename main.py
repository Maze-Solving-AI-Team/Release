'''
solution-line 1762

priorities-line 262
rightTurn-line 528
deadEnd-line 702
intersection-line 963
'''

# Import modules
import sys, pygame, time, math
from time import sleep
from PIL import Image
from datetime import datetime
# from algs import Algorithms1

'''
deadEnd=Algs()
intersection=Algs()
priorities=Algs()
http://python4java.necaiseweb.org/OOP/DefiningClasses
'''

#Colors
color = (0, 188, 0)
white = (255, 255, 255)
black = (0, 0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0, 100)
green = (0, 188, 0)

pygame.mixer.init()
pygame.mixer.music.load('MSAI.ogg')
pygame.mixer.music.play(loops=-1)

#================================GUI===================================
# Display background image
pygame.font.init()
image = 'start.png'
change = 1
img = Image.open(image)
width = img.width * change
height = img.height * change
screen = pygame.display.set_mode((width,height))
background = pygame.image.load(image).convert()
newscreen = pygame.transform.scale(background, (width, height))
screen.blit(newscreen, (0,0))
pygame.display.update()

# Start page
running = True
while running:
    event = pygame.event.wait()
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            x,y = pygame.mouse.get_pos()
            if 162 <= x <= 482 and 483 <= y <= 574:
                running = False
    elif event.type == pygame.QUIT:
        pygame.display.quit()
        pygame.quit()
        sys.exit()

#Settings Page
background = pygame.image.load('settings.png').convert()
newscreen = pygame.transform.scale(background, (width, height))
screen.blit(newscreen, (0,0))
pygame.display.update()

def makeTransRect(x,y,locX,locY):
    s = pygame.Surface((x,y))
    s.set_alpha(120)
    s.fill((18,158,46))
    newscreen.blit(s,(locX,locY))

mazeX = 29
mazeY = 113
speedX = 234
speedY = 435
makeTransRect(95,95,mazeX,mazeY)
makeTransRect(181,43,speedX,speedY)
sleep = 0.01
maze = 'maze.png'
running = True

while running:
    event = pygame.event.wait()
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            x,y = pygame.mouse.get_pos()
            if 190 <= x <= 470 and 514 <= y <= 628: #Next
                running = False
            if 28 <= x <= 210 and 435 <= y <= 478: #Slow
                sleep = 0.05
                speedX = 28
                speedY = 435
                background = pygame.image.load('settings.png').convert()
                newscreen = pygame.transform.scale(background, (width, height))
                makeTransRect(182,43,28,435)
                makeTransRect(95,95,mazeX,mazeY)                
                screen.blit(newscreen, (0,0))
                pygame.display.update()
            if 234 <= x <= 415 and 435 <= y <= 478: #Medium
                sleep = 0.01
                speedX = 234
                speedY = 435
                background = pygame.image.load('settings.png').convert()
                newscreen = pygame.transform.scale(background, (width, height))
                makeTransRect(181,43,234,435)
                makeTransRect(95,95,mazeX,mazeY)
                screen.blit(newscreen, (0,0))
                pygame.display.update()
            if 441 <= x <= 622 and 435 <= y <= 478: #Fast
                sleep = 0.005
                speedX = 441
                speedY = 435
                background = pygame.image.load('settings.png').convert()
                newscreen = pygame.transform.scale(background, (width, height))
                makeTransRect(182,43,441,435)
                makeTransRect(95,95,mazeX,mazeY)
                screen.blit(newscreen, (0,0))
                pygame.display.update()
            if 29 <= x <= 124 and 113 <= y <= 207: #maze1
                maze = 'maze.png'
                mazeX = 29
                mazeY = 113
                background = pygame.image.load('settings.png').convert()
                newscreen = pygame.transform.scale(background, (width, height))
                makeTransRect(95,95,29,113)
                makeTransRect(181,43,speedX,speedY)
                screen.blit(newscreen, (0,0))
                pygame.display.update()
            if 156 <= x <= 250 and 113 <= y <= 207: #maze2
                maze = 'maze2.png'
                mazeX = 156
                mazeY = 113
                background = pygame.image.load('settings.png').convert()
                newscreen = pygame.transform.scale(background, (width, height))
                makeTransRect(95,95,156,113)
                makeTransRect(181,43,speedX,speedY)
                screen.blit(newscreen, (0,0))
                pygame.display.update()
            if 282 <= x <= 377 and 113 <= y <= 207: #maze3
                maze = 'maze3.png'
                mazeX = 282
                mazeY = 113
                background = pygame.image.load('settings.png').convert()
                newscreen = pygame.transform.scale(background, (width, height))
                makeTransRect(95,95,282,113)
                makeTransRect(181,43,speedX,speedY)
                screen.blit(newscreen, (0,0))
                pygame.display.update()
            if 406 <= x <= 498 and 113 <= y <= 207: #maze4
                maze = 'maze4.png'
                mazeX = 406
                mazeY = 113
                background = pygame.image.load('settings.png').convert()
                newscreen = pygame.transform.scale(background, (width, height))
                makeTransRect(95,95,406,113)
                makeTransRect(181,43,speedX,speedY)
                screen.blit(newscreen, (0,0))
                pygame.display.update()
            if 528 <= x <= 621 and 113 <= y <= 207: #maze5
                maze = 'maze5.png'
                mazeX = 528
                mazeY = 113
                background = pygame.image.load('settings.png').convert()
                newscreen = pygame.transform.scale(background, (width, height))
                makeTransRect(95,95,528,113)
                makeTransRect(181,43,speedX,speedY)
                screen.blit(newscreen, (0,0))
                pygame.display.update()
            if 29 <= x <= 124 and 239 <= y <= 333: #maze6
                maze = 'maze6.png'
                mazeX = 29
                mazeY = 239
                background = pygame.image.load('settings.png').convert()
                newscreen = pygame.transform.scale(background, (width, height))
                makeTransRect(95,95,29,239)
                makeTransRect(181,43,speedX,speedY)
                screen.blit(newscreen, (0,0))
                pygame.display.update()
            if 156 <= x <= 250 and 239 <= y <= 333: #maze7
                maze = 'maze7.png'
                mazeX = 156
                mazeY = 239
                background = pygame.image.load('settings.png').convert()
                newscreen = pygame.transform.scale(background, (width, height))
                makeTransRect(95,95,156,239)
                makeTransRect(181,43,speedX,speedY)
                screen.blit(newscreen, (0,0))
                pygame.display.update()
            if 282 <= x <= 377 and 239 <= y <= 333: #maze8
                maze = 'maze8.png'
                mazeX = 282
                mazeY = 239
                background = pygame.image.load('settings.png').convert()
                newscreen = pygame.transform.scale(background, (width, height))
                makeTransRect(95,95,282,239)
                makeTransRect(181,43,speedX,speedY)
                screen.blit(newscreen, (0,0))
                pygame.display.update()
            if 406 <= x <= 498 and 239 <= y <= 333: #maze9
                maze = 'maze9.png'
                mazeX = 406
                mazeY = 239
                background = pygame.image.load('settings.png').convert()
                newscreen = pygame.transform.scale(background, (width, height))
                makeTransRect(95,95,406,239)
                makeTransRect(181,43,speedX,speedY)
                screen.blit(newscreen, (0,0))
                pygame.display.update()
            if 528 <= x <= 621 and 239 <= y <= 333: #maze10
                maze = 'maze10.png'
                mazeX = 528
                mazeY = 239
                background = pygame.image.load('settings.png').convert()
                newscreen = pygame.transform.scale(background, (width, height))
                makeTransRect(95,95,528,239)
                makeTransRect(181,43,speedX,speedY)
                screen.blit(newscreen, (0,0))
                pygame.display.update()
    elif event.type == pygame.QUIT:
        pygame.display.quit()
        pygame.quit()
        sys.exit()

#Information Page
background = pygame.image.load('information.png').convert()
newscreen = pygame.transform.scale(background, (width, height))
screen.blit(newscreen, (0,0))
pygame.display.update()

running = True
while running:
    event = pygame.event.wait()
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            x,y = pygame.mouse.get_pos()
            if 190 <= x <= 469 and 516 <= y <= 628:
                running = False
    elif event.type == pygame.QUIT:
        pygame.display.quit()
        pygame.quit()
        sys.exit()

#x = Algorithms(1,15,15) # pass direction, x, y to this
#x.initialize()
#x.rightTurn()

'''
#Run mazes
import rightturn
import deadend
import intersection
import priorities
'''

#================PRIORITIES SCREEN==============
background = pygame.image.load('priorities.png').convert()
newscreen = pygame.transform.scale(background, (width, height))
screen.blit(newscreen, (0,0))
pygame.display.update()
time.sleep(2)

#=====================================PRIORITIES===============================================
img = Image.open(maze)
change = 3
width = img.width * change
height = img.height * change    
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

stepCounterPriorities = 0

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

# Function to move down
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

#Initialization of currentX and currentY
def varsInit(x, y, steps):
    global currentX
    global currentY
    global direction
    global stepCounterPriorities
    stepCounterPriorities = steps
    currentX = x
    currentY = y
    direction = 1
    stepCounterPriorities += 6

#Algorithm to determine direction to move if facing up
def up(replace, steps):
    global direction
    global stepCounterPriorities
    stepCounterPriorities = steps
    if newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace, sleep)
        direction = 2
        stepCounterPriorities += 3
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace, sleep)
        direction = 1
        stepCounterPriorities += 3
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace, sleep)
        direction = 3
        stepCounterPriorities += 3
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace, sleep)
        direction = 4
        stepCounterPriorities += 3
    else:
        if newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
            moveLeft(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 3
            stepCounterPriorities += 3
        elif newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
            moveDown(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 4
            stepCounterPriorities += 3
        elif newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
            moveRight(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 2
            stepCounterPriorities += 3
        elif newscreen.get_at((currentX, currentY - blockSize)) == blue:#up        
            moveUp(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 1
            stepCounterPriorities += 3
    
#Algorithm to determine direction to move if facing right
def right(replace, steps):
    global direction
    global stepCounterPriorities
    stepCounterPriorities = steps
    if newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace, sleep)
        direction = 4
        stepCounterPriorities += 3
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace, sleep)
        direction = 2
        stepCounterPriorities += 3
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace, sleep)
        direction = 1
        stepCounterPriorities += 3
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace, sleep)
        direction = 3
        stepCounterPriorities += 3
    else:
        if newscreen.get_at((currentX, currentY - blockSize)) == blue:#up        
            moveUp(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 1
            stepCounterPriorities += 3
        elif newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
            moveLeft(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 3
            stepCounterPriorities += 3
        elif newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
            moveDown(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 4
            stepCounterPriorities += 3
        elif newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
            moveRight(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 2
            stepCounterPriorities += 3

#Algorithm to determine direction to move if facing left
def left(replace, steps):
    global direction
    global stepCounterPriorities
    stepCounterPriorities = steps
    if newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace, sleep)
        direction = 1
        stepCounterPriorities += 3
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace, sleep)
        direction = 3
        stepCounterPriorities += 3
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace, sleep)
        direction = 4
        stepCounterPriorities += 3
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace, sleep)
        direction = 2
        stepCounterPriorities += 3
    else:
        if newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
            moveDown(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 4
            stepCounterPriorities += 3
        elif newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
            moveRight(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 2
            stepCounterPriorities += 3
        elif newscreen.get_at((currentX, currentY - blockSize)) == blue:#up        
            moveUp(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 1
            stepCounterPriorities += 3
        elif newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
            moveLeft(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 3
            stepCounterPriorities += 3

#Algorithm to determine direction to move if facing down
def down(replace, steps):
    global direction
    global stepCounterPriorities
    stepCounterPriorities = steps
    if newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace, sleep)
        direction = 3
        stepCounterPriorities += 3
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace, sleep)
        direction = 4
        stepCounterPriorities += 3
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace, sleep)
        direction = 2
        stepCounterPriorities += 3
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace, sleep)
        direction = 1
        stepCounterPriorities += 3
    else:
        stepCounterPriorities += 1
        if newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
            moveRight(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 2
            stepCounterPriorities += 3
        elif newscreen.get_at((currentX, currentY - blockSize)) == blue:#up        
            moveUp(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 1
            stepCounterPriorities += 3
        elif newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
            moveLeft(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 3
            stepCounterPriorities += 3
        elif newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
            moveDown(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 4
            stepCounterPriorities += 3

start = datetime.now()

varsInit(xvalueOfStart, yvalueOfStart, stepCounterPriorities)

moveUp(currentX, currentY, blockSize, blue, sleep)
stepCounterPriorities += 1
skipPriorities = False
while 0 != currentY and skipPriorities == False:    
    pygame.event.get()
    stepCounterPriorities += 2
    if direction == 1:#up
        stepCounterPriorities += 1
        up(blue, stepCounterPriorities)
    elif direction == 2:
        stepCounterPriorities += 1
        right(blue, stepCounterPriorities)
    elif direction == 3:
        stepCounterPriorities += 1
        left(blue, stepCounterPriorities)
    elif direction == 4:
        stepCounterPriorities += 1
        down(blue, stepCounterPriorities)
    for event in pygame.event.get():
        stepCounterPriorities += 1        
        # This lets you quit by pressing the X button of the window.
        if event.type == pygame.QUIT:
            stepCounterPriorities += 1
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            stepCounterPriorities += 1
            if event.button == 1:  # 1 = left mouse button, 2 = middle, 3 = right.
                stepCounterPriorities += 1
                x,y = pygame.mouse.get_pos()
                # Skip button
                if 415 <= x <= 532 and 494 <= y <= 532:
                    stepCounterPriorities += 1
                    skipPriorities = True
                    
timePriorities = datetime.now() - start
pygame.image.save(newscreen,'temp.png')
time.sleep(1)

#================RIGHT TURN SCREEN==============
background = pygame.image.load('rightturn.png').convert()
newscreen = pygame.transform.scale(background, (width, height))
screen.blit(newscreen, (0,0))
pygame.display.update()
time.sleep(2)

#=====================================RIGHT TURN===============================================
# Initialize
img = Image.open(maze)
change = 3
width = img.width * change
height = img.height * change
screen = pygame.display.set_mode((width,height))
background = pygame.image.load(maze).convert()
newscreen = pygame.transform.scale(background, (width, height))

#Colors
color = (0, 188, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 188, 0)

stepCounterRightTurn = 0

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

#Initialization of currentX and currentY
def varsInit (x, y, steps):
    global currentX
    global currentY
    global direction
    global stepCounterRightTurn
    stepCounterRightTurn = steps
    currentX = x
    currentY = y
    direction = 1
    stepCounterRightTurn += 6

#Algorithm to determine direction to move if facing up
def up(replace, steps):
    global direction
    global stepCounterRightTurn
    stepCounterRightTurn = steps
    if newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 2
        stepCounterRightTurn += 3
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 1
        stepCounterRightTurn += 3
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 3
        stepCounterRightTurn += 3
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 4
        stepCounterRightTurn += 3
    
#Algorithm to determine direction to move if facing right
def right(replace, steps):
    global direction
    global stepCounterRightTurn
    stepCounterRightTurn = steps
    if newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 4
        stepCounterRightTurn += 3
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 2
        stepCounterRightTurn += 3
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 1
        stepCounterRightTurn += 3
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 3
        stepCounterRightTurn += 3
    
#Algorithm to determine direction to move if facing left
def left(replace, steps):
    global direction
    global stepCounterRightTurn
    stepCounterRightTurn = steps
    if newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 1
        stepCounterRightTurn += 3
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 3
        stepCounterRightTurn += 3
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 4
        stepCounterRightTurn += 3
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 2
        stepCounterRightTurn += 3

#Algorithm to determine direction to move if facing down
def down(replace, steps):
    global direction
    global stepCounterRightTurn
    stepCounterRightTurn = steps
    if newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 3
        stepCounterRightTurn += 3
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 4
        stepCounterRightTurn += 3
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 2
        stepCounterRightTurn += 3
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 1
        stepCounterRightTurn += 3

start = datetime.now()

varsInit(xvalueOfStart, yvalueOfStart, stepCounterRightTurn)

moveUp(currentX, currentY, blockSize, white, sleep+0.005)
stepCounterRightTurn += 1

skipRightTurn = False
#original
while 0 != currentY and skipRightTurn == False:
    stepCounterRightTurn += 2
    pygame.event.get()
    if direction == 1:#up
        stepCounterPriorities += 1
        up(white, stepCounterRightTurn)
    elif direction == 2:
        stepCounterPriorities += 1
        right(white, stepCounterRightTurn)
    elif direction == 3:
        stepCounterRightTurn += 1
        left(white, stepCounterRightTurn)
    elif direction == 4:
        stepCounterRightTurn += 1
        down(white, stepCounterRightTurn)
    for event in pygame.event.get():
        stepCounterRightTurn += 1
        # This lets you quit by pressing the X button of the window.
        if event.type == pygame.QUIT:
            stepCounterRightTurn += 1
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            stepCounterRightTurn += 1       
            if event.button == 1:  # 1 = left mouse button, 2 = middle, 3 = right.
                stepCounterRightTurn += 1
                x,y = pygame.mouse.get_pos()
                if 415 <= x <= 532 and 494 <= y <= 532:
                    stepCounterRightTurn += 1
                    skipRightTurn = True

timeRightTurn = datetime.now() - start
time.sleep(1)

#================DEAD END SCREEN==============
background = pygame.image.load('deadend.png').convert()
newscreen = pygame.transform.scale(background, (width, height))
screen.blit(newscreen, (0,0))
pygame.display.update()
time.sleep(2)

#==============================DEAD END=================================
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
blue = (0, 255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0, 255)

stepCounterDeadEnd = 0

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
def varsInit(x, y, steps):
    global currentX
    global currentY
    global direction
    global stepCounterDeadEnd
    stepCounterDeadEnd = steps
    currentX = x
    currentY = y
    direction = 1
    stepCounterDeadEnd += 6

#Function to determine direction to move if facing up
def up(replace, steps):
    global stepCounterDeadEnd
    stepCounterDeadEnd = steps
    if newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace, sleep)
        stepCounterDeadEnd += 2
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace, sleep)
        stepCounterDeadEnd += 2
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace, sleep)
        stepCounterDeadEnd += 2
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace, sleep)
        stepCounterDeadEnd += 2

    
#Function to determine direction to move if facing right
def right(replace, steps):
    global stepCounterDeadEnd
    stepCounterDeadEnd = steps
    if newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace, sleep)
        stepCounterDeadEnd += 2
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace, sleep)
        stepCounterDeadEnd += 2
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace, sleep)
        stepCounterDeadEnd += 2
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace, sleep)
        stepCounterDeadEnd += 2
    
#Function to determine direction to move if facing left
def left(replace, steps):
    global stepCounterDeadEnd
    stepCounterDeadEnd = steps
    if newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace, sleep)
        stepCounterDeadEnd += 2
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace, sleep)
        stepCounterDeadEnd += 2
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace, sleep)
        stepCounterDeadEnd += 2
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace, sleep)
        stepCounterDeadEnd += 2

#Function to determine direction to move if facing down
def down(replace, steps):
    global stepCounterDeadEnd
    stepCounterDeadEnd = steps
    if newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace, sleep)
        stepCounterDeadEnd += 2
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace, sleep)
        stepCounterDeadEnd += 2
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace, sleep)
        stepCounterDeadEnd += 2
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace, sleep)
        stepCounterDeadEnd += 2

start = datetime.now()

varsInit(xvalueOfStart, yvalueOfStart, stepCounterDeadEnd)

direction = 1
currentX = blockSize
currentY = blockSize
whiteListX = []
whiteListY = []
deadEnds = 1

stepCounterDeadEnd += 6

#-------------DEAD END FILLER------------
while deadEnds != 0:
    pygame.event.get()
    #Define variables
    deadEnds = 0
    intersection = 0
    #Check the color of each and add location to list if white
    stepCounterDeadEnd += 3
    while currentY <= (height - blockSize):
        getCur = newscreen.get_at((currentX, currentY))
        stepCounterDeadEnd += 2
        if getCur == white:
            whiteListX.append(currentX)
            whiteListY.append(currentY)
            stepCounterDeadEnd += 3
        currentX = currentX + blockSize
        stepCounterDeadEnd += 1
        if currentX >= (width - blockSize + 1):
            currentX = 0
            currentY = currentY + blockSize
            stepCounterDeadEnd += 3
    whiteListLength = len(whiteListX)
    stepCounterDeadEnd += 1
    #Determine if each white space is a deadend
    for x in range (0, whiteListLength):
        count = 0
        stepCounterDeadEnd += 1
        if newscreen.get_at((whiteListX[x], whiteListY[x])) != white or newscreen.get_at((whiteListX[x] - blockSize, whiteListY[x])) == black or newscreen.get_at((whiteListX[x] - blockSize, whiteListY[x])) == blue:
            count = count + 1
            stepCounterDeadEnd += 2
        if newscreen.get_at((whiteListX[x], whiteListY[x])) != white or newscreen.get_at((whiteListX[x] + blockSize, whiteListY[x])) == black or newscreen.get_at((whiteListX[x] + blockSize, whiteListY[x])) == blue:
            count = count + 1
            stepCounterDeadEnd += 2
        if newscreen.get_at((whiteListX[x], whiteListY[x])) != white or newscreen.get_at((whiteListX[x], whiteListY[x] - blockSize)) == black or newscreen.get_at((whiteListX[x], whiteListY[x] - blockSize)) == blue:
            count = count + 1
            stepCounterDeadEnd += 2
        if newscreen.get_at((whiteListX[x], whiteListY[x])) != white or newscreen.get_at((whiteListX[x], whiteListY[x] + blockSize)) == black or newscreen.get_at((whiteListX[x], whiteListY[x] + blockSize)) == blue:
            count = count + 1
            stepCounterDeadEnd += 2
        if count == 3:
            deadEnds = deadEnds + 1
            pygame.draw.rect(newscreen, blue, pygame.Rect(whiteListX[x], whiteListY[x], blockSize, blockSize))
            stepCounterDeadEnd += 3
        if count < 3:
            intersection == 1
            stepCounterDeadEnd += 2
    #Break the while loop once all dead ends are filled
    if deadEnds == intersection:
        stepCounterDeadEnd += 1
        break

    screen.blit(newscreen, (0,0))
    pygame.display.update()
    stepCounterDeadEnd += 2

varsInit(xvalueOfStart, yvalueOfStart, stepCounterDeadEnd)

moveUp(currentX, currentY, blockSize, white, sleep)
stepCounterDeadEnd += 1
skipDeadEnd = False
#Right turn movement through the solution
while 0 != currentY and skipDeadEnd == False:
    stepCounterDeadEnd += 2
    pygame.event.get()
    if direction == 1:#up
        stepCounterDeadEnd += 1
        up(white, stepCounterDeadEnd)
    elif direction == 2:
        stepCounterDeadEnd += 1
        right(white, stepCounterDeadEnd)
    elif direction == 3:
        stepCounterDeadEnd += 1
        left(white, stepCounterDeadEnd)
    elif direction == 4:
        stepCounterDeadEnd += 1
        down(white, stepCounterDeadEnd)
    for event in pygame.event.get():
        # This lets you quit by pressing the X button of the window.
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # 1 = left mouse button, 2 = middle, 3 = right.
                x,y = pygame.mouse.get_pos()
                if 415 <= x <= 532 and 494 <= y <= 532:
                    skipDeadEnd = True                                                                                                        

timeDeadEnd = datetime.now() - start

time.sleep(1)

#================INTERSECTION SCREEN==============
background = pygame.image.load('intersection.png').convert()
newscreen = pygame.transform.scale(background, (width, height))
screen.blit(newscreen, (0,0))
pygame.display.update()
time.sleep(2)

#===========================Intersection===============================

# Initialize
img = Image.open(maze)
change = 3
width = img.width * change
height = img.height * change
screen = pygame.display.set_mode((width,height))
background = pygame.image.load(maze).convert()
newscreen = pygame.transform.scale(background, (width, height))
sleepTime = sleep
stepCounterIntersection = 0

#set upMem,leftMem,rightMem to values from memory(pathCount.txt)
resetMem=False
upMem=0
leftMem=0
rightMem=0
y=0
stepCounterIntersection += 5
    #if memory needs to be reset, then set memory to 0 up, 0 left, 0 right
if resetMem:
    f = open('pathCount.txt','w')
    f.write("0U0L0R")
    f.close
    stepCounterIntersection += 4
    #set memory to pathCount.txt
f = open('pathCount.txt','r')
memory = f.read()
f.close
stepCounterIntersection += 3
    #set memory values to values in memory(pathCount.txt)
for z in range(len(memory)):
    stepCounterIntersection += 1
    if memory[z]=='U':
        upMem=int(memory[y:z])
        y=z+1
        stepCounterIntersection += 2
    elif memory[z]=='L':
        leftMem=int(memory[y:z])
        y=z+1
        stepCounterIntersection += 2
    elif memory[z]=='R':
        rightMem=int(memory[y:z])
        stepCounterIntersection += 2


#number of turns
upCount = 0
leftCount = 0
rightCount = 0

#Colors
color = (0, 188, 0)
white = (255, 255, 255)
black = (0, 0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 188, 0)

# Recognizing black/white
#-print(width, height)
size = [img.size]
#-print(size[0])
colors = img.getcolors()
#-print(colors)
pix = img.load()
list = []

# Locate the starting coordinate
for x in range(0,180):
    if pix[x,179] == (255, 255, 255, 255):
        list.append(x)

xvalueOfStart = list[0] * change
#-print(xvalueOfStart)

blockSize = len(list) * change

yvalueOfStart = height - blockSize

list = []

# Locate the ending coordinate
for x in range(0,180):
    if pix[x,0] == (255, 255, 255, 255):
        list.append(x)

xvalueOfEnd = list[0] * change
#-print(xvalueOfEnd)

pygame.draw.rect(newscreen, color, pygame.Rect(xvalueOfStart, yvalueOfStart, blockSize, blockSize))
screen.blit(newscreen, (0,0))
pygame.display.update()
time.sleep(sleepTime)

# Function to move forward
def moveUp(x, y, blocksize, newcolor):
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blockSize, blockSize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x+1, y - blocksize+1, blockSize-2, blockSize-2))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentY
    global currentX
    currentY = y - blocksize
    currentX = x

# Function to move down
def moveDown(x, y, blocksize, newcolor):
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blockSize, blockSize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x+1, y + blocksize+1, blockSize-2, blockSize-2))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentY
    global currentX    
    currentY = y + blocksize
    currentX = x   
    
# Function to move left  
def moveLeft(x, y, blocksize, newcolor):
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blockSize, blockSize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x - blocksize+1, y+1, blockSize-2, blockSize-2))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentX
    global currentY        
    currentX = x - blocksize
    currentY = y

# Function to move right
def moveRight(x, y, blocksize, newcolor):
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blockSize, blockSize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x + blocksize+1, y+1, blockSize-2, blockSize-2))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentX
    global currentY        
    currentX = x + blocksize
    currentY = y

#Initialization of currentX and currentY
def varsInit(x, y, steps):
    global currentX
    global currentY
    global direction
    global stepCounterIntersection
    stepCounterIntersection = steps
    currentX = x
    currentY = y
    direction = 1
    stepCounterIntersection += 6

#Algorithm to determine direction to move if facing up
def up(replace, steps):
    global direction
    global stepCounterIntersection
    stepCounterIntersection = steps
    if newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace)
        time.sleep(sleepTime)
        direction = 1
        stepCounterIntersection += 3
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace)
        time.sleep(sleepTime)
        direction = 2
        stepCounterIntersection += 3
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace)
        time.sleep(sleepTime)
        direction = 3
        stepCounterIntersection += 3
        #check for blue paths
    elif newscreen.get_at((currentX,currentY-blockSize))==blue:
        moveUp(currentX, currentY, blockSize, replace)
        time.sleep(sleepTime)
        direction = 1
        stepCounterIntersection += 3
    elif newscreen.get_at((currentX+blockSize,currentY))==blue:
        time.sleep(sleepTime)
        direction = 2
        stepCounterIntersection += 3
    elif newscreen.get_at((currentX-blockSize,currentY))==blue:
        moveLeft(currentX, currentY, blockSize, replace)
        time.sleep(sleepTime)
        direction = 3
        stepCounterIntersection += 3
        #check rear
    elif newscreen.get_at((currentX, currentY + blockSize)) == white or newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
        moveDown(currentX, currentY, blockSize, replace)
        time.sleep(sleepTime)
        direction = 4
        stepCounterIntersection += 3
    
#Algorithm to determine direction to move if facing right
def right(replace, steps):
    global direction
    global stepCounterIntersection
    stepCounterIntersection = steps
    if newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace)
        time.sleep(sleepTime)
        direction = 2
        stepCounterIntersection += 3
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace)
        time.sleep(sleepTime)
        direction = 4
        stepCounterIntersection += 3
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace)
        time.sleep(sleepTime)
        direction = 1
        stepCounterIntersection += 3
    #check blue
    elif newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
        moveRight(currentX, currentY, blockSize, replace)
        time.sleep(sleepTime)
        direction = 2
        stepCounterIntersection += 3
    elif newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
        moveDown(currentX, currentY, blockSize, replace)
        time.sleep(sleepTime)
        direction = 4
        stepCounterIntersection += 3
    elif newscreen.get_at((currentX, currentY - blockSize)) == blue:#up        
        moveUp(currentX, currentY, blockSize, replace)
        time.sleep(sleepTime)
        direction = 1
        stepCounterIntersection += 3
    #check rear
    elif newscreen.get_at((currentX - blockSize, currentY)) == white or newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
        moveLeft(currentX, currentY, blockSize, replace)
        time.sleep(sleepTime)
        direction = 3
        stepCounterIntersection += 3
    
#Algorithm to determine direction to move if facing left
def left(replace, steps):
    global direction
    global stepCounterIntersection
    stepCounterIntersection = steps
    if newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace)
        time.sleep(sleepTime)
        direction = 3
        stepCounterIntersection += 3
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up
        moveUp(currentX, currentY, blockSize, replace)
        time.sleep(sleepTime)
        direction = 1
        stepCounterIntersection += 3
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down        
        moveDown(currentX, currentY, blockSize, replace)
        time.sleep(sleepTime)
        direction = 4
        stepCounterIntersection += 3
        #check blue
    elif newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
        moveLeft(currentX, currentY, blockSize, replace)
        time.sleep(sleepTime)
        direction = 3
        stepCounterIntersection += 3
    elif newscreen.get_at((currentX, currentY - blockSize)) == blue:#up
        moveUp(currentX, currentY, blockSize, replace)
        time.sleep(sleepTime)
        direction = 1
        stepCounterIntersection += 3
    elif newscreen.get_at((currentX, currentY + blockSize)) == blue:#down        
        moveDown(currentX, currentY, blockSize, replace)
        time.sleep(sleepTime)
        direction = 4
        stepCounterIntersection += 3
        #check rear
    elif newscreen.get_at((currentX + blockSize, currentY)) == white or newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
        moveRight(currentX, currentY, blockSize, replace)
        time.sleep(sleepTime)
        direction = 2
        stepCounterIntersection += 3

#Algorithm to determine direction to move if facing down
def down(replace, steps):
    global direction
    global stepCounterIntersection
    stepCounterIntersection = steps
    if newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace)
        time.sleep(sleepTime)
        direction = 4
        stepCounterIntersection += 4
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace)
        time.sleep(sleepTime)
        direction = 3
        stepCounterIntersection += 4
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace)
        time.sleep(sleepTime)
        direction = 2
        stepCounterIntersection += 4
        #check blue
    elif newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
        moveDown(currentX, currentY, blockSize, replace)
        time.sleep(sleepTime)
        direction = 4
        stepCounterIntersection += 4
    elif newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
        moveLeft(currentX, currentY, blockSize, replace)
        time.sleep(sleepTime)
        direction = 3
        stepCounterIntersection += 4
    elif newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
        moveRight(currentX, currentY, blockSize, replace)
        time.sleep(sleepTime)
        direction = 2
        stepCounterIntersection += 4
        #check rear
    elif newscreen.get_at((currentX, currentY - blockSize)) == white or newscreen.get_at((currentX, currentY - blockSize)) == blue:#up        
        moveUp(currentX, currentY, blockSize, replace)
        time.sleep(sleepTime)
        direction = 1
        stepCounterIntersection += 4

#returns boolean if current tile is intersection
def isIntersection(steps):
    global direction
    global stepCounterIntersection
    stepCounterIntersection = steps
    paths = 0 
    stepCounterIntersection += 2
    if newscreen.get_at((currentX, currentY - blockSize)) == white or newscreen.get_at((currentX, currentY - blockSize)) == red or newscreen.get_at((currentX, currentY - blockSize)) == green or newscreen.get_at((currentX, currentY - blockSize)) == blue:
        paths = paths + 1
        stepCounterIntersection += 2
    if newscreen.get_at((currentX - blockSize, currentY)) == white or newscreen.get_at((currentX - blockSize, currentY)) == red or newscreen.get_at((currentX - blockSize, currentY)) == green or newscreen.get_at((currentX - blockSize, currentY)) == blue:
        paths = paths + 1
        stepCounterIntersection += 2
    if newscreen.get_at((currentX + blockSize, currentY)) == white or newscreen.get_at((currentX + blockSize, currentY)) == red or newscreen.get_at((currentX + blockSize, currentY)) == green or newscreen.get_at((currentX + blockSize, currentY)) == blue:
        paths = paths + 1
        stepCounterIntersection += 2
    if  newscreen.get_at((currentX, currentY + blockSize)) == white or newscreen.get_at((currentX, currentY + blockSize)) == red or newscreen.get_at((currentX, currentY + blockSize)) == green or newscreen.get_at((currentX, currentY + blockSize)) == blue:
        paths = paths + 1
        stepCounterIntersection += 2
    
    if paths > 2:
        return True
        stepCounterIntersection += 2
    else:
        return False
        stepCounterIntersection += 2

varsInit(xvalueOfStart, yvalueOfStart, stepCounterIntersection)

moveUp(currentX, currentY, blockSize, white)

direction = 1
stepCounterIntersection += 2
def checkSurround(color, steps):#returns direction or 0 if no color present on intersection paths
    global direction
    global stepCounterIntersection
    stepCounterIntersection = steps
    paths=0
    x=0
    stepCounterIntersection += 3
    if newscreen.get_at((currentX, currentY - blockSize)) == color:#up
        paths+=1
        x=1
        stepCounterIntersection += 2
    if newscreen.get_at((currentX + blockSize, currentY)) == color:#right
        paths+=1
        x=2
        stepCounterIntersection += 2
    if newscreen.get_at((currentX - blockSize, currentY)) == color:#left
        paths+=1
        x=3
        stepCounterIntersection += 2
    if newscreen.get_at((currentX,currentY+blockSize))==color:#down
        paths+=1
        x=4
        stepCounterIntersection += 2
    if paths>1:
        x=5
        stepCounterIntersection += 1
    return x

def addCount(isInt,directionMove,firstTime, steps):
    global direction,rightCount,upCount,leftCount
    global stepCounterIntersection
    stepCounterIntersection = steps
    stepCounterIntersection += 4
    if isInt:
        stepCounterIntersection += 1
        if checkSurround(red, stepCounterIntersection)==4:#AI faces up
            stepCounterIntersection += 1
            if directionMove==1:#up
                upCount+=1
                stepCounterIntersection += 2
            if directionMove==3:#left
                leftCount+=1
                stepCounterIntersection += 2
            if directionMove==2:#right
                rightCount+=1
                stepCounterIntersection += 2
            if direction==4:#AI comes from top
                upCount-=1
                stepCounterIntersection += 2
            if direction==3:#AI comes from right
                rightCount-=1
                stepCounterIntersection += 2
            if direction==2:#AI comes from left
                leftCount-=1
                stepCounterIntersection += 2
        if checkSurround(red, stepCounterIntersection)==3:#AI faces right
            stepCounterIntersection += 1
            if directionMove==2:#right
                upCount+=1
                stepCounterIntersection += 2
            if directionMove==1:#up
                leftCount+=1
                stepCounterIntersection += 2
            if directionMove==4:#down
                rightCount+=1
                stepCounterIntersection += 2
            if direction==3:#AI comes from right
                upCount-=1
                stepCounterIntersection += 2
            if direction==1:#AI comes from bottom
                rightCount-=1
                stepCounterIntersection += 2
            if direction==4:#AI comes from top
                leftCount-=1
                stepCounterIntersection += 2
        if checkSurround(red, stepCounterIntersection)==2:#AI faces left
            stepCounterIntersection += 1
            if directionMove==3:#left
                upCount+=1
                stepCounterIntersection += 2
            if directionMove==4:#down
                leftCount+=1
                stepCounterIntersection += 2
            if directionMove==1:#up
                rightCount+=1
                stepCounterIntersection += 2
            if direction==2:#AI comes from left
                upCount-=1
                stepCounterIntersection += 2
            if direction==4:#AI comes from top
                rightCount-=1
                stepCounterIntersection += 2
            if direction==1:#AI comes from bottom
                leftCount-=1
                stepCounterIntersection += 2
        if checkSurround(red, stepCounterIntersection)==1:#AI faces down
            stepCounterIntersection += 1
            if directionMove==4:#down
                upCount+=1
                stepCounterIntersection += 2
            if directionMove==2:#right
                leftCount+=1
                stepCounterIntersection += 2
            if directionMove==3:#left
                rightCount+=1
                stepCounterIntersection += 2
            if direction==1:#AI comes from bottom
                upCount-=1
                stepCounterIntersection += 2
            if direction==2:#AI comes from left
                rightCount-=1
                stepCounterIntersection += 2
            if direction==3:#AI comes from right
                leftCount-=1
                stepCounterIntersection += 2
        #check blue
        if checkSurround(red, stepCounterIntersection)==0:
            stepCounterIntersection += 1
            if checkSurround(blue, stepCounterIntersection)==4:#AI faces up
                stepCounterIntersection += 1
                if directionMove==1:#up
                    upCount+=1
                    stepCounterIntersection += 2
                if directionMove==3:#left
                    leftCount+=1
                    stepCounterIntersection += 2
                if directionMove==2:#right
                    rightCount+=1
                    stepCounterIntersection += 2
                if direction==4:#AI comes from top
                    upCount-=1
                    stepCounterIntersection += 2
                if direction==3:#AI comes from right
                    rightCount-=1
                    stepCounterIntersection += 2
                if direction==2:#AI comes from left
                    leftCount-=1
                    stepCounterIntersection += 2
            if checkSurround(blue, stepCounterIntersection)==3:#AI faces right
                stepCounterIntersection += 1
                if directionMove==2:#right
                    upCount+=1
                    stepCounterIntersection += 2
                if directionMove==1:#up
                    leftCount+=1
                    stepCounterIntersection += 2
                if directionMove==4:#down
                    rightCount+=1
                    stepCounterIntersection += 2
                if direction==3:#AI comes from right
                    upCount-=1
                    stepCounterIntersection += 2
                if direction==1:#AI comes from bottom
                    rightCount-=1
                    stepCounterIntersection += 2
                if direction==4:#AI comes from top
                    leftCount-=1
                    stepCounterIntersection += 2
            if checkSurround(blue, stepCounterIntersection)==2:#AI faces left
                stepCounterIntersection += 1
                if directionMove==3:#left
                    upCount+=1
                    stepCounterIntersection += 2
                if directionMove==4:#down
                    leftCount+=1
                    stepCounterIntersection += 2
                if directionMove==1:#up
                    rightCount+=1
                    stepCounterIntersection += 2
                if direction==2:#AI comes from left
                    upCount-=1
                    stepCounterIntersection += 2
                if direction==4:#AI comes from top
                    rightCount-=1
                    stepCounterIntersection += 2
                if direction==1:#AI comes from bottom
                    leftCount-=1
                    stepCounterIntersection += 2
            if checkSurround(blue, stepCounterIntersection)==1:#AI faces down
                stepCounterIntersection += 1
                if directionMove==4:#down
                    upCount+=1
                    stepCounterIntersection += 2
                if directionMove==2:#right
                    leftCount+=1
                    stepCounterIntersection += 2
                if directionMove==3:#left
                    rightCount+=1
                    stepCounterIntersection += 2
                if direction==1:#AI comes from bottom
                    upCount-=1
                    stepCounterIntersection += 2
                if direction==2:#AI comes from left
                    rightCount-=1
                    stepCounterIntersection += 2
                if direction==3:#AI comes from right
                    leftCount-=1
                    stepCounterIntersection += 2

def turnAround(facing, steps):
    global direction
    global stepCounterIntersection
    stepCounterIntersection = steps
    stepCounterIntersection += 1
    if facing==1:
        direction=4
        stepCounterIntersection += 2
    elif facing==2:
        direction=3
        stepCounterIntersection += 2
    elif facing==3:
        direction=2
        stepCounterIntersection += 2
    elif facing==4:
        direction=1
        stepCounterIntersection += 2

def moveForward(color, steps):
    global direction
    global stepCounterIntersection
    stepCounterIntersection = steps
    stepCounterIntersection += 1
    if direction==1:
        moveUp(currentX,currentY,blockSize,color)
        stepCounterIntersection += 2
    elif direction==2:
        moveRight(currentX,currentY,blockSize,color)
        stepCounterIntersection += 2
    elif direction==3:
        moveLeft(currentX,currentY,blockSize,color)
        stepCounterIntersection += 2
    elif direction==4:
        moveDown(currentX,currentY,blockSize,color)
        stepCounterIntersection += 2

intersectionX=[]
intersectionY=[]
blueIntX=[]
blueIntY=[]
intersectionNum=0
redDirection=0
stepCounterIntersection += 6
# Check if all paths of an intersection have been travelled. If so, go back on red
def intersection(isInt,firstTime, steps):
    global direction, upCount, rightCount, leftCount, intersectionX,intersectionY,blueIntX,blueIntY, intersectionNum, redDirection
    global stepCounterIntersection
    stepCounterIntersection = steps
    finished=False
    stepCounterIntersection += 1
    if firstTime:#if first time at intersection, then add x/y cordinates of red
        stepCounterIntersection += 1
        if direction==1:#facing up
            intersectionX.append(currentX)
            intersectionY.append(currentY+blockSize)
            stepCounterIntersection += 3
        elif direction==2:#facing right
            intersectionX.append(currentX-blockSize)
            intersectionY.append(currentY)
            stepCounterIntersection += 3
        elif direction==3:#facing left
            intersectionX.append(currentX+blockSize)
            intersectionY.append(currentY)
            stepCounterIntersection += 3
        elif direction==4:#facing down
            intersectionX.append(currentX)
            intersectionY.append(currentY-blockSize)
            stepCounterIntersection += 3
        blueIntX=[].append(currentX)
        blueIntY=[].append(currentY)
        stepCounterIntersection += 2
        
    for z in range(0,len(intersectionX)):#go through array of intersections
        #====RED====
        stepCounterIntersection += 1
        if intersectionX[z]==currentX-blockSize and intersectionY[z]==currentY:#left
            stepCounterIntersection += 1
            if z!=len(intersectionX)-1:#if z is not last item in array, that means there are still incomplete intersections after this one
                addCount(isInt,2,firstTime,stepCounterIntersection)
                turnAround(direction, stepCounterIntersection)
                moveForward(blue, stepCounterIntersection)
                finished=True
                stepCounterIntersection += 5
                break
        elif intersectionX[z]==currentX+blockSize and intersectionY[z]==currentY:#right
            stepCounterIntersection += 1
            if z!=len(intersectionX)-1:#intersections traveled after this one are not completed
                addCount(isInt,3,firstTime, stepCounterIntersection)
                turnAround(direction, stepCounterIntersection)
                moveForward(blue, stepCounterIntersection)
                finished=True
                stepCounterIntersection += 5
                break
        elif intersectionY[z]==currentY-blockSize and intersectionX[z]==currentX:#up
            stepCounterIntersection += 1
            if z!=len(intersectionX)-1:#intersections traveled after this one are not completed
                addCount(isInt, 4,firstTime, stepCounterIntersection)
                turnAround(direction, stepCounterIntersection)
                moveForward(blue,stepCounterIntersection)
                finished=True
                stepCounterIntersection += 5
                break
        elif intersectionY[z]==currentY+blockSize and intersectionX[z]==currentX:#down
            stepCounterIntersection += 1
            if z!=len(intersectionX)-1:#intersections traveled after this one are not completed
                addCount(isInt,1,firstTime, stepCounterIntersection)
                turnAround(direction, stepCounterIntersection)
                moveForward(blue, stepCounterIntersection)
                finished=True
                stepCounterIntersection += 5
                break

    if checkSurround(white, stepCounterIntersection)!=0:#white(untraveled) paths still present
        stepCounterIntersection += 1
        if checkSurround(red, stepCounterIntersection)==1:
            redDirection=4
            stepCounterIntersection += 2
        elif checkSurround(red, stepCounterIntersection)==2:
            redDirection=3
            stepCounterIntersection += 2
        elif checkSurround(red, stepCounterIntersection)==3:
            redDirection=2
            stepCounterIntersection += 2
        elif checkSurround(red, stepCounterIntersection)==4:
            redDirection=1
            stepCounterIntersection += 2
        elif checkSurround(blue, stepCounterIntersection)==1:
            redDirection=4
            stepCounterIntersection += 2
        elif checkSurround(blue, stepCounterIntersection)==2:
            redDirection=3
            stepCounterIntersection += 2
        elif checkSurround(blue, stepCounterIntersection)==3:
            redDirection=2
            stepCounterIntersection += 2
        elif checkSurround(blue, stepCounterIntersection)==4:
            redDirection=1
            stepCounterIntersection += 2

        if redDirection==1:#if AI facing up/red on bottom
            stepCounterIntersection += 1
            if upMem>=leftMem and upMem>=rightMem and newscreen.get_at((currentX, currentY - blockSize)) == white:#up
                addCount(isInt,1,firstTime, stepCounterIntersection)
                direction = 1
                moveUp(currentX, currentY, blockSize, blue)
                stepCounterIntersection += 4
            elif rightMem>=upMem and rightMem>=leftMem and newscreen.get_at((currentX + blockSize, currentY)) == white:#right
                addCount(isInt,2,firstTime, stepCounterIntersection)
                direction = 2
                moveRight(currentX, currentY, blockSize, blue)
                stepCounterIntersection += 4
            elif leftMem>=upMem and leftMem>=rightMem and newscreen.get_at((currentX - blockSize, currentY)) == white:#left
                addCount(isInt,3,firstTime, stepCounterIntersection)
                direction = 3
                moveLeft(currentX, currentY, blockSize, blue)
                stepCounterIntersection += 4
            else:
                stepCounterIntersection += 1
                if newscreen.get_at((currentX, currentY - blockSize)) == white:#up
                    addCount(isInt,1,firstTime, stepCounterIntersection)
                    direction = 1
                    moveUp(currentX, currentY, blockSize, blue)
                    stepCounterIntersection += 4
                elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
                    addCount(isInt,2,firstTime, stepCounterIntersection)
                    direction = 2
                    moveRight(currentX, currentY, blockSize, blue)
                    stepCounterIntersection += 4
                elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
                    addCount(isInt,3,firstTime, stepCounterIntersection)
                    direction = 3
                    moveLeft(currentX, currentY, blockSize, blue)
                    stepCounterIntersection += 4
        elif redDirection==2:#right
            stepCounterIntersection += 1
            if upMem>=leftMem and upMem>=rightMem and newscreen.get_at((currentX + blockSize, currentY)) == white:#right
                addCount(isInt,2,firstTime, stepCounterIntersection)
                direction = 2
                moveRight(currentX, currentY, blockSize, blue)
                stepCounterIntersection += 4
            elif rightMem>=upMem and rightMem>=leftMem and newscreen.get_at((currentX, currentY + blockSize)) == white:#down
                addCount(isInt,4,firstTime, stepCounterIntersection)
                direction = 4
                moveDown(currentX, currentY, blockSize, blue)
                stepCounterIntersection += 4
            elif leftMem>=upMem and leftMem>=rightMem and newscreen.get_at((currentX, currentY - blockSize)) == white:#up
                addCount(isInt,1,firstTime, stepCounterIntersection)
                direction = 1
                moveUp(currentX, currentY, blockSize, blue)
                stepCounterIntersection += 4
            else:
                stepCounterIntersection += 1
                if newscreen.get_at((currentX + blockSize, currentY)) == white:#right
                    addCount(isInt,2,firstTime, stepCounterIntersection)
                    direction = 2
                    moveRight(currentX, currentY, blockSize, blue)
                    stepCounterIntersection += 4
                elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
                    addCount(isInt,4,firstTime, stepCounterIntersection)
                    direction = 4
                    moveDown(currentX, currentY, blockSize, blue)
                    stepCounterIntersection += 4
                elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up
                    addCount(isInt,1,firstTime, stepCounterIntersection)
                    direction = 1
                    moveUp(currentX, currentY, blockSize, blue)
                    stepCounterIntersection += 4
        elif redDirection==3:#left
            stepCounterIntersection += 1
            if upMem>=leftMem and upMem>=rightMem and newscreen.get_at((currentX - blockSize, currentY)) == white:#left
                addCount(isInt,3,firstTime, stepCounterIntersection)
                direction = 3
                moveLeft(currentX, currentY, blockSize, blue)
                stepCounterIntersection += 4
            elif rightMem>=upMem and rightMem>=leftMem and newscreen.get_at((currentX, currentY - blockSize)) == white:#up
                addCount(isInt,1,firstTime, stepCounterIntersection)
                direction = 1
                moveUp(currentX, currentY, blockSize, blue)
                stepCounterIntersection += 4
            elif leftMem>=upMem and leftMem>=rightMem and newscreen.get_at((currentX, currentY + blockSize)) == white:#down
                addCount(isInt,4,firstTime, stepCounterIntersection)
                direction = 4
                moveDown(currentX, currentY, blockSize, blue)
                stepCounterIntersection += 4
            else:
                stepCounterIntersection += 4
                if newscreen.get_at((currentX - blockSize, currentY)) == white:#left
                    addCount(isInt,3,firstTime, stepCounterIntersection)
                    direction = 3
                    moveLeft(currentX, currentY, blockSize, blue)
                    stepCounterIntersection += 4
                elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up
                    addCount(isInt,1,firstTime, stepCounterIntersection)
                    direction = 1
                    moveUp(currentX, currentY, blockSize, blue)
                    stepCounterIntersection += 4
                elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
                    addCount(isInt,4,firstTime, stepCounterIntersection)
                    direction = 4
                    moveDown(currentX, currentY, blockSize, blue)
                    stepCounterIntersection += 4
        elif redDirection==4:#down
            stepCounterIntersection += 1
            if upMem>=leftMem and upMem>=rightMem and newscreen.get_at((currentX, currentY + blockSize)) == white:#down
                addCount(isInt,4,firstTime, stepCounterIntersection)
                direction = 4
                moveDown(currentX, currentY, blockSize, blue)
                stepCounterIntersection += 4
            elif rightMem>=upMem and rightMem>=leftMem and newscreen.get_at((currentX - blockSize, currentY)) == white:#left
                addCount(isInt,3,firstTime, stepCounterIntersection)
                direction = 3
                moveLeft(currentX, currentY, blockSize, blue)
                stepCounterIntersection += 4
            elif leftMem>=upMem and leftMem>=rightMem and newscreen.get_at((currentX + blockSize, currentY)) == white:#right
                addCount(isInt,2,firstTime, stepCounterIntersection)
                direction = 2
                moveRight(currentX, currentY, blockSize, blue)
                stepCounterIntersection += 4
            else:
                stepCounterIntersection += 1
                if newscreen.get_at((currentX, currentY + blockSize)) == white:#down
                    addCount(isInt,4,firstTime, stepCounterIntersection)
                    direction = 4
                    moveDown(currentX, currentY, blockSize, blue)
                    stepCounterIntersection += 4
                elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
                    addCount(isInt,3,firstTime, stepCounterIntersection)
                    direction = 3
                    moveLeft(currentX, currentY, blockSize, blue)
                    stepCounterIntersection += 4
                elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
                    addCount(isInt,2,firstTime, stepCounterIntersection)
                    direction = 2
                    moveRight(currentX, currentY, blockSize, blue)
                    stepCounterIntersection += 4
                    
    elif finished==False and checkSurround(red, stepCounterIntersection) == 0:#no red
        stepCounterIntersection += 1
        if newscreen.get_at((currentX, currentY - blockSize)) == blue:#up
            addCount(isInt,1,firstTime, stepCounterIntersection)
            direction = 1
            moveUp(currentX, currentY, blockSize, blue)
            del intersectionX[intersectionNum-1]
            del intersectionY[intersectionNum-1]
            intersectionNum-=1
            stepCounterIntersection += 7
        elif newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
            addCount(isInt,2,firstTime, stepCounterIntersection)
            direction=2
            moveRight(currentX, currentY, blockSize, blue)
            del intersectionX[intersectionNum-1]
            del intersectionY[intersectionNum-1]
            intersectionNum-=1
            stepCounterIntersection += 7
        elif newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
            addCount(isInt,3,firstTime, stepCounterIntersection)
            direction=3
            moveLeft(currentX, currentY, blockSize, blue)
            del intersectionX[intersectionNum-1]
            del intersectionY[intersectionNum-1]
            intersectionNum-=1
            stepCounterIntersection += 7
        elif newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
            addCount(isInt,4,firstTime, stepCounterIntersection)
            direction = 4
            moveDown(currentX, currentY, blockSize, blue)
            del intersectionX[intersectionNum-1]
            del intersectionY[intersectionNum-1]
            intersectionNum-=1
            stepCounterIntersection += 7
    elif checkSurround(red, stepCounterIntersection)==1:#red on top
        addCount(isInt,1,firstTime, stepCounterIntersection)
        direction = 1
        moveUp(currentX, currentY, blockSize, blue)
        del intersectionX[intersectionNum-1]
        del intersectionY[intersectionNum-1]
        intersectionNum-=1
        stepCounterIntersection += 7
    elif checkSurround(red, stepCounterIntersection)==2:#red on right
        addCount(isInt,2,firstTime, stepCounterIntersection)
        direction = 2
        moveRight(currentX, currentY, blockSize, blue)
        del intersectionX[intersectionNum-1]
        del intersectionY[intersectionNum-1]
        intersectionNum-=1
        stepCounterIntersection += 7
    elif checkSurround(red, stepCounterIntersection)==3:#red on left
        addCount(isInt,3,firstTime, stepCounterIntersection)
        direction = 3
        moveLeft(currentX, currentY, blockSize, blue)
        del intersectionX[intersectionNum-1]
        del intersectionY[intersectionNum-1]
        intersectionNum-=1
        stepCounterIntersection += 7
    elif checkSurround(red, stepCounterIntersection)==4:#red on bottom
        addCount(isInt,4,firstTime, stepCounterIntersection)
        direction = 4
        moveDown(currentX, currentY, blockSize, blue)
        del intersectionX[intersectionNum-1]
        del intersectionY[intersectionNum-1]
        intersectionNum-=1
        stepCounterIntersection += 7

# ------------- OUR ALGORITHM -------------
start = datetime.now()
skipIntersection = False
while 0 != currentY and skipIntersection == False:
    pygame.event.get()
    stepCounterIntersection += 4
#for x in range(0,10):
    getCur = newscreen.get_at((currentX, currentY))
    isInt=isIntersection(stepCounterIntersection)
    if direction == 1:#up
        stepCounterIntersection += 1
        if isInt:
            stepCounterIntersection += 1
            if getCur == blue:#blue=intersection tile
                moveDown(currentX, currentY, blockSize, blue)
                moveUp(currentX, currentY, blockSize, green)#green=used path
                intersection(isInt,False, stepCounterIntersection)
                stepCounterIntersection += 4
            else:
                stepCounterIntersection += 1
                if newscreen.get_at((currentX, currentY + blockSize)) != blue:#down
                    stepCounterIntersection += 2
                    pygame.draw.rect(newscreen, red, pygame.Rect(currentX, currentY+blockSize, blockSize, blockSize))#set red path into intersection
                pygame.draw.rect(newscreen, blue, pygame.Rect(currentX, currentY, blockSize, blockSize))#set current space to blue
                intersectionNum+=1
                intersection(isInt,True, stepCounterIntersection)
                stepCounterIntersection += 3
        else:
            stepCounterIntersection += 1
            if newscreen.get_at((currentX, currentY - blockSize)) == blue:
                moveUp(currentX, currentY, blockSize, white)
                stepCounterIntersection += 2
            else:
                stepCounterIntersection += 2
                up(white, stepCounterIntersection)
    elif direction == 2:#right
        stepCounterIntersection += 1
        if isInt:
            stepCounterIntersection += 1
            if getCur == blue:#blue=intersection tile
                stepCounterIntersection += 4
                moveLeft(currentX, currentY, blockSize, blue)
                moveRight(currentX, currentY, blockSize, green)#green=used path
                intersection(isInt,False, stepCounterIntersection)
            else:
                stepCounterIntersection += 1
                if newscreen.get_at((currentX-blockSize, currentY)) != blue:#left
                    stepCounterIntersection += 3
                    pygame.draw.rect(newscreen, red, pygame.Rect(currentX-blockSize, currentY, blockSize, blockSize))#set red path into intersection
                pygame.draw.rect(newscreen, blue, pygame.Rect(currentX, currentY, blockSize, blockSize))#set current space to blue
                intersectionNum+=1
                intersection(isInt,True, stepCounterIntersection)
                stepCounterIntersection += 3
        else:
            stepCounterIntersection += 1
            if newscreen.get_at((currentX + blockSize, currentY)) == blue:
                moveRight(currentX, currentY, blockSize, white)
                stepCounterIntersection += 2
            else:
                right(white, stepCounterIntersection)
                stepCounterIntersection += 2
    elif direction == 3:#left
        stepCounterIntersection += 1
        if isInt:
            stepCounterIntersection += 1
            if getCur == blue:#blue=intersection tile
                moveRight(currentX, currentY, blockSize, blue)
                moveLeft(currentX, currentY, blockSize, green)#green=used path
                intersection(isInt,False,stepCounterIntersection)
                stepCounterIntersection += 4
            else:
                stepCounterIntersection += 1
                if newscreen.get_at((currentX+blockSize, currentY)) != blue:#right
                    stepCounterIntersection += 2
                    pygame.draw.rect(newscreen, red, pygame.Rect(currentX+blockSize, currentY, blockSize, blockSize))#set red path into intersection
                pygame.draw.rect(newscreen, blue, pygame.Rect(currentX, currentY, blockSize, blockSize))#set current space to blue
                intersectionNum+=1
                intersection(isInt,True,stepCounterIntersection)
                stepCounterIntersection += 3
        else:
            stepCounterIntersection += 1
            if newscreen.get_at((currentX - blockSize, currentY)) == blue:
                moveLeft(currentX, currentY, blockSize, white)
                stepCounterIntersection += 2
            else:
                left(white, stepCounterIntersection)
                stepCounterIntersection += 2
    elif direction == 4:#down
        stepCounterIntersection += 1
        if isInt:
            stepCounterIntersection += 1
            if getCur == blue:#blue=intersection tile
                moveUp(currentX, currentY, blockSize, blue)
                moveDown(currentX, currentY, blockSize, green)#green=used path               
                intersection(isInt,False,stepCounterIntersection)
                stepCounterIntersection += 4
            else:
                stepCounterIntersection += 1
                if newscreen.get_at((currentX, currentY - blockSize)) != blue:#up
                    pygame.draw.rect(newscreen, red, pygame.Rect(currentX, currentY-blockSize, blockSize, blockSize))#set red path into intersection
                pygame.draw.rect(newscreen, blue, pygame.Rect(currentX, currentY, blockSize, blockSize))#set current space to blue
                intersectionNum+=1
                intersection(isInt,True,stepCounterIntersection)
                stepCounterIntersection += 3
        else:
            stepCounterIntersection += 1
            if newscreen.get_at((currentX, currentY + blockSize)) == blue:
                moveDown(currentX, currentY, blockSize, white)
                stepCounterIntersection += 2
            else:
                down(white, stepCounterIntersection)
                stepCounterIntersection += 2
    for event in pygame.event.get():
        # This lets you quit by pressing the X button of the window.
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # 1 = left mouse button, 2 = middle, 3 = right.
                x,y = pygame.mouse.get_pos()
                if 415 <= x <= 532 and 494 <= y <= 532:
                    skipIntersection = True

#print("FRONT PATH CHOSEN",upCount,"TIMES")
#print("LEFT PATH CHOSEN",leftCount,"TIMES")
#print("RIGHT PATH CHOSEN",rightCount,"TIMES")

for z in range(0,intersectionNum):
    pygame.draw.rect(newscreen, (100,100,100), pygame.Rect(intersectionX[z], intersectionY[z], blockSize, blockSize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    stepCounterIntersection += 4

#update memory(pathCount.txt) by adding currentMaze's count(upCount,leftCount,rightCount) to memory count(up,left,right)
f=open('pathCount.txt','w')
count=str(upCount+upMem)+"U"+str(leftCount+leftMem)+"L"+str(rightCount+rightMem)+"R"
f.write(count)
f.close()
stepCounterIntersection += 4

timeIntersection = datetime.now() - start

time.sleep(1)

#================Solution SCREEN==============
background = pygame.image.load('solutionscreen.png').convert()
newscreen = pygame.transform.scale(background, (width, height))
screen.blit(newscreen, (0,0))
pygame.display.update()
time.sleep(2)

#==========================================Solution=====================================
# Initialize
img = Image.open(maze)
change = 3
width = img.width * change
height = img.height * change
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

# Function to move forward
# Function to move forward
def moveUp(x, y, blocksize, newcolor):
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blocksize, blocksize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x, y - blocksize, blocksize, blocksize))
    screen.blit(newscreen, (0,0))
    global currentY
    global currentX
    currentY = y - blocksize
    currentX = x

# Function to move left
def moveDown(x, y, blocksize, newcolor):
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blocksize, blocksize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x, y + blocksize, blocksize, blocksize))
    screen.blit(newscreen, (0,0))
    global currentY
    global currentX    
    currentY = y + blocksize
    currentX = x
    
# Function to move left  
def moveLeft(x, y, blocksize, newcolor):
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blocksize, blocksize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x - blocksize, y, blocksize, blocksize))
    screen.blit(newscreen, (0,0))
    global currentX
    global currentY        
    currentX = x - blocksize
    currentY = y

# Function to move right
def moveRight(x, y, blocksize, newcolor):
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blocksize, blocksize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x + blocksize, y, blocksize, blocksize))
    screen.blit(newscreen, (0,0))
    global currentX
    global currentY        
    currentX = x + blocksize
    currentY = y

#Initialization of currentX and currentY
def varsInit(x, y):
    global currentX
    global currentY
    global direction
    currentX = x
    currentY = y
    direction = 1

#Algorithm to determine direction to move if facing up
def up(replace):
    global direction
    if newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace)
        direction = 2
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace)
        direction = 1
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace)
        direction = 3
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace)
        direction = 4
    else:
        if newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
            moveLeft(currentX, currentY, blockSize, (0,255,255))
            direction = 3
        elif newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
            moveDown(currentX, currentY, blockSize, (0,255,255))
            direction = 4
        elif newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
            moveRight(currentX, currentY, blockSize, (0,255,255))
            direction = 2
        elif newscreen.get_at((currentX, currentY - blockSize)) == blue:#up        
            moveUp(currentX, currentY, blockSize, (0,255,255))
            direction = 1
    
#Algorithm to determine direction to move if facing right
def right(replace):
    global direction
    if newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace)
        direction = 4
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace)
        direction = 2
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace)
        direction = 1
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace)
        direction = 3
    else:
        if newscreen.get_at((currentX, currentY - blockSize)) == blue:#up        
            moveUp(currentX, currentY, blockSize, (0,255,255))
            direction = 1
        elif newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
            moveLeft(currentX, currentY, blockSize, (0,255,255))
            direction = 3
        elif newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
            moveDown(currentX, currentY, blockSize, (0,255,255))
            direction = 4
        elif newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
            moveRight(currentX, currentY, blockSize, (0,255,255))
            direction = 2

#Algorithm to determine direction to move if facing left
def left(replace):
    global direction
    if newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace)
        direction = 1
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace)
        direction = 3
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace)
        direction = 4
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace)
        direction = 2
    else:
        if newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
            moveDown(currentX, currentY, blockSize, (0,255,255))
            direction = 4
        elif newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
            moveRight(currentX, currentY, blockSize, (0,255,255))
            direction = 2
        elif newscreen.get_at((currentX, currentY - blockSize)) == blue:#up        
            moveUp(currentX, currentY, blockSize, (0,255,255))
            direction = 1
        elif newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
            moveLeft(currentX, currentY, blockSize, (0,255,255))
            direction = 3

#Algorithm to determine direction to move if facing down
def down(replace):
    global direction
    if newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace)
        direction = 3
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace)
        direction = 4
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace)
        direction = 2
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace)
        direction = 1
    else:
        if newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
            moveRight(currentX, currentY, blockSize, (0,255,255))
            direction = 2
        elif newscreen.get_at((currentX, currentY - blockSize)) == blue:#up        
            moveUp(currentX, currentY, blockSize, (0,255,255))
            direction = 1
        elif newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
            moveLeft(currentX, currentY, blockSize, (0,255,255))
            direction = 3
        elif newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
            moveDown(currentX, currentY, blockSize, (0,255,255))
            direction = 4

varsInit(xvalueOfStart, yvalueOfStart)

moveUp(currentX, currentY, blockSize, blue)

while 0 != currentY:
    pygame.event.get()
    if direction == 1:#up
        up(blue)
    elif direction == 2:
        right(blue)
    elif direction == 3:
        left(blue)
    elif direction == 4:
        down(blue)

#MazeSolver
direction = 1
currentX = blockSize
currentY = blockSize
whiteListX = []
whiteListY = []
deadEnds = 1

while True:
    pygame.event.get()
    #Define variables
    while currentY <= (height - blockSize):
        getCur = newscreen.get_at((currentX, currentY))
        if getCur == (0,255,255):
            whiteListX.append(currentX)
            whiteListY.append(currentY)
        currentX = currentX + blockSize
        if currentX >= (width - blockSize + 1):
            currentX = 0
            currentY = currentY + blockSize
    whiteListLength = len(whiteListX)
    for x in range (0, whiteListLength):
        pygame.draw.rect(newscreen, white, pygame.Rect(whiteListX[x], whiteListY[x], blockSize, blockSize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    break
pygame.image.save(newscreen,'solution.png')
time.sleep(2)

#Comparing results
array = sorted([timePriorities,timeRightTurn,timeDeadEnd,timeIntersection])
arrayLength = len(array)

steps = sorted([stepCounterPriorities,stepCounterRightTurn,stepCounterDeadEnd,stepCounterIntersection])
stepsLength = len(steps)

#==================================RESULTS=============================
#Results page
background = pygame.image.load('results.png').convert()
newscreen = pygame.transform.scale(background, (width, height))
screen.blit(newscreen, (0,0))
pygame.display.update()

pygame.draw.rect(newscreen, black, pygame.Rect(290, 180, 10, 240))
screen.blit(newscreen, (0,0))
pygame.display.update()

location = 180
tnr = pygame.font.SysFont('Times New Roman', 30)
for i in range(0,arrayLength):
    if timePriorities == array[i] and skipPriorities == False:
        timePriorities = str(timePriorities)
        text1 = tnr.render('Priorities', False, (0, 0, 0))
        text2 = tnr.render(timePriorities, False, (0, 0, 0))
        screen.blit(text1,(60,location))
        screen.blit(text2,(80,location + 30))
        location += 60
    else:
        if timeRightTurn == array[i] and skipRightTurn == False:
            timeRightTurn = str(timeRightTurn)
            text3 = tnr.render('Right Turn', False, (0, 0, 0))
            text4 = tnr.render(timeRightTurn, False, (0, 0, 0))
            screen.blit(text3,(60,location))
            screen.blit(text4,(80,location + 30))
            location += 60
        else:
            if timeDeadEnd == array[i] and skipDeadEnd == False:
                timeDeadEnd = str(timeDeadEnd)
                text5 = tnr.render('Dead End', False, (0, 0, 0))
                text6 = tnr.render(timeDeadEnd, False, (0, 0, 0))
                screen.blit(text5,(60,location))
                screen.blit(text6,(80,location + 30))
                location += 60
            else:
                if timeIntersection == array[i] and skipIntersection == False:
                    timeIntersection = str(timeIntersection)
                    text7 = tnr.render('Intersection', False, (0, 0, 0))
                    text8 = tnr.render(timeIntersection, False, (0, 0, 0))
                    screen.blit(text7,(60,location))
                    screen.blit(text8,(80,location + 30))
                    location += 60

location = 180

for i in range(0,stepsLength):
    if stepCounterPriorities == steps[i] and skipPriorities == False:
        stepsPriorities = str(stepCounterPriorities)
        text9 = tnr.render('Priorities', False, (0, 0, 0))
        text10 = tnr.render(stepsPriorities, False, (0, 0, 0))
        screen.blit(text9,(320,location))
        screen.blit(text10,(340,location + 30))
        location += 60
    else:
        if stepCounterRightTurn == steps[i] and skipRightTurn == False:
            stepsRightTurn = str(stepCounterRightTurn)
            text11 = tnr.render('Right Turn', False, (0, 0, 0))
            text12 = tnr.render(stepsRightTurn, False, (0, 0, 0))
            screen.blit(text11,(320,location))
            screen.blit(text12,(340,location + 30))
            location += 60
        else:
            if stepCounterDeadEnd == steps[i] and skipDeadEnd == False:
                stepsDeadEnd = str(stepCounterDeadEnd)
                text13 = tnr.render('Dead End', False, (0, 0, 0))
                text14 = tnr.render(stepsDeadEnd, False, (0, 0, 0))
                screen.blit(text13,(320,location))
                screen.blit(text14,(340,location + 30))
                location += 60
            else:
                if stepCounterIntersection == steps[i] and skipIntersection == False:
                    stepsIntersection = str(stepCounterIntersection)
                    text15 = tnr.render('Intersection', False, (0, 0, 0))
                    text16 = tnr.render(stepsIntersection, False, (0, 0, 0))
                    screen.blit(text15,(320,location))
                    screen.blit(text16,(340,location + 30))
                    location += 60



pygame.display.update()
while True: 
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        pygame.display.quit()
        pygame.quit()
        sys.exit()