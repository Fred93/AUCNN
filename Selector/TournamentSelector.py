# -*- coding: utf-8 -*-
"""
Created on Sun Jun 05 14:13:47 2016

@author: dkoehn
"""

import random as rand
import numpy as np
import AbstractSelector

class TournamentSelector(AbstractSelector.AbstractSelector):
    selector = Selector.NaiveSelector.NaiveSelector()
    elitism.AbstractSelector.elitism(generation, fitness, elitism_rate)
    """
    This Class implements the deterministic tournament selection , i.e. we 
    set the probability of selecting the best out of k individuals to 1. 
    This is called deterministic tournament selection. We could also set the
    probability different, but this would result in a Roulette Wheel Section
    in each Tournament. 
       
    
    Question: How to call elitsm from the AbstractSelector properly
    """    
    
    def __init__(self):
        pass 
     
     """
     Additional Input:
     tournament_size - number of solution that compete against each other in 
                       each iteration
     """
     def select(self, generation, fitness, perform_elitism=False, elitism_rate=0.1, tournmament_size = 2):
         generation_size = len(generation)
         new_generation = np.array([])

         # define number of solutions to be selected
         num = generation_size
         new_generation = np.array([])
         # if elitism strategy is used call eltitsm() and reduce number of iteration accodingly
         if perform_elitism is True:
             new_generation = AbstractSelector.elitism(generation, fitness, elitism_rate) # Bug
             num -= int(len(fitness) * elitism_rate)

         for _ in xrange(num):
             # randomly choose k solution
             random_solutions = np.random.randint(generation_size, size = tournmament_size )
             # add the best solution of the tournament to new_generation
             for i in generation[random_solutions]:
                 if fitness[i] == max(fitness[random_solutions]):
                     new_generation = np.append(new_generation,generation[i])
                     break
         return new_generation.astype(int)
    























 
 
 