import math
import pygame

class Player:


    def __init__(self,agent,startX,startY):
        self.playerX = startX
        self.playerY = startY
        self.angle = -math.pi/2.0
        self.agent=agent

    def move(self):
        self.playerX += 0.6*math.cos(self.angle)
        self.playerY += 0.6*math.sin(self.angle)

    def rotateLeft(self):
        self.angle = (self.angle - 0.01 )%(2*math.pi)# % 2.0 - 1
        #self.playerY -= 0.6*math.cos(self.angle)


    def rotateRight(self):
        self.angle = (self.angle + 0.01 )%(2*math.pi)# % 2.0 - 1
        #print(self.angle)
    
    
    def getAction(self):
        self.agent.getAction(self)

    def getHitBox(self):
        return [(self.playerX , self.playerY), (self.playerX, self.playerY+64), (self.playerX + 64, self.playerY +64), (self.playerX+64, self.playerY)]

