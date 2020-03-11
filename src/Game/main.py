import pygame
from player import *

#init pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((960,720))


# Title & icon
pygame.display.set_caption("nn-arena")

up,down,left,right=False,False,False,False
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
# Player
p = Player(KeyAgent())
playerImg = pygame.image.load('pilot.png')


def drawPlayer():
    temp=pygame.transform.rotate(playerImg,360-p.angle * 180/math.pi-90)
    
    screen.blit(temp,(p.playerX,p.playerY))



    
def drawBackground():
    # screen color
    screen.fill((24,24,24))



# game loop
running = True
while running:
    
    drawBackground()
    drawPlayer()
    p.getAction()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("keydown")
                up=True
            if event.key == pygame.K_DOWN:
                print("keydown")
                down=True
            if event.key == pygame.K_LEFT:
                print("keydown")
                left=True
            if event.key == pygame.K_RIGHT:
                print("keydown")
                right=True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                print("keydown")
                up=False
            if event.key == pygame.K_DOWN:
                print("keydown")
                down=False
            if event.key == pygame.K_LEFT:
                print("keydown")
                left=False
            if event.key == pygame.K_RIGHT:
                print("keydown")
                right=False
            



    pygame.display.update()