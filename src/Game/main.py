import pygame

#init pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((960,720))


# Title & icon
pygame.display.set_caption("nn-arena")


# Player
playerImg = pygame.image.load('pilot.png')
playerX = 480
playerY = 460

def player():
    screen.blit(playerImg,(playerX,playerY))


# game loop
running = True
while running:
    
    # screen color
    screen.fill((24,24,24))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()