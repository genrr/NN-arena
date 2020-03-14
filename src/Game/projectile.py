import entity
class Projectile:


    def __init__(self,x,y,ang):
        self.x=x
        self.y=y
        self.ang=ang
    def move(self):
        self.x += 3*math.cos(self.ang)
        self.y += 3*math.sin(self.ang)

    