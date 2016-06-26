import random as rand
import numpy as np

import AbstractSelector

class RouletteSelector(AbstractSelector.AbstractSelector):
    """
    This Class implements the Roulette Wheel Selector 
    """    
    
    def __init__(self):
        pass
    

    def select(self, population, fitness, perform_elitism = False, elitism_rate = 0.1):
        theta = 0.01
        # compute total fitness
        total_fitness = float(sum(fitness))
        # compute relative fitness value
        rel_fitness = [(f+theta)/(total_fitness+theta*len(fitness)) for f in fitness]
        #rel_fitness = [(f)/(total_fitness) for f in fitness]
        # Generate probability intervals for each individual
        probs = [sum(rel_fitness[:i+1]) for i in range(len(rel_fitness))]
    
        # define number of solutions to be selected
        num = len(fitness)
        # empty array for index of the selected solution
        new_population_idx = np.array([])
        # if elitism strategy is used call eltitsm() and reduce number of iteration accodingly
        if perform_elitism is True:
            new_population_idx = self.elitism(population, fitness, elitism_rate)
            num -= int(len(fitness) * elitism_rate)
    
        # Select indices of solution in the population using roulette wheel selection
        for n in xrange(num):
            r = rand.random()
            for (i, individual) in enumerate(population):
                if r <= probs[i]:
                    new_population_idx = np.append(new_population_idx,i)
                    break
                
        # return selected items from the population
        return population[new_population_idx.astype(int)]