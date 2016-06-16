import random as rand
import numpy as np
import AbstractSelector

class TournamentSelector(AbstractSelector.AbstractSelector):
    """
    This Class implements the deterministic tournament selection , i.e. we 
    set the probability of selecting the best out of k individuals to 1. 
    This is called deterministic tournament selection. We could also set the
    probability different, but this would result in a Roulette Wheel Section
    in each Tournament. 
    """
     
    """
    Additional Input:
    tournament_size - number of solution that compete against each other in each iteration
    """

    def select(self, population, fitness, perform_elitism=False, elitism_rate=0.1, tournmament_size = 2):

         # define population size for the random choice of k elements later
         population_size = len(population)
         # define number of solutions to be selected (differs from population_size if perform_elitism = True)
         num = population_size

         # empty array for index of the selected solution
         new_population_idx = np.array([])
         # if elitism strategy is used call eltitsm() and reduce number of iteration accodingly
         if perform_elitism is True:
             new_population_idx = elitism(population, fitness, elitism_rate) # Bug
             num -= int(len(fitness) * elitism_rate)

         # Select indices of solutions in the population using tournament selection
         for _ in xrange(num):
             # randomly choose k solution
             random_solutions = np.random.randint(population_size, size = tournmament_size )
             # add the best solution of the tournament to new_population
             for i in random_solutions:
                 if fitness[i] == max(fitness[random_solutions]):
                     new_population_idx = np.append(new_population_idx, i)
                     break

         # return selected items from the population
         return population[new_population_idx.astype(int)]