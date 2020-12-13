from baseagent import BaseAgent


class KeyAgent(BaseAgent):
    def __init__(self):
        pass

    def getAction(self, player, cd, game):
        if game.up:
            player.move(game.arenaHeight, game.arenaWidth)
        if game.right:
            player.rotateRight()
        if game.left:
            player.rotateLeft()
        if game.fire:
            player.fire(game.entities, cd)