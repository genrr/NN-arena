import math
class Player:


    def __init__(self,agent):
        self.playerX = 480
        self.playerY = 460
        self.angle = 1.0
        self.agent=agent

    def move(self):
        self.playerX += 0.1*math.cos(self.angle)
        self.playerY += 0.1*math.sin(self.angle)

    def rotateLeft(self):
        self.angle = (self.angle - 0.01 )%(2*math.pi)# % 2.0 - 1


    def rotateRight(self):
        self.angle = (self.angle + 0.01 )%(2*math.pi)# % 2.0 - 1
        print(self.angle)
    
    
    def getAction(self):
        self.agent.getAction(self)



