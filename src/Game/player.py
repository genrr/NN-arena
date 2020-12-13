import math
import pygame
import projectile
#from main import arenaHeight, arenaWidth


class Player:
    gotHit = False
    cooldown = 0
    cooldownMax = 100

    def getHitstate(self):
        return self.gotHit

    def setHit(self):
        self.gotHit = True

    def setImage(self, img):
        self.img = img

    def __init__(self, agent, startX, startY, img):
        self.playerX = startX
        self.playerY = startY
        self.angle = -math.pi/2.0
        self.agent = agent
        self.setImage(img)

    def move(self, arenaHeight, arenaWidth):
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
        self.angle = (self.angle - 0.05) % (2*math.pi)  # % 2.0 - 1
        #self.playerY -= 0.6*math.cos(self.angle)

    def fire(self, ent, canShoot):
        if canShoot:
            ent.append(projectile.Projectile(self.playerX+16+64*math.cos(self.angle),
                                             self.playerY+16+64*math.sin(self.angle), self.angle))
            self.cooldown = self.cooldownMax

    def rotateRight(self):
        self.angle = (self.angle + 0.05) % (2*math.pi)  # % 2.0 - 1
        # print(self.angle)

    def getAction(self, game):
        self.agent.getAction(self, self.cooldown <= 0, game)
        if self.cooldown > 0:
            self.cooldown = self.cooldown-1

    def getHitBox(self):
        return [(self.playerX, self.playerY), (self.playerX, self.playerY+64), (self.playerX + 64, self.playerY + 64), (self.playerX+64, self.playerY)]
