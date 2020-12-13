from baseagent import BaseAgent


class KeyAgent2(BaseAgent):
    def __init__(self):
        pass

    def getAction(self, player, cd, game):
        if game.w:
            player.move(game.arenaHeight, game.arenaWidth)
        if game.d:
            player.rotateRight()
        if game.a:
            player.rotateLeft()
        if game.fire2:
            player.fire(game.entities, cd)