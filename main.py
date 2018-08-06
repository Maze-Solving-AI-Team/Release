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

skipscreen = pygame.transform.scale(background, (width, height))
skip = pygame.image.load('skip.png')
skipscreen.blit(skip,(0,0))
pygame.display.update()

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
        moveRight(currentX, currentY, blockSize, replace, sleep)
        direction = 2
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace, sleep)
        direction = 1
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace, sleep)
        direction = 3
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace, sleep)
        direction = 4
    else:
        if newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
            moveLeft(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 3
        elif newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
            moveDown(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 4
        elif newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
            moveRight(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 2
        elif newscreen.get_at((currentX, currentY - blockSize)) == blue:#up        
            moveUp(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 1
    
#Algorithm to determine direction to move if facing right
def right(replace):
    global direction
    if newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace, sleep)
        direction = 4
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace, sleep)
        direction = 2
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace, sleep)
        direction = 1
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace, sleep)
        direction = 3
    else:
        if newscreen.get_at((currentX, currentY - blockSize)) == blue:#up        
            moveUp(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 1
        elif newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
            moveLeft(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 3
        elif newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
            moveDown(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 4
        elif newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
            moveRight(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 2

#Algorithm to determine direction to move if facing left
def left(replace):
    global direction
    if newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace, sleep)
        direction = 1
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace, sleep)
        direction = 3
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace, sleep)
        direction = 4
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace, sleep)
        direction = 2
    else:
        if newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
            moveDown(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 4
        elif newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
            moveRight(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 2
        elif newscreen.get_at((currentX, currentY - blockSize)) == blue:#up        
            moveUp(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 1
        elif newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
            moveLeft(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 3

#Algorithm to determine direction to move if facing down
def down(replace):
    global direction
    if newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace, sleep)
        direction = 3
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace, sleep)
        direction = 4
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace, sleep)
        direction = 2
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace, sleep)
        direction = 1
    else:
        if newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
            moveRight(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 2
        elif newscreen.get_at((currentX, currentY - blockSize)) == blue:#up        
            moveUp(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 1
        elif newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
            moveLeft(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 3
        elif newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
            moveDown(currentX, currentY, blockSize, (0,255,255), sleep)
            direction = 4

start = datetime.now()

varsInit(xvalueOfStart, yvalueOfStart)

moveUp(currentX, currentY, blockSize, blue, sleep)

stepCounterPriorities = 0
skipPriorities = False
while 0 != currentY and skipPriorities == False:    
    pygame.event.get()
    if direction == 1:#up
        up(blue)
        stepCounterPriorities += 1
        print("priorities-up",direction)#delete this
    elif direction == 2:
        right(blue)
        stepCounterPriorities += 1
        print("priorities-right",direction)#delete this

    elif direction == 3:
        left(blue)
        stepCounterPriorities += 1
        print("priorities-left",direction)#delete this

    elif direction == 4:
        down(blue)
        stepCounterPriorities += 1
        print("priorities-down",direction)#delete this

    for event in pygame.event.get():
        # This lets you quit by pressing the X button of the window.
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # 1 = left mouse button, 2 = middle, 3 = right.
                x,y = pygame.mouse.get_pos()
                # Skip button
                if 415 <= x <= 532 and 494 <= y <= 532:
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

skipscreen = pygame.transform.scale(background, (width, height))
skip = pygame.image.load('skip.png')
skipscreen.blit(skip,(0,0))
pygame.display.update()

#Colors
color = (0, 188, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 188, 0)

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
def varsInit (x, y):
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
        moveRight(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 2
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 1
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 3
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 4
    
#Algorithm to determine direction to move if facing right
def right(replace):
    global direction
    if newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 4
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 2
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 1
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 3
    
#Algorithm to determine direction to move if facing left
def left(replace):
    global direction
    if newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 1
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 3
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 4
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 2

#Algorithm to determine direction to move if facing down
def down(replace):
    global direction
    if newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 3
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 4
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 2
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace, sleep+0.005)
        direction = 1

start = datetime.now()

varsInit(xvalueOfStart, yvalueOfStart)

moveUp(currentX, currentY, blockSize, white, sleep+0.005)

stepCounterRightTurn = 0

skipRightTurn = False
#original
while 0 != currentY and skipRightTurn == False:
    stepCounterRightTurn += 1
    pygame.event.get()
    if direction == 1:#up
        up(white)
        stepCounterRightTurn += 1
    elif direction == 2:
        right(white)
        stepCounterRightTurn += 1
    elif direction == 3:
        left(white)
        stepCounterRightTurn += 1
    elif direction == 4:
        down(white)
        stepCounterRightTurn += 1
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
'''
skip = pygame.image.load('skip.png')
newscreen.blit(skip,(0,0))
pygame.display.update()
'''
#Colors
color = (0, 188, 0)
white = (255, 255, 255, 255)
black = (0, 0, 0, 255)
blue = (0, 255, 255, 255)
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

start = datetime.now()

varsInit(xvalueOfStart, yvalueOfStart)

direction = 1
currentX = blockSize
currentY = blockSize
whiteListX = []
whiteListY = []
deadEnds = 1

#-------------DEAD END FILLER------------
stepCounterDeadEnd = 0
while deadEnds != 0:
    pygame.event.get()
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
            stepCounterDeadEnd += 1
        if count < 3:
            intersection == 1
    #Break the while loop once all dead ends are filled
    if deadEnds == intersection:
        break

    screen.blit(newscreen, (0,0))
    pygame.display.update()

varsInit(xvalueOfStart, yvalueOfStart)

moveUp(currentX, currentY, blockSize, white, sleep)

skipDeadEnd = False
#Right turn movement through the solution
while 0 != currentY and skipDeadEnd == False:
    pygame.event.get()
    if direction == 1:#up
        up(white)
        stepCounterDeadEnd += 1
    elif direction == 2:
        right(white)
        stepCounterDeadEnd += 1
    elif direction == 3:
        left(white)
        stepCounterDeadEnd += 1
    elif direction == 4:
        down(white)
        stepCounterDeadEnd += 1
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
'''
skip = pygame.image.load('skip.png')
newscreen.blit(skip,(0,0))
pygame.display.update()
'''
sleepTime = sleep
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
    if newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace)
        #-print("up-Move up called")
        time.sleep(sleepTime)
        direction = 1
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace)
        #-print("up-Move right called")
        time.sleep(sleepTime)
        direction = 2
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace)
        #-print("up-Move left called")
        time.sleep(sleepTime)
        direction = 3
        #check for blue paths
    elif newscreen.get_at((currentX,currentY-blockSize))==blue:
        moveUp(currentX, currentY, blockSize, replace)
        #-print("up-Move up blue called")
        time.sleep(sleepTime)
        direction = 1
    elif newscreen.get_at((currentX+blockSize,currentY))==blue:
        #-print("up-Move right blue called")
        time.sleep(sleepTime)
        direction = 2
    elif newscreen.get_at((currentX-blockSize,currentY))==blue:
        moveLeft(currentX, currentY, blockSize, replace)
        #-print("up-Move left blue called")
        time.sleep(sleepTime)
        direction = 3
        #check rear
    elif newscreen.get_at((currentX, currentY + blockSize)) == white or newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
        moveDown(currentX, currentY, blockSize, replace)
        #-print("up-Move down called")
        time.sleep(sleepTime)
        direction = 4
    #-print("direction-up", direction)
    
