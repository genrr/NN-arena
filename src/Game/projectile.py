import pygame
import math
class Projectile:

    img=pygame.image.load('projectile.png')
    def __init__(self,x,y,angle):
        self.playerX=x
        self.playerY=y
        self.angle=angle
    def move(self):
        self.playerX += 3*math.cos(self.angle)
        self.playerY += 3*math.sin(self.angle)

    def getAction(self,game):
        self.move()
    def getHitBox(self):
        return [(self.playerX , self.playerY), (self.playerX, self.playerY+32), (self.playerX + 32, self.playerY +32), (self.playerX+32, self.playerY)]