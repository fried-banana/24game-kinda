import random
import pygame
from pygame.constants import QUIT
def ifint(n):
    if isinstance(n,int):
        return True
    else:
        return False

list = []
k=1
while k==1 :
    for i in range(4):
        list.append(random.randint(1, 9))

    number = list
    
    print(number)
    random.shuffle(number)
    print(number)

    opt = ('+','-','*','/')
    cur_opt = random.randint(0, 3)
    if cur_opt == 0:
        ans1 = number[0]+number[1]
    elif cur_opt == 1:
        ans1 = number[0]-number[1]
    elif cur_opt ==2:
        ans1 = number[0]*number[1]
    elif cur_opt == 3:
        ans1 = number[0]/number[1]
    print("first Half :" ,ans1)

    cur_opt = random.randint(0,3)
    if cur_opt == 0:
        ans2 = number[2]+number[3]
    elif cur_opt == 1:
        ans2 = number[2]-number[3]
    elif cur_opt ==2:
        ans2 = number[2]*number[3]
    elif cur_opt == 3:
        ans2 = number[2]/number[3]
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

    if ans_fin >=0 and ifint(ans_fin):
        print("ok")
        break
    else:
        list.clear()


pygame.init()


screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("24Game kinda")

firstnumbox = pygame.Surface([200,200])
firstnumbox.fill((192,192,192))

secondnumbox = pygame.Surface([200,200])
secondnumbox.fill((192,192,192))

thirdnumbox = pygame.Surface([200,200])
thirdnumbox.fill((192,192,192))

fourthnumbox = pygame.Surface([200,200])
fourthnumbox.fill((192,192,192))
font = pygame.font.Font('supermarket.ttf',150)
numfont = pygame.font.Font('supermarket.ttf',200)

num01 = numfont.render(str(list[0]),True,(255,0,0))
num02 = numfont.render(str(list[1]),True,(255,0,0))
num03 = numfont.render(str(list[2]),True,(255,0,0))
num04 = numfont.render(str(list[3]),True,(255,0,0))

operatoricon01 = pygame.Surface((128,128))
operatoricon01.fill((192,192,192))

operatoricon02 = pygame.Surface((128,128))
operatoricon02.fill((192,192,192))

operatoricon03 = pygame.Surface((128,128))
operatoricon03.fill((192,192,192))

operatoricon04 = pygame.Surface((128,128))
operatoricon04.fill((192,192,192))

addicon = pygame.image.load('add.png')
minusicon = pygame.image.load('minus.png')
multiplyicon = pygame.image.load('crossed.png')
divideicon = pygame.image.load('divide.png')




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