#Algorithm to determine direction to move if facing right
def right(replace):
    global direction
    if newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace)
        #-print("right-Move right called")
        time.sleep(sleepTime)
        direction = 2
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace)
        #-print("right-Move down called")
        time.sleep(sleepTime)
        direction = 4
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace)
        #-print("right-Move up called")
        time.sleep(sleepTime)
        direction = 1
    #check blue
    elif newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
        moveRight(currentX, currentY, blockSize, replace)
        #-print("right-Move right blue called")
        time.sleep(sleepTime)
        direction = 2
    elif newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
        moveDown(currentX, currentY, blockSize, replace)
        #-print("right-Move down called")
        time.sleep(sleepTime)
        direction = 4
    elif newscreen.get_at((currentX, currentY - blockSize)) == blue:#up        
        moveUp(currentX, currentY, blockSize, replace)
        #-print("right-Move up blue called")
        time.sleep(sleepTime)
        direction = 1
    #check rear
    elif newscreen.get_at((currentX - blockSize, currentY)) == white or newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
        moveLeft(currentX, currentY, blockSize, replace)
        #-print("right-Move left called")
        time.sleep(sleepTime)
        direction = 3
    #-print("direction-right", direction)
    
#Algorithm to determine direction to move if facing left
def left(replace):
    global direction
    if newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace)
        #-print("left-Move left called")
        time.sleep(sleepTime)
        direction = 3
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up
        moveUp(currentX, currentY, blockSize, replace)
        #-print("left-Move up called")
        time.sleep(sleepTime)
        direction = 1
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down        
        moveDown(currentX, currentY, blockSize, replace)
        #-print("left-Move down called")
        time.sleep(sleepTime)
        direction = 4
        #check blue
    elif newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
        moveLeft(currentX, currentY, blockSize, replace)
        #-print("left-Move left blue called")
        time.sleep(sleepTime)
        direction = 3
    elif newscreen.get_at((currentX, currentY - blockSize)) == blue:#up
        moveUp(currentX, currentY, blockSize, replace)
        #-print("left-Move up blue called")
        time.sleep(sleepTime)
        direction = 1
    elif newscreen.get_at((currentX, currentY + blockSize)) == blue:#down        
        moveDown(currentX, currentY, blockSize, replace)
        #-print("left-Move down blue called")
        time.sleep(sleepTime)
        direction = 4
        #check rear
    elif newscreen.get_at((currentX + blockSize, currentY)) == white or newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
        moveRight(currentX, currentY, blockSize, replace)
        #-print("left-Move right called")
        time.sleep(sleepTime)
        direction = 2
    #-print("direction-left", direction)

