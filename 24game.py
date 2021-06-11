import random
import pygame
from pygame.constants import QUIT

def isInt(n):
    return isinstance(n, int)

unselectedColor = (192, 192, 192)
selectedColor = (158, 158, 158)

mousePosX = 0
mousePosY = 0

startNum = []

operator = ' '

while True:
    for i in range(4):
        startNum.append(random.randint(1, 9))

    testData = startNum
    
    random.shuffle(testData)
    cur_opt = random.randint(0, 3)
    if cur_opt == 0:
        ans1 = testData[0]+testData[1]
    elif cur_opt == 1:
        ans1 = testData[0]-testData[1]
    elif cur_opt == 2:
        ans1 = testData[0]*testData[1]
    elif cur_opt == 3:
        ans1 = testData[0]/testData[1]

    print("first Half :" ,ans1)

    cur_opt = random.randint(0,3)
    if cur_opt == 0:
        ans2 = testData[2]+testData[3]
    elif cur_opt == 1:
        ans2 = testData[2]-testData[3]
    elif cur_opt ==2:
        ans2 = testData[2]*testData[3]
    elif cur_opt == 3:
        ans2 = testData[2]/testData[3]
        
    print("Second Half :",ans2)

    cur_opt = random.randint(0,3)
    if cur_opt == 0:
        ans_fin = ans1 + ans2
    elif cur_opt == 1:
        ans_fin = ans1 - ans2
    elif cur_opt ==2:
        ans_fin = ans1 * ans2
    elif cur_opt == 3:
        ans_fin = ans1 / ans2
    
    print("final ans : ",ans_fin)

    if ans_fin >=0 and isInt(ans_fin):
        print("ok")
        break
    else:
        startNum.clear()

pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("24Game kinda")

firstNumBox = pygame.Surface([200,200])
firstNumBox.fill(unselectedColor)

secondNumBox = pygame.Surface([200,200])
secondNumBox.fill(unselectedColor)

thirdNumBox = pygame.Surface([200,200])
thirdNumBox.fill(unselectedColor)

fourthNumBox = pygame.Surface([200,200])
fourthNumBox.fill(unselectedColor)
font = pygame.font.Font('supermarket.ttf',150)
numfont = pygame.font.Font('supermarket.ttf',200)

# HALL OF FAME
'''
num01 = startNum[0]
num02 = startNum[1]
num03 = startNum[2]
num04 = startNum[3]
'''

operatorIcon01 = pygame.Surface((128,128))
operatorIcon01.fill(unselectedColor)

operatorIcon02 = pygame.Surface((128,128))
operatorIcon02.fill(unselectedColor)

operatorIcon03 = pygame.Surface((128,128))
operatorIcon03.fill(unselectedColor)

operatorIcon04 = pygame.Surface((128,128))
operatorIcon04.fill(unselectedColor)

resetIconSurface = pygame.Surface((128,128))
resetIconSurface.fill(unselectedColor)


addIcon = pygame.image.load('add.png')
minusIcon = pygame.image.load('minus.png')
multiplyIcon = pygame.image.load('crossed.png')
divideIcon = pygame.image.load('divide.png')
resetIcon = pygame.image.load('refreshing.png')

questionLength = [0, 247, 231, 200, 155]

def show_Question(qLen):
    question = font.render(str(ans_fin), True, (255, 0, 0))
    screen.blit(question, (questionLength[qLen] + 120, 20))

# HALL OF FAME
'''
def show_question1():
    question = font.render(str(ans_fin),True,(255,0,0))
    screen.blit(question, (247+120,20))
def show_question2():
    question = font.render(str(ans_fin),True,(255,0,0))
    screen.blit(question, (231+120,20))
def show_question3():
    question = font.render(str(ans_fin),True,(255,0,0))
    screen.blit(question, (190+130,20))
def show_question4():
    question = font.render(str(ans_fin),True,(255,0,0))
    screen.blit(question, (155+120,20))
'''

calculatingList = []

def selectNumber():
    global calculatingList
    global operator
    firstNumBox.fill(unselectedColor)
    secondNumBox.fill(unselectedColor)
    thirdNumBox.fill((192 ,192, 192))
    fourthNumBox.fill(unselectedColor)
    idx = 0
    if mousePosX >= 190 and mousePosX <= 390 and mousePosY >= 150 and mousePosY <= 350:
       firstNumBox.fill(selectedColor)
       idx = 0
    elif mousePosX >= 420 and mousePosX <= 620 and mousePosY >= 150 and mousePosY <= 350:
       secondNumBox.fill(selectedColor)
       idx = 1
    elif mousePosX >= 190 and mousePosX <= 390 and mousePosY >= 400 and mousePosY <= 600:
       thirdNumBox.fill(selectedColor)
       idx = 2
    elif mousePosX >= 420 and mousePosX <= 620 and mousePosY >= 400 and mousePosY <= 600:
       fourthNumBox.fill(selectedColor)
       idx = 3
    else:
        return
    if numberInBlock[idx] == ' ':
        return
    if idx in calculatingList:
        return
    if operator != ' ':
        calculatingList.append(idx)
    elif(len(calculatingList) <= 1):
        calculatingList = [idx]