mouseposx = 0
mouseposy = 0
selectnumconunt = 0
def selectnum():
    
    if mouseposx >= 190 and mouseposx <=390  and mouseposy >=150 and mouseposy <=350 and selectnumconunt == 0:
       firstnumbox.fill((158, 158, 158))
       secondnumbox.fill((192,192,192))
       thirdnumbox.fill((192,192,192))
       fourthnumbox.fill((192,192,192))
       selectnumconunt = 1
    elif mouseposx >= 420 and mouseposx <=620  and mouseposy >=150 and mouseposy <=350 and selectnumconunt == 0:
       firstnumbox.fill((192,192,192))
       secondnumbox.fill((158, 158, 158))
       thirdnumbox.fill((192,192,192))
       fourthnumbox.fill((192,192,192))  
       selectnumconunt = 1
    elif mouseposx >= 190 and mouseposx <=390  and mouseposy >=400 and mouseposy <=600 and selectnumconunt == 0:
       firstnumbox.fill((192,192,192))
       secondnumbox.fill((192,192,192))
       thirdnumbox.fill((158, 158, 158))
       fourthnumbox.fill((192,192,192))  
       selectnumconunt = 1
    elif mouseposx >= 420 and mouseposx <=620  and mouseposy >=400 and mouseposy <=600 and selectnumconunt == 0:
       firstnumbox.fill((192,192,192))
       secondnumbox.fill((192,192,192))
       thirdnumbox.fill((192,192,192))
       fourthnumbox.fill((158, 158, 158))
       selectnumconunt = 1
    elif mouseposx >= 190 and mouseposx <=390  and mouseposy >=150 and mouseposy <=350 and selectnumconunt == 1:
       firstnumbox.fill((158, 158, 158))
       secondnumbox.fill((192,192,192))
       thirdnumbox.fill((192,192,192))
       fourthnumbox.fill((192,192,192))
       selectnumconunt = 0
    elif mouseposx >= 420 and mouseposx <=620  and mouseposy >=150 and mouseposy <=350 and selectnumconunt == 1:
       firstnumbox.fill((192,192,192))
       secondnumbox.fill((158, 158, 158))
       thirdnumbox.fill((192,192,192))
       fourthnumbox.fill((192,192,192))  
       selectnumconunt = 0
    elif mouseposx >= 190 and mouseposx <=390  and mouseposy >=400 and mouseposy <=600 and selectnumconunt == 1:
       firstnumbox.fill((192,192,192))
       secondnumbox.fill((192,192,192))
       thirdnumbox.fill((158, 158, 158))
       fourthnumbox.fill((192,192,192))  
       selectnumconunt = 0
    elif mouseposx >= 420 and mouseposx <=620  and mouseposy >=400 and mouseposy <=600 and selectnumconunt == 1:
       firstnumbox.fill((192,192,192))
       secondnumbox.fill((192,192,192))
       thirdnumbox.fill((192,192,192))
       fourthnumbox.fill((158, 158, 158))
       selectnumconunt = 0


def selectoperator():
    if mouseposx >=70 and mouseposy >=650 and mouseposx <=198 and mouseposy <=778:
        operatoricon01.fill((158, 158, 158))
        operatoricon02.fill((192,192,192))
        operatoricon03.fill((192,192,192))
        operatoricon04.fill((192,192,192))
    elif mouseposx >=248 and mouseposy >=650 and mouseposx <=379 and mouseposy <=778:
        operatoricon01.fill((192,192,192))
        operatoricon02.fill((158, 158, 158))
        operatoricon03.fill((192,192,192))
        operatoricon04.fill((192,192,192))
    elif mouseposx >=426 and mouseposy >=650 and mouseposx <=554 and mouseposy <=778:
        operatoricon01.fill((192,192,192))
        operatoricon02.fill((192,192,192))
        operatoricon03.fill((158, 158, 158))
        operatoricon04.fill((192,192,192))
    elif mouseposx >=604 and mouseposy >=650 and mouseposx <=732 and mouseposy <=778:
        operatoricon01.fill((192,192,192))
        operatoricon02.fill((192,192,192))
        operatoricon03.fill((192,192,192))
        operatoricon04.fill((158, 158, 158))






running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseposx,  mouseposy = pygame.mouse.get_pos()
            print(mouseposx,mouseposy)            
             

    
    screen.fill((255,255,255))
    if ans_fin < 10:
        show_question1()
    elif ans_fin >=10 and ans_fin < 100:
        show_question2()
    elif ans_fin >999:
        show_question4()
    elif ans_fin >=100:
        show_question3()
    


    screen.blit(firstnumbox,(70+120,150))
    screen.blit(secondnumbox,(300+120,150))
    screen.blit(thirdnumbox,(70+120,400))
    screen.blit(fourthnumbox,(300+120,400))
    screen.blit(operatoricon01,(50+20,650))
    screen.blit(operatoricon02,(178+50+20,650))
    screen.blit(operatoricon03,(356+50+20,650))
    screen.blit(operatoricon04,(534+50+20,650))
    screen.blit(addicon,(50+20,650))
    screen.blit(minusicon,(178+50+20,650))
    screen.blit(multiplyicon,(356+50+20,650))
    screen.blit(divideicon,(534+50+20,650))
    screen.blit(num01,(70+175,150+30))
    screen.blit(num02,(300+175,150+30))
    screen.blit(num03,(70+175,400+30))
    screen.blit(num04,(300+175,400+30))

    selectnum()
    selectoperator()
    

    
    pygame.display.update()

    