#Algorithm to determine direction to move if facing down
def down(replace):
    global direction
    if newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace)
        #-print("down-Move down called")
        time.sleep(sleepTime)
        direction = 4
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace)
        #-print("down-Move left called")
        time.sleep(sleepTime)
        direction = 3
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace)
        #-print("down-Move right called")
        time.sleep(sleepTime)
        direction = 2
        #check blue
    elif newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
        moveDown(currentX, currentY, blockSize, replace)
        #-print("down-Move down blue called")
        time.sleep(sleepTime)
        direction = 4
    elif newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
        moveLeft(currentX, currentY, blockSize, replace)
        #-print("down-Move left blue called")
        time.sleep(sleepTime)
        direction = 3
    elif newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
        moveRight(currentX, currentY, blockSize, replace)
        #-print("down-Move right blue called")
        time.sleep(sleepTime)
        direction = 2
        #check rear
    elif newscreen.get_at((currentX, currentY - blockSize)) == white or newscreen.get_at((currentX, currentY - blockSize)) == blue:#up        
        moveUp(currentX, currentY, blockSize, replace)
        #-print("down-Move up called")
        time.sleep(sleepTime)
        direction = 1
    #-print("direction-down", direction)

#returns boolean if current tile is intersection
def isIntersection():
    global direction
    paths = 0 
    #-print("isIntersection")
    if newscreen.get_at((currentX, currentY - blockSize)) == white or newscreen.get_at((currentX, currentY - blockSize)) == red or newscreen.get_at((currentX, currentY - blockSize)) == green or newscreen.get_at((currentX, currentY - blockSize)) == blue:
        paths = paths + 1
        #-print("returnUp")
    if newscreen.get_at((currentX - blockSize, currentY)) == white or newscreen.get_at((currentX - blockSize, currentY)) == red or newscreen.get_at((currentX - blockSize, currentY)) == green or newscreen.get_at((currentX - blockSize, currentY)) == blue:
        paths = paths + 1
        #-print("returnLeft")
    if newscreen.get_at((currentX + blockSize, currentY)) == white or newscreen.get_at((currentX + blockSize, currentY)) == red or newscreen.get_at((currentX + blockSize, currentY)) == green or newscreen.get_at((currentX + blockSize, currentY)) == blue:
        paths = paths + 1
        #-print("returnRight")
    if  newscreen.get_at((currentX, currentY + blockSize)) == white or newscreen.get_at((currentX, currentY + blockSize)) == red or newscreen.get_at((currentX, currentY + blockSize)) == green or newscreen.get_at((currentX, currentY + blockSize)) == blue:
        paths = paths + 1
        #-print("returnDown")
    #-print("direction-isIntersection", direction)
    
    if paths > 2:
        #-print(paths)
        #-print("isIntersection-TRUE")
        return True
    else:
        #-print(paths)
        #-print("isIntersection-FALSE")
        return False

varsInit(xvalueOfStart, yvalueOfStart)

moveUp(currentX, currentY, blockSize, white)

