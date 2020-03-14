import pygame
from senses import *
from player import *

#init pygame
pygame.init()


vectorLength = 512.0
vectors = 4
arenaWidth = 960
arenaHeight = 720
fieldOfVision = 1.0


#create screen
screen = pygame.display.set_mode((arenaWidth,arenaHeight))

# Title & icon
pygame.display.set_caption("nn-arena")


up,down,left,right,fire=False,False,False,False,False
w,s,a,d,fire2=False,False,False,False,False
b = True

class BaseAgent:
    def __init__(self):
        pass
    def getAction(self):
        pass
class KeyAgent(BaseAgent):
    def __init__(self):
        pass
    def getAction(self,player):
        if(up):
            player.move()
        if(right):
            player.rotateRight()
        if(left):
            player.rotateLeft()

class KeyAgent2(BaseAgent):
    def __init__(self):
        pass
    def getAction(self,player):
        if(w):
            player.move()
        if(d):
            player.rotateRight()
        if(a):
            player.rotateLeft()

# Init players
p = Player(KeyAgent(),630,480)
p2 = Player(KeyAgent2(),270,480)
playerImg = pygame.image.load('pilot.png')
player2Img = pygame.image.load('pilot2.png')


def drawPlayers():
    temp = pygame.transform.rotate(playerImg,360-p.angle * 180/math.pi-90)
    temp2 = pygame.transform.rotate(player2Img,360-p2.angle * 180/math.pi-90)
    screen.blit(temp,(p.playerX,p.playerY))
    screen.blit(temp2,(p2.playerX,p2.playerY))

    hitBoxPoints = p.getHitBox()
    degrees = 360-p.angle * 180/math.pi-90

    pygame.draw.lines(screen,(255,255,255),True,p.getHitBox(),1)
    pygame.draw.lines(screen,(255,255,255),True,p2.getHitBox(),1)



    
def drawBackground():
    # screen color
    screen.fill((24,24,24))


def update(deltatime):
    p.getAction()
    p2.getAction()
def draw():
    drawBackground()
    drawPlayers()
# game loop
running = True
fpslimit=True
time=pygame.time.get_ticks()
while running:
    
    deltatime=pygame.time.get_ticks()-time
    #movePlayers()
    if(fpslimit):
        if(deltatime>1000/60):
            update(deltatime)
            draw()
            time=pygame.time.get_ticks()
    else:
        update(1)
        drawPlayers()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up=True
            if event.key == pygame.K_DOWN:
                down=True

            if event.key == pygame.K_LEFT:
                left=True

            if event.key == pygame.K_RIGHT:
                right=True


            if event.key == pygame.K_w:
                print("w")
                w=True

            if event.key == pygame.K_a:
                print("a")
                a=True

            if event.key == pygame.K_d:
                print("d")
                d=True


            if event.key == pygame.K_g:
                print("fire")
                fire=True
            if event.key == pygame.K_f:
                print("fire")
                fire2=True


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up=False
            if event.key == pygame.K_DOWN:
                down=False
            if event.key == pygame.K_LEFT:
                left=False
            if event.key == pygame.K_RIGHT:
                right=False
            
            if event.key == pygame.K_w:
                print("w released")
                w=False
            if event.key == pygame.K_a:
                print("a")
                a=False
            if event.key == pygame.K_d:
                print("d")
                d=False

            if event.key == pygame.K_g:
                print("fire stopped")
                fire=False
            if event.key == pygame.K_f:
                print("fire stopped")
                fire2=False
            
    length = vectorLength

    #print("vectors for agent 1",generateVectors(screen,p,length,vectors,fieldOfVision))
    #print("vectors for agent 2",generateVectors(screen,p2,length,vectors,fieldOfVision))
    #print(distToWall(generateVectors(screen,p,length,vectors,fieldOfVision), p, vectors))
    print(distToPlayer(generateVectors(screen,p,length,vectors,fieldOfVision), [p,p2], vectors))
    print(distToPlayer(generateVectors(screen,p2,length,vectors,fieldOfVision), [p2,p], vectors))

    #pygame.time.delay(1000)
    pygame.display.update()