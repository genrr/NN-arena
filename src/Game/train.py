import main
from NeatAgent import NeatAgent
import neat
import os
import tqdm
import random
import pickle

# set SDL to use the dummy NULL video driver,
#   so it doesn't need a windowing system.
#os.environ["SDL_VIDEODRIVER"] = "dummy"


def eval_genomes(genomes, config):
    r = main.Game()
    g2 = random.sample(genomes, 20)
    for genome_id, genome in tqdm.tqdm(genomes):
        genome.fitness = 0.0
        for genome_id2, genome2 in g2:
            net = neat.nn.FeedForwardNetwork.create(genome, config)
            net2 = neat.nn.FeedForwardNetwork.create(genome2, config)
            #output = net.activate(xi)
            genome.fitness += r.run(NeatAgent(net), NeatAgent(net2), False)[0]


def run(config_file):
    # Load configuration.
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(
        5, 10, './NeatCheckpoints/neat-checkpoint-'))

    # Run for up to 300 generations.
    winner = p.run(eval_genomes, 50)

    # Display the winning genome.
    print('\nBest genome:\n{!s}'.format(winner))

    # Show output of the most fit genome against training data.
    print('\nOutput:')
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
    pickle.dump(winner_net, open( "./NeatCheckpoints/save.pickle", "wb" ))
    p = neat.Checkpointer.restore_checkpoint(
        './NeatCheckpoints/neat-checkpoint-9')
    p.run(eval_genomes, 10)


if __name__ == '__main__':
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward')
    run(config_path)

# r=main.Game()
# r.run(NeatAgent,main.KeyAgent2)
