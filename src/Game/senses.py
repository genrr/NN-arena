import pygame
import math

# senses, distance calculations




def generateVectors(s, p, length, noOfVectors, fieldOfVision):
    vectors = [None] * noOfVectors
    slope = p.angle - fieldOfVision * (3.0/6.0)


    for j in range(noOfVectors):

        #print(slope)
        vectors[j] = (p.playerX + length*math.cos(slope) + 32, p.playerY + length*math.sin(slope) + 32)       
        pygame.draw.line(s, (255,255,255), (p.playerX+32, p.playerY+32), vectors[j], 1)
        slope += fieldOfVision/noOfVectors
    #print(math.sqrt(((p.playerX +32) - vectors[0][0])**2+((p.playerY +32) - vectors[0][1])**2))    
    
    return vectors






# returns agents minimum distance to borders of the screen

def distToWall(v,p,noOfVectors,width,height):

    #wall detection:

    wallWest = 0
    wallNorth = 0
    wallEast = width - 64
    wallSouth = height - 64

    for j in range(noOfVectors):
            tempX = v[j][0]
            tempY = v[j][1]
            #print(tempX,tempY)

            if (tempX > wallEast or tempY > wallSouth or tempX < wallWest or tempY < wallNorth):
                print("near the edge!")

            #print(min(math.fabs(wallEast - p.PlayerX), math.fabs(wallSouth - p.PlayerY)))

            return min(math.fabs(wallEast - p.playerX), math.fabs(wallWest - p.playerX), math.fabs(wallSouth - p.playerY), math.fabs(wallNorth - p.playerY))
                



def l(a,b,c,d,x):
    xChange = (c-a)
    if(xChange == 0):
        xChange = 1
    return (d-b)/xChange * (x - a) + b
            
            


# returns agents distance to instances in the PlayerList (like other Agent, projectiles, walls..)

def distToPlayer(v, PlayerList, noOfVectors):
    distanceArray = [None] * noOfVectors

    for j in range(noOfVectors):
        tempX = v[j][0]
        tempY = v[j][1]
        #print(tempX,tempY)


        for i in range(len(PlayerList)):
            currentPlayer = PlayerList[0]
            otherPlayer = PlayerList[1]
            hitBoxPoints = otherPlayer.getHitBox()
            a = hitBoxPoints[0]
            b = hitBoxPoints[1]
            c = hitBoxPoints[2]
            d = hitBoxPoints[3]

            minX = min(a[0], b[0], c[0], d[0])
            maxX = max(a[0], b[0], c[0], d[0])
            minY = min(a[1], b[1], c[1], d[1])
            maxY = max(a[1], b[1], c[1], d[1])

            lminX = l(currentPlayer.playerX+32,currentPlayer.playerY+32,tempX,tempY,minX)
            lmaxX = l(currentPlayer.playerX+32,currentPlayer.playerY+32,tempX,tempY,maxX)

            if((lminX >= minY and lminX <= maxY) or (lmaxX >= minY and lmaxX <= maxY)):
                distanceArray[j] = (math.fabs(currentPlayer.playerX - otherPlayer.playerX), math.fabs(currentPlayer.playerY - otherPlayer.playerY))                    
            else:
                distanceArray[j] = (0,0)

            #if (Player.getHitBox().collidepoint(tempX,tempY)):
            #    distX = tempX
            #    distY = tempY
            #    distanceArray[j] = (math.fabs(currentPlayer.playerX - distX), math.fabs(currentPlayer.playerY - distY))
            #else:
            #    distanceArray[j] = (0,0)
                
                
                    
    return distanceArray
            
    

            
            
            
            
            
            

