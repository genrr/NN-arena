import NeatAgent
import keyagent
import train
import main
import pickle
import neat
import os
r=main.Game()
local_dir=os.path.dirname(__file__)
config_file= os.path.join(local_dir, 'config-feedforward')
config=neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)
r.run(NeatAgent.NeatAgent(pickle.load(open("./NeatCheckpoints/save.pickle", "rb"))), keyagent.KeyAgent(), True)