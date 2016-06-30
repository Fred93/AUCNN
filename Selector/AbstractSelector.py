from abc import ABCMeta, abstractmethod
import numpy as np

class AbstractSelector():
    __metaclass__ = ABCMeta
 

    """
    select() performs a selection strategy:
    
    Inputs:
    ---------
    population - a numpy array, where population[i] puts out i-th solution
    fitness - a numpy array of all n fitness values for each solution
    perform_elitsm - a boolean indicating wether an elitism strategy is performed     
    elitism_rate - a float between 0 and 1 indicating which fraction of the 
                   solutions shoulb be save
 
    """
    @abstractmethod
    def select(self, population, fitness, perform_elitism = False, elitisim_rate=0.1):
        pass
    
    """
    elitism() function performs standard elitsm strategy and finds the 
    solutions with the 10% highest fitness values.
    
    Inputs: 
    ---------
    same as in select() but without the boolean perform_elitism
    ---------
    Output: an one dimensional np.array containing the indices of the 10% best solution
    """
    
    def elitism(self, population, fitness, elitism_rate=0.1):
        n = int(len(fitness) * elitism_rate)
        return np.argpartition(fitness,-n)[-n:]
