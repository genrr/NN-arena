import math
import pygame
#from main import arenaHeight, arenaWidth

class Player:

    def setImage(self,img):
        self.img=img
    def __init__(self,agent,startX,startY,img):
        self.playerX = startX
        self.playerY = startY
        self.angle = -math.pi/2.0
        self.agent=agent
        self.setImage(img)

    def move(self,arenaHeight,arenaWidth):
        self.playerX += 2.0*math.cos(self.angle)
        self.playerY += 2.0*math.sin(self.angle)
        if self.playerX+64 > arenaWidth:
            self.playerX = arenaWidth-64
        if self.playerX < 0:
            self.playerX = 0
        if self.playerY+64 > arenaHeight:
            self.playerY = arenaHeight-64
        if self.playerY < 0:
            self.playerY = 0

    def rotateLeft(self):
        self.angle = (self.angle - 0.05 )%(2*math.pi)# % 2.0 - 1
        #self.playerY -= 0.6*math.cos(self.angle)


    def rotateRight(self):
        self.angle = (self.angle + 0.05 )%(2*math.pi)# % 2.0 - 1
        #print(self.angle)
    
    
    def getAction(self):
        self.agent.getAction(self,self)

    def getHitBox(self):
        return [(self.playerX , self.playerY), (self.playerX, self.playerY+64), (self.playerX + 64, self.playerY +64), (self.playerX+64, self.playerY)]

