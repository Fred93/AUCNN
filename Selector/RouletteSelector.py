import random as rand
import numpy as np

import AbstractSelector

class RouletteSelector(AbstractSelector.AbstractSelector):
    selector = Selector.NaiveSelector.NaiveSelector()
    elitism.AbstractSelector.elitism(generation, fitness, elitism_rate)
    """
    This Class implements the Roulette Wheel Selector 
    
    Question: How to call elitsm from the AbstractSelector properly
    """    
    
    def __init__(self):
        pass
    

    def select(self, generation, fitness, perform_elitism = False, elitism_rate = 0.1):
        # compute total fitness
        total_fitness = float(sum(fitness))
        # compute relative fitness value
        rel_fitness = [f/total_fitness for f in fitness]
        # Generate probability intervals for each individual
        probs = [sum(rel_fitness[:i+1]) for i in range(len(rel_fitness))]
    
        # define number of solutions to be selected
        num = len(fitness)
        new_generation = np.array([])
        # if elitism strategy is used call eltitsm() and reduce number of iteration accodingly
        if perform_elitism is True:
            new_generation = AbstractSelector.elitism(generation, fitness, elitism_rate)  # Bug
            num -= int(len(fitness) * elitism_rate)
    
        # Update generation
        for n in xrange(num):
            r = rand.random()
            for (i, individual) in enumerate(generation):
                if r <= probs[i]:
                    new_generation = np.append(new_generation,individual)
                    break
        return new_generation.astype(int)
    
    
    
    
    

