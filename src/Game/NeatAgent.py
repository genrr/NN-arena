import math

import baseagent
from senses import distToPlayer, generateVectors, distToWall


class NeatAgent(baseagent.BaseAgent):
    def __init__(self, network):
        self.model = network
        pass

    def convert(self, p, p2, game):
        array = []

        for i in range(game.vectors):
            a = distToPlayer(generateVectors(
                p, game.vectorLength, game.vectors, game.fieldOfVision), [p, p2], game.vectors)[i]
            length = math.sqrt(a[0]**2+a[1]**2)
            array.append(length/game.vectorLength)
        a = min(game.arenaWidth, game.arenaHeight)
        a = a/2.0

        array.append(distToWall(p, game.arenaWidth, game.arenaHeight)/a)

        return array

    def getAction(self, player, cd, game):
        if game.entities[0] is player:
            opponent = game.entities[1]
        else:
            opponent = game.entities[0]
        predictions = self.model.activate(self.convert(player, opponent, game))

        if predictions[0] > 0.5:
            player.move(game.arenaHeight, game.arenaWidth)
        if predictions[1] > 0.5:
            player.rotateRight()
        if predictions[2] > 0.5:
            player.rotateLeft()
        if predictions[3] > 0.5:
            player.fire(game.entities, cd)