direction = 1

def checkSurround(color):#returns direction or 0 if no color present on intersection paths
    global direction
    paths=0
    x=0
    if newscreen.get_at((currentX, currentY - blockSize)) == color:#up
        #direction = 4
        #-print("checkRed-red up-AI faces down")#debug
        paths+=1
        x=1
    if newscreen.get_at((currentX + blockSize, currentY)) == color:#right
        #direction = 3
        #-print("checkRed-red right-AI faces left")#debug
        paths+=1
        x=2
    if newscreen.get_at((currentX - blockSize, currentY)) == color:#left
        #direction = 2
        #-print("checkRed-red left-AI faces right")#debug
        paths+=1
        x=3
    if newscreen.get_at((currentX,currentY+blockSize))==color:#down
        #direction = 1
        #-print("checkRed-red down-AI faces up")#debug
        paths+=1
        x=4
    if paths>1:
        x=5
    #-print("checkRed-no red present")#debug
    return x
    #-print("direction-checkRed", direction)

def addCount(isInt,directionMove,firstTime):
    global direction,rightCount,upCount,leftCount
    #direction=direction coming into intersection
    #directionMove=direction leaving intersection
    if isInt:
        #-print("addCount-isIntersection-TRUE")#debug
        #-print("addCount-checkRed output",checkSurround(red))
        if checkSurround(red)==4:#AI faces up
            #-print("addCount-AI up")#debug
            if directionMove==1:#up
                upCount+=1
            if directionMove==3:#left
                leftCount+=1
            if directionMove==2:#right
                rightCount+=1
            if direction==4:#AI comes from top
                upCount-=1
            if direction==3:#AI comes from right
                rightCount-=1
            if direction==2:#AI comes from left
                leftCount-=1
        if checkSurround(red)==3:#AI faces right
            #-print("addCount-AI right")#debug
            if directionMove==2:#right
                upCount+=1
            if directionMove==1:#up
                leftCount+=1
            if directionMove==4:#down
                rightCount+=1
            if direction==3:#AI comes from right
                upCount-=1
            if direction==1:#AI comes from bottom
                rightCount-=1
            if direction==4:#AI comes from top
                leftCount-=1
        if checkSurround(red)==2:#AI faces left
            #-print("addCount-AI left")#debug
            if directionMove==3:#left
                upCount+=1
            if directionMove==4:#down
                leftCount+=1
            if directionMove==1:#up
                rightCount+=1
            if direction==2:#AI comes from left
                upCount-=1
            if direction==4:#AI comes from top
                rightCount-=1
            if direction==1:#AI comes from bottom
                leftCount-=1
        if checkSurround(red)==1:#AI faces down
            #-print("addCount-AI down")#debug
            if directionMove==4:#down
                upCount+=1
            if directionMove==2:#right
                leftCount+=1
            if directionMove==3:#left
                rightCount+=1
            if direction==1:#AI comes from bottom
                upCount-=1
            if direction==2:#AI comes from left
                rightCount-=1
            if direction==3:#AI comes from right
                leftCount-=1
        #check blue
        if checkSurround(red)==0:
            if checkSurround(blue)==4:#AI faces up
                #-print("addCount-AI up")#debug
                if directionMove==1:#up
                    upCount+=1
                if directionMove==3:#left
                    leftCount+=1
                if directionMove==2:#right
                    rightCount+=1
                if direction==4:#AI comes from top
                    upCount-=1
                if direction==3:#AI comes from right
                    rightCount-=1
                if direction==2:#AI comes from left
                    leftCount-=1
            if checkSurround(blue)==3:#AI faces right
                #-print("addCount-AI right")#debug
                if directionMove==2:#right
                    upCount+=1
                if directionMove==1:#up
                    leftCount+=1
                if directionMove==4:#down
                    rightCount+=1
                if direction==3:#AI comes from right
                    upCount-=1
                if direction==1:#AI comes from bottom
                    rightCount-=1
                if direction==4:#AI comes from top
                    leftCount-=1
            if checkSurround(blue)==2:#AI faces left
                #-print("addCount-AI left")#debug
                if directionMove==3:#left
                    upCount+=1
                if directionMove==4:#down
                    leftCount+=1
                if directionMove==1:#up
                    rightCount+=1
                if direction==2:#AI comes from left
                    upCount-=1
                if direction==4:#AI comes from top
                    rightCount-=1
                if direction==1:#AI comes from bottom
                    leftCount-=1
            if checkSurround(blue)==1:#AI faces down
                #-print("addCount-AI down")#debug
                if directionMove==4:#down
                    upCount+=1
                if directionMove==2:#right
                    leftCount+=1
                if directionMove==3:#left
                    rightCount+=1
                if direction==1:#AI comes from bottom
                    upCount-=1
                if direction==2:#AI comes from left
                    rightCount-=1
                if direction==3:#AI comes from right
                    leftCount-=1

