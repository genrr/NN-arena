import math
import pickle
import random

import gym
import numpy as np
from gym import error, spaces, utils
from gym.utils import seeding
import pygame

import projectile
from NeatAgent import NeatAgent
from keyagent import KeyAgent
from keyagent2 import KeyAgent2
from player import Player


class NNArenaEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    action_space = spaces.Discrete(5)
    observation_space = spaces.Box(-np.inf, np.inf, shape=(5,), dtype=np.float32)

    up, down, left, right, fire = False, False, False, False, False
    w, s, a, d, fire2 = False, False, False, False, False
    entities = []
    vectorLength = 512.0
    vectors = 4
    arenaWidth = 960
    arenaHeight = 720
    fieldOfVision = 1.0

    screen = None

    # Init players
    # p = Player(KeyAgent(),630,480)
    # p2 = Player(KeyAgent2(),270,480)
    playerImg = pygame.transform.scale(pygame.image.load('pilot.png'), (64, 64))
    player2Img = pygame.transform.scale(pygame.image.load('pilot2.png'), (64, 64))

    def loadPlayerImages(self, URL1, URL2):
        self.playerImg = pygame.transform.scale(pygame.image.load(URL1), (64, 64))
        self.player2Img = pygame.transform.scale(pygame.image.load(URL2), (64, 64))

    def createPlayers(self, agent1, agent2):
        self.entities.append(Player(agent1, 630, 480, self.playerImg))
        self.entities.append(Player(agent2, 270, 480, self.player2Img))

    def drawEntity(self, screen, e):
        temp = pygame.transform.rotate(e.img, 360 - e.angle * 180 / math.pi - 90)
        screen.blit(temp, (e.playerX, e.playerY))
        pygame.draw.lines(screen, (255, 255, 255), True, e.getHitBox(), 1)

    def drawBackground(self, screen):
        # screen color
        screen.fill((24, 24, 24))

    def update(self, deltatime):
        for en in self.entities:
            en.getAction(self)

    def draw(self, screen):
        self.drawBackground(screen)
        for en in self.entities:
            self.drawEntity(screen, en)

    def testCollision(self):
        for e in self.entities:
            if (isinstance(e, projectile.Projectile) and (
                    e.playerX > self.arenaWidth or e.playerX < 0 or e.playerY > self.arenaHeight or e.playerY < 0)):
                self.entities.remove(e)
                break
        for e in self.entities:
            for e2 in self.entities:
                if e != e2:
                    r1 = pygame.Rect(
                        e.getHitBox()[0][0], e.getHitBox()[0][1], 64, 64)
                    r2 = pygame.Rect(
                        e2.getHitBox()[0][0], e2.getHitBox()[0][1], 32, 32)
                    if isinstance(e, Player) and isinstance(e2, projectile.Projectile) and (r1.colliderect(r2)):
                        e.setHit()
        if self.entities[0].getHitstate() or self.entities[1].getHitstate():
            return True
        else:
            return False

    def __init__(self):
        self.loadPlayerImages("./res/rockets/rocket 4 blue gray.png", "./res/rockets/rocket 3 light blue orange.png")

    def step(self, action):
        #pygame.time.delay(50)
        self.update(1)
        self.draw(self.screen)
        done = self.testCollision()
        self.score_p1 -= 0.1
        self.score_p2 -= 0.1

        if action == 1:
            self.entities[0].move(self.arenaHeight, self.arenaWidth)
        if action == 2:
            self.entities[0].rotateRight()
        if action == 3:
            self.entities[0].rotateLeft()
        if action == 4:
            self.entities[0].fire(self.entities, self.entities[0].cooldown <= 0)


        if self.score_p1 < 0 or self.score_p2 < 0:
            done = True

        reward = 0

        if done:
            if self.entities[0].getHitstate():
                reward = (0, self.score_p2)
            elif self.entities[1].getHitstate():
                reward = (self.score_p1, 0)
            else:
                reward = (0, 0)
        return "obs", reward, done, {}

    def reset(self):
        pygame.init()

        self.score_p1 = 120
        self.score_p2 = 120

        # create screen
        self.screen = pygame.display.set_mode((self.arenaWidth, self.arenaHeight))

        # Title & icon
        pygame.display.set_caption("nn-arena")

        self.entities = []
        self.createPlayers(KeyAgent(), NeatAgent(pickle.load(open("./NeatCheckpoints/save.pickle", "rb"))))


    def render(self, mode='human'):
        pygame.display.update()

    def close(self):
        pass

env = NNArenaEnv()

for i_episode in range(20):
    done = False
    observation = env.reset()
    t=0
    while not done:
        env.render()
        #print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
        t += 1
env.close()