numberInBlock = [str(num) for num in startNum]

def reset():
    global numberInBlock
    print('reset')
    numberInBlock = [str(num) for num in startNum]
    listOfResult.clear()
    operator = ' '
    mousePosX, mousePosY = 0, 0

def changeToNumFont(num):
    return numfont.render(str(num), True, (255, 0, 0))

def selectOperator():
    global operator
    operatorIcon01.fill(unselectedColor)
    operatorIcon02.fill(unselectedColor)
    operatorIcon03.fill(unselectedColor)
    operatorIcon04.fill(unselectedColor)
    if mousePosX >= 70 and mousePosY >= 650 and mousePosX <= 198 and mousePosY <= 778:
        operatorIcon01.fill(selectedColor)
        operator = '+'
        # HALL OF FAME
        # numberInBlock02 = 23

    elif mousePosX >= 248 and mousePosY >= 650 and mousePosX <= 379 and mousePosY <= 778:
        operatorIcon02.fill(selectedColor)
        operator = '-'

    elif mousePosX >= 426 and mousePosY >= 650 and mousePosX <= 554 and mousePosY <= 778:
        operatorIcon03.fill(selectedColor)
        operator = '*'

    elif mousePosX >= 604 and mousePosY >= 650 and mousePosX <= 732 and mousePosY <= 778:
        operatorIcon04.fill(selectedColor)
        operator = '/'

def selectOption():
    global mousePosX, mousePosY
    if mousePosX >= 672 and mousePosY >= 0 and mousePosX <= 800 and mousePosY <= 128:
        resetIconSurface.fill(selectedColor)
        reset()
    mousePosX, mousePosY = 0, 0

def calculate(a, opr, b):
    if opr == '+':
        return a + b
    if opr == '-':
        return a - b
    if opr == '*':
        return a * b
    if opr == '/':
        if b == 0 or a % b != 0:
            return 'INVALID'
        return a / b

def validAnswer(ans):
    return ans == ans_fin

listOfResult = []

running = True

while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePosX, mousePosY = pygame.mouse.get_pos()
            print(mousePosX, mousePosY)
    
    screen.fill((255, 255, 255))
    
    # Question
    show_Question(len(str(ans_fin)))
    #

    # Display
    screen.blit(firstNumBox, (70 + 120, 150))
    screen.blit(secondNumBox, (300 + 120, 150))
    screen.blit(thirdNumBox, (70 + 120, 400))
    screen.blit(fourthNumBox, (300 + 120, 400))
    screen.blit(operatorIcon01, (50 + 20, 650))
    screen.blit(operatorIcon02, (178 + 50 + 20, 650))
    screen.blit(operatorIcon03, (356 + 50 + 20, 650))
    screen.blit(operatorIcon04, (534 + 50 + 20, 650))
    screen.blit(resetIconSurface, (672, 0))
    screen.blit(addIcon, (50 + 20, 650))
    screen.blit(minusIcon, (178 + 50 + 20, 650))
    screen.blit(multiplyIcon, (356 + 50 + 20, 650))
    screen.blit(divideIcon, (534 + 50 + 20, 650))
    screen.blit(resetIcon, (672, 0))
    screen.blit(changeToNumFont(numberInBlock[0]), (70 + 175, 150 + 30))
    screen.blit(changeToNumFont(numberInBlock[1]), (300 + 175, 150 + 30))
    screen.blit(changeToNumFont(numberInBlock[2]), (70 + 175, 400 + 30))
    screen.blit(changeToNumFont(numberInBlock[3]), (300 + 175, 400 + 30))
    #

    # No Action
    if mousePosX == 0 and mousePosY == 0:
        continue
    #

    # Select Option
    selectNumber()
    selectOperator()
    selectOption()
    #

    if len(calculatingList) == 2:
        a = calculatingList[0]
        b = calculatingList[1]
        res = calculate(int(numberInBlock[a]), operator, int(numberInBlock[b]))
        # Clear
        calculatingList.clear()
        operator = ' '
        #
        if res == 'INVALID':
            continue
        # Set Result
        numberInBlock[a] = ' '
        numberInBlock[b] = str(res)
        listOfResult.append(res)
        #
        # Correct Answer
        if len(listOfResult) == 3 and validAnswer(listOfResult[-1]):
            print('Correct')
        #
        mousePosX, mousePosY = 0, 0

    


