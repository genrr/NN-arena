import pygame
from senses import *
from player import *
import neat
#init pygame

up,down,left,right,fire=False,False,False,False,False
w,s,a,d,fire2=False,False,False,False,False
entities=[]
class BaseAgent:
    def __init__(self):
        pass
    def getAction(self, player):
        pass
class NeatAgent:
    def __init__(self, genome, config):

        pass
    def convert(self,p,p2,vectors,vectorLength):
        array = []

        for i in range(vectors):
            a = distToPlayer(generateVectors(screen,p,length,vectors,fieldOfVision), [p,p2], vectors)[i]
            length = math.sqrt(a[0]**2+a[1]**2)
            array[i] = length/vectorLength
        array[vectors] = distToWall(generateVectors(screen,p,length,vectors,fieldOfVision), p, vectors)

    def getAction(self,player):
       # predictions= model.predict(convert(player,))
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
            print("action")
            player.move()
        if(d):
            player.rotateRight()
        if(a):
            player.rotateLeft()

# Init players
#p = Player(KeyAgent(),630,480)
#p2 = Player(KeyAgent2(),270,480)
playerImg = pygame.image.load('pilot.png')
player2Img = pygame.image.load('pilot2.png')

def createPlayers(agent1,agent2):
    entities.append(Player(agent1,630,480,playerImg))
    entities.append(Player(agent2,270,480,player2Img))




def drawEntity(screen,e):
    temp = pygame.transform.rotate(playerImg,360-e.angle * 180/math.pi-90)
    screen.blit(temp,(e.playerX,e.playerY))
    pygame.draw.lines(screen,(255,255,255),True,e.getHitBox(),1)
    
def drawBackground(screen):
    # screen color
    screen.fill((24,24,24))


def update(deltatime):
    for en in entities:
        en.getAction()
def draw(screen):
    drawBackground(screen)
    for en in entities:
        en.getAction()
        drawEntity(screen,en)
    #drawPlayers(screen)
# game loop
def run(agent1,agent2):
    createPlayers(agent1,agent2)
    global w,a,d,up,left,right,fire,fire2
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



    b = True
    running = True
    fpslimit=True
    time=pygame.time.get_ticks()
    while running:
        
        deltatime=pygame.time.get_ticks()-time
        #movePlayers()
        if(fpslimit):
            if(deltatime>1000/60):
                update(deltatime)
                draw(screen)
                time=pygame.time.get_ticks()
        else:
            update(1)
            draw(screen)

        
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

        
        

        #pygame.time.delay(1000)
        pygame.display.update()
run(KeyAgent,KeyAgent2)