def turnAround(facing):
    global direction
    if facing==1:
        direction=4
    elif facing==2:
        direction=3
    elif facing==3:
        direction=2
    elif facing==4:
        direction=1
def moveForward(color):
    global direction
    if direction==1:
        moveUp(currentX,currentY,blockSize,color)
    elif direction==2:
        moveRight(currentX,currentY,blockSize,color)
    elif direction==3:
        moveLeft(currentX,currentY,blockSize,color)
    elif direction==4:
        moveDown(currentX,currentY,blockSize,color)

intersectionX=[]
intersectionY=[]
intersectionNum=0
# Check if all paths of an intersection have been travelled. If so, go back on red

stepCounterIntersection = 0

def intersection(isInt,firstTime):
    global direction, upCount, rightCount, leftCount, intersectionX,intersectionY, intersectionNum
    
    if firstTime:#if first time at intersection, then add x/y cordinates of red
        if direction==1:#facing up
            intersectionX.append(currentX)
            intersectionY.append(currentY+blockSize)
        elif direction==2:#facing right
            intersectionX.append(currentX-blockSize)
            intersectionY.append(currentY)
        elif direction==3:#facing left
            intersectionX.append(currentX+blockSize)
            intersectionY.append(currentY)
        elif direction==4:#facing down
            intersectionX.append(currentX)
            intersectionY.append(currentY-blockSize)
    #print("X-",intersectionX)
    #print(" y-",intersectionY)
    #pygame.draw.rect(newscreen, (100,100,100), pygame.Rect(currentX-blockSize, currentY-blockSize, blockSize, blockSize))
    #print("intersectionNum",intersectionNum)
    #-time.sleep(2)#debug-sleep
    
    
    if newscreen.get_at((currentX, currentY - blockSize)) == white:#up
        addCount(isInt,1,firstTime)
        direction = 1
        moveUp(currentX, currentY, blockSize, blue)
        #print("int-move-up")
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        addCount(isInt,2,firstTime)
        direction = 2
        moveRight(currentX, currentY, blockSize, blue)
        #print("int-move-right")
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        addCount(isInt,3,firstTime)
        direction = 3
        moveLeft(currentX, currentY, blockSize, blue)
        #print("int-move-left")
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        addCount(isInt,4,firstTime)
        direction = 4
        moveDown(currentX, currentY, blockSize, blue)
        #print("int-move-down")
    else:
        if checkSurround(red)==5:#more than 1 red path
            #print("more than 1 red path")
            for z in range(0,len(intersectionX)):
                if intersectionX[z]==currentX-blockSize:#left
                    #print("more than 1 red-left")
                    if intersectionY[z]==currentY:
                        if z!=len(intersectionY):#intersections traveled after this one are not completed
                            turnAround(direction)
                            addCount(isInt,direction,firstTime)
                            moveForward(blue)
                            #print("int-to red-left-turn around")
                        else:
                            addCount(isInt,3,firstTime)
                            direction=3
                            moveLeft(currentX,currentY,blockSize,blue)
                            #print("int-to red-left")
                        break
                elif intersectionX[z]==currentX+blockSize:#right
                    #print("more than 1 red-right")
                    if intersectionY[z]==currentY:
                        if z!=len(intersectionY):#intersections traveled after this one are not completed
                            turnAround(direction)
                            addCount(isInt,direction,firstTime)
                            moveForward(blue)
                            #print("int-to red-right-turn around")
                        else:
                            addCount(isInt,2,firstTime)
                            direction=2
                            moveRight(currentX,currentY,blockSize,blue)
                            #print("int-to red-right")
                        break
                elif intersectionY[z]==currentY-blockSize:#up
                    #print("more than 1 red-up")
                    if intersectionX[z]==currentX:
                        #print("intersectionX[z]",intersectionX[z])
                        #print("currentX",currentX)
                        if z!=len(intersectionX):#intersections traveled after this one are not completed
                            #print("z!=last value of intersection[]")
                            turnAround(direction)
                            addCount(isInt, direction,firstTime)
                            moveForward(blue)
                            #print("int-to red-up-turn around")
                        else:
                            addCount(isInt,1,firstTime)
                            direction=1
                            moveUp(currentX,currentY,blockSize,blue)
                            #print("int-to red-up")
                        break
                elif intersectionY[z]==currentY+blockSize:#down
                    #print("more than 1 red-down")
                    if intersectionX[z]==currentX:
                        #print("intersectionX[z]",intersectionX[z])
                        #print("currentX",currentX)
                        if z!=len(intersectionX):#intersections traveled after this one are not completed
                            #print("z!=last value of intersection[]")
                            #print("direction",direction)
                            turnAround(direction)
                            addCount(isInt,direction,firstTime)
                            moveForward(blue)
                            #print("int-to red-down-turn around")
                        else:
                            addCount(isInt,4,firstTime)
                            direction=4
                            moveDown(currentX,currentY,blockSize,blue)
                            #print("int-to red-down")
                        break
            #print("z-",z)
        elif checkSurround(red) == 0:#no red
            if newscreen.get_at((currentX, currentY - blockSize)) == blue:#up
                addCount(isInt,1,firstTime)
                direction = 1
                moveUp(currentX, currentY, blockSize, blue)
                del intersectionX[intersectionNum-1]
                del intersectionY[intersectionNum-1]
                intersectionNum-=1
            elif newscreen.get_at((currentX + blockSize, currentY)) == blue:#right
                addCount(isInt,2,firstTime)
                direction=2
                moveRight(currentX, currentY, blockSize, blue)
                del intersectionX[intersectionNum-1]
                del intersectionY[intersectionNum-1]
                intersectionNum-=1
            elif newscreen.get_at((currentX - blockSize, currentY)) == blue:#left
                addCount(isInt,3,firstTime)
                direction=3
                moveLeft(currentX, currentY, blockSize, blue)
                del intersectionX[intersectionNum-1]
                del intersectionY[intersectionNum-1]
                intersectionNum-=1
            elif newscreen.get_at((currentX, currentY + blockSize)) == blue:#down
                addCount(isInt,4,firstTime)
                direction = 4
                moveDown(currentX, currentY, blockSize, blue)
                del intersectionX[intersectionNum-1]
                del intersectionY[intersectionNum-1]
                intersectionNum-=1
        elif checkSurround(red)==1:#red on top
            addCount(isInt,1,firstTime)
            direction = 1
            moveUp(currentX, currentY, blockSize, blue)
            del intersectionX[intersectionNum-1]
            del intersectionY[intersectionNum-1]
            intersectionNum-=1
        elif checkSurround(red)==2:#red on right
            addCount(isInt,2,firstTime)
            direction = 2
            moveRight(currentX, currentY, blockSize, blue)
            del intersectionX[intersectionNum-1]
            del intersectionY[intersectionNum-1]
            intersectionNum-=1
        elif checkSurround(red)==3:#red on left
            addCount(isInt,3,firstTime)
            direction = 3
            moveLeft(currentX, currentY, blockSize, blue)
            del intersectionX[intersectionNum-1]
            del intersectionY[intersectionNum-1]
            intersectionNum-=1
        elif checkSurround(red)==4:#red on bottom
            addCount(isInt,4,firstTime)
            direction = 4
            moveDown(currentX, currentY, blockSize, blue)
            del intersectionX[intersectionNum-1]
            del intersectionY[intersectionNum-1]
            intersectionNum-=1
            
        '''
        print("intersection-length",len(intersectionX))
        print("intersectionX",intersectionX[intersectionNum-1])
        print("currentX",currentX)
        if intersectionX[intersectionNum-1]>currentX:#left
            addCount(isInt,3,firstTime)
            direction=3
            moveLeft(currentX,currentY,blockSize,blue)
            print("GHASJFHFJWHAUJSHFWAHSDJNWAJSKFJWHANMSDKWASIJD")
            '''
        
        
            
        #-time.sleep(5)#debug-sleep

