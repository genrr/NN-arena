import pygame
import math

# senses, distance calculations


def generateVectors(p, length, noOfVectors, fieldOfVision):
    vectors = [None] * noOfVectors
    halfOfVision = 1.0 * fieldOfVision * (noOfVectors + 14)/50.0
    slope = p.angle - halfOfVision
    
    r = halfOfVision*2.0

    if(noOfVectors > 1):
        slopeChange = r/(noOfVectors- 1)
    elif(noOfVectors == 1):
        vectors[0] = (p.playerX + length*math.cos(p.angle) + 32, p.playerY + length*math.sin(p.angle) + 32)
        return vectors
    else:
        print("Invalid number of vectors!")
        return None

    for j in range(noOfVectors):
        # print(slope)
        vectors[j] = (p.playerX + length*math.cos(slope) + 32, p.playerY + length*math.sin(slope) + 32)
        #pygame.draw.line(s, (255,255,255), (p.playerX+32, p.playerY+32), vectors[j], 1)
        slope += slopeChange


    return vectors


# returns agents minimum distance to borders of the screen

def distToWall(p, width, height):

    wallWest = 0
    wallNorth = 0
    wallEast = width - 64
    wallSouth = height - 64

    return min(math.fabs(wallEast - p.playerX), math.fabs(wallWest - p.playerX), math.fabs(wallSouth - p.playerY), math.fabs(wallNorth - p.playerY))


def l(x1, y1, x2, y2, x):
    xChange = (x2 - x1)
    if(xChange == 0):
        xChange = 1
    return (y2-y1)/xChange * (x - x1) + y1




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

            pX = currentPlayer.playerX+32
            pY = currentPlayer.playerY+32

            # check if hitbox Rect collides with another Rect, which has the vector as its diagonal
            if(pygame.Rect(min(pX,tempX),min(pY,tempY),abs(pX-tempX),abs(pY-tempY)).colliderect(minX,minY,abs(minX-maxX),abs(minY-maxY))):
                # compute a line through (pX,pY) & (tempX,tempY) at minimum and maximum x of hitbox
                lminX = l(pX, pY, tempX, tempY, minX)
                lmaxX = l(pX, pY, tempX, tempY, maxX)

                # test if line collides with hitbox: if line has values in between minY and maxY at minimum x or maximum x of hitbox
                # or has smaller value than minY at minimum x and larger than maxY at maximum x(and vice versa), the line has to intersect the hitbox
                if((lminX >= minY and lminX <= maxY) or (lmaxX >= minY and lmaxX <= maxY) or (lminX <= minY and lmaxX >= maxY) or (lminX >= maxY and lmaxX <= minY)):
                    distanceArray[j] = (math.fabs(currentPlayer.playerX - otherPlayer.playerX), math.fabs(currentPlayer.playerY - otherPlayer.playerY))
                else:
                    distanceArray[j] = (0,0)
            else:
                distanceArray[j] = (0,0)

    return distanceArray
