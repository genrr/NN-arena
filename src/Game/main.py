import pygame
from senses import *
from player import *
#import neat
#init pygame
class BaseAgent:
    def __init__(self):
        pass
    def getAction(self, player,cd):
        pass

class NeatAgent:
    def __init__(self, genome, config):

        pass
    def convert(self,p,p2):
        array = []

        for i in range(vectors):
            a = distToPlayer(generateVectors(screen,p,length,vectors,fieldOfVision), [p,p2], vectors)[i]
            length = math.sqrt(a[0]**2+a[1]**2)
            array[i] = length/vectorLength
        a = min(arenaWidth,arenaHeight)
        a = a/2

        array[vectors] = distToWall(generateVectors(screen,p,length,vectors,fieldOfVision), p, vectors,arenaWidth,arenaHeight)/a

    def getAction(self,player,cd,game):
        # predictions= model.predict(convert(player,))
        pass

class KeyAgent(BaseAgent):
    def __init__(self):
        pass
    def getAction(self,player,cd,game):
        if(game.up):
            print("this ran")
            player.move(game.arenaHeight,game.arenaWidth)
        if(game.right):
            player.rotateRight()
        if(game.left):
            player.rotateLeft()
        if(game.fire):
            player.fire(game.entities,cd)

class KeyAgent2(BaseAgent):
    def __init__(self):
        pass
    def getAction(self,player,cd,game):
        if(game.w):
            print("action")
            player.move(game.arenaHeight,game.arenaWidth)
        if(game.d):
            player.rotateRight()
        if(game.a):
            player.rotateLeft()
        if(game.fire2):
            player.fire(game.entities,cd)
class Game:
    up,down,left,right,fire=False,False,False,False,False
    w,s,a,d,fire2=False,False,False,False,False
    entities=[]
    vectorLength = 512.0
    vectors = 4
    arenaWidth = 960
    arenaHeight = 720
    fieldOfVision = 1.0


    # Init players
    #p = Player(KeyAgent(),630,480)
    #p2 = Player(KeyAgent2(),270,480)
    playerImg = pygame.image.load('pilot.png')
    player2Img = pygame.image.load('pilot2.png')

    def createPlayers(self,agent1,agent2):
        self.entities.append(Player(agent1,630,480,self.playerImg))
        self.entities.append(Player(agent2,270,480,self.player2Img))




    def drawEntity(self,screen,e):
        temp = pygame.transform.rotate(e.img,360-e.angle * 180/math.pi-90)
        screen.blit(temp,(e.playerX,e.playerY))
        pygame.draw.lines(screen,(255,255,255),True,e.getHitBox(),1)
        
    def drawBackground(self,screen):
        # screen color
        screen.fill((24,24,24))


    def update(self,deltatime):
        for en in self.entities:
            #print(en)
            en.getAction(self)
    def draw(self,screen):
        self.drawBackground(screen)
        for en in self.entities:
            self.drawEntity(screen,en)
        #drawPlayers(screen)
    # game loop

    def testCollision(self):
        for e in self.entities:
            for e2 in self.entities:
                if(e!=e2):
                    r1 = pygame.Rect(e.getHitBox()[0][0],e.getHitBox()[0][1],64,64)
                    r2 = pygame.Rect(e2.getHitBox()[0][0],e2.getHitBox()[0][1],32,32)             
                    if(isinstance(e,Player) and isinstance(e2, projectile.Projectile) and (r1.colliderect(r2))):
                        e.setHit()
        if(self.entities[0].getHitstate() or self.entities[1].getHitstate()):
            return False
        else:
            return True

                        
    def run(self,agent1,agent2):
        self.createPlayers(agent1,agent2)
        pygame.init()

        score_p1, score_p2 = 120, 120


        #create screen
        screen = pygame.display.set_mode((self.arenaWidth,self.arenaHeight))

        # Title & icon
        pygame.display.set_caption("nn-arena")


        running = True
        fpslimit=True
        time=pygame.time.get_ticks()
        while running:
            
            deltatime=pygame.time.get_ticks()-time
            #movePlayers()
            if(fpslimit):
                if(deltatime>1000/60):
                    self.update(deltatime)
                    self.draw(screen)
                    time=pygame.time.get_ticks()
                    
                    running = self.testCollision()

                    score_p1 -= 0.1
                    score_p2 -= 0.1
                    if(score_p1 < 0 or score_p2 < 0):
                        break

                    
            else:
                self.update(1)
                self.draw(screen)
                running=self.testCollision()
                score_p1 -= 0.1
                score_p2 -= 0.1
                if(score_p1 < 0 or score_p2 < 0):
                    break
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.up=True
                    if event.key == pygame.K_DOWN:
                        self.down=True

                    if event.key == pygame.K_LEFT:
                        self.left=True

                    if event.key == pygame.K_RIGHT:
                        self.right=True


                    if event.key == pygame.K_w:
                        print("w")
                        self.w=True

                    if event.key == pygame.K_a:
                        print("a")
                        self.a=True

                    if event.key == pygame.K_d:
                        self.d=True
                        print(self.d)


                    if event.key == pygame.K_g:
                        print("fire")
                        self.fire=True
                    if event.key == pygame.K_f:
                        print("fire")
                        self.fire2=True


                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.up=False
                    if event.key == pygame.K_DOWN:
                        self.down=False
                    if event.key == pygame.K_LEFT:
                        self.left=False
                    if event.key == pygame.K_RIGHT:
                        self.right=False
                    
                    if event.key == pygame.K_w:
                        print("w released")
                        self.w=False
                    if event.key == pygame.K_a:
                        print("a")
                        self.a=False
                    if event.key == pygame.K_d:
                        print("d")
                        self.d=False

                    if event.key == pygame.K_g:
                        print("fire stopped")
                        self.fire=False
                    if event.key == pygame.K_f:
                        print("fire stopped")
                        self.fire2=False
                    
            length = self.vectorLength

            #print("vectors for agent 1",generateVectors(screen,p,length,vectors,fieldOfVision))
            #print("vectors for agent 2",generateVectors(screen,p2,length,vectors,fieldOfVision))

            
            

            #pygame.time.delay(1000)
            pygame.display.update()
        if self.entities[0].getHitstate():
            temp = (0,score_p2)
        elif self.entities[1].getHitstate():
            temp= (score_p1,0)
        else:
            temp = (0,0)
        self.entities = []
        return temp
r=Game()
r.run(KeyAgent(),KeyAgent2())