# ------------- OUR ALGORITHM -------------
start = datetime.now()

skipIntersection = False
while 0 != currentY and skipIntersection==False:
    pygame.event.get()
    getCur = newscreen.get_at((currentX, currentY))
    isInt=isIntersection()
    stepCounterIntersection += 1
    if direction == 1:#up
        if isInt:
            if getCur == blue:#blue=intersection tile
                moveDown(currentX, currentY, blockSize, blue)
                moveUp(currentX, currentY, blockSize, green)#green=used path
                intersection(isInt,False)
            else:
                if newscreen.get_at((currentX, currentY + blockSize)) != blue:#down
                    pygame.draw.rect(newscreen, red, pygame.Rect(currentX, currentY+blockSize, blockSize, blockSize))#set red path into intersection
                pygame.draw.rect(newscreen, blue, pygame.Rect(currentX, currentY, blockSize, blockSize))#set current space to blue
                intersectionNum+=1
                intersection(isInt,True)
        else:
            if newscreen.get_at((currentX, currentY - blockSize)) == blue:
                moveUp(currentX, currentY, blockSize, white)
            else:
                up(white)
    elif direction == 2:#right
        if isInt:
            if getCur == blue:#blue=intersection tile
                moveLeft(currentX, currentY, blockSize, blue)
                moveRight(currentX, currentY, blockSize, green)#green=used path
                intersection(isInt,False)
            else:
                if newscreen.get_at((currentX-blockSize, currentY)) != blue:#left
                    pygame.draw.rect(newscreen, red, pygame.Rect(currentX-blockSize, currentY, blockSize, blockSize))#set red path into intersection
                pygame.draw.rect(newscreen, blue, pygame.Rect(currentX, currentY, blockSize, blockSize))#set current space to blue
                intersectionNum+=1
                intersection(isInt,True)
        else:
            if newscreen.get_at((currentX + blockSize, currentY)) == blue:
                moveRight(currentX, currentY, blockSize, white)
            else:
                right(white)
    elif direction == 3:#left
        if isInt:
            if getCur == blue:#blue=intersection tile
                moveRight(currentX, currentY, blockSize, blue)
                moveLeft(currentX, currentY, blockSize, green)#green=used path
                intersection(isInt,False)
            else:
                if newscreen.get_at((currentX+blockSize, currentY)) != blue:#right
                    pygame.draw.rect(newscreen, red, pygame.Rect(currentX+blockSize, currentY, blockSize, blockSize))#set red path into intersection
                pygame.draw.rect(newscreen, blue, pygame.Rect(currentX, currentY, blockSize, blockSize))#set current space to blue
                intersectionNum+=1
                intersection(isInt,True)
        else:
            if newscreen.get_at((currentX - blockSize, currentY)) == blue:
                moveLeft(currentX, currentY, blockSize, white)
            else:
                left(white)
    elif direction == 4:#down
        if isInt:
            if getCur == blue:#blue=intersection tile
                moveUp(currentX, currentY, blockSize, blue)
                moveDown(currentX, currentY, blockSize, green)#green=used path               
                intersection(isInt,False)
            else:
                if newscreen.get_at((currentX, currentY - blockSize)) != blue:#up
                    pygame.draw.rect(newscreen, red, pygame.Rect(currentX, currentY-blockSize, blockSize, blockSize))#set red path into intersection
                pygame.draw.rect(newscreen, blue, pygame.Rect(currentX, currentY, blockSize, blockSize))#set current space to blue
                intersectionNum+=1
                intersection(isInt,True)
        else:
            if newscreen.get_at((currentX, currentY + blockSize)) == blue:
                moveDown(currentX, currentY, blockSize, white)
            else:
                down(white)
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
    #-print("direction-main", direction)
                '''
    print("front-",upCount)
    print("left-",leftCount)
    print("right-",rightCount)
    print("-------")
    '''

#print("FRONT PATH CHOSEN",upCount,"TIMES")
#print("LEFT PATH CHOSEN",leftCount,"TIMES")
#print("RIGHT PATH CHOSEN",rightCount,"TIMES")

for z in range(0,intersectionNum):
    stepCounterIntersection += 1
    pygame.draw.rect(newscreen, (100,100,100), pygame.Rect(intersectionX[z], intersectionY[z], blockSize, blockSize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    #print("for number",z)

timeIntersection = datetime.now() - start
time.sleep(1)

#================Solution SCREEN==============
background = pygame.image.load('solutionscreen.png').convert()
newscreen = pygame.transform.scale(background, (width, height))
screen.blit(newscreen, (0,0))
pygame.display.update()
time.sleep(2)

#================================================Solution==========================================
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