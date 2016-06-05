from abc import ABCMeta, abstractmethod
import numpy as np

"""
Should the fitness values get computed here or in some other class?
"""


class AbstractSelector():
    __metaclass__ = ABCMeta
 

    """
    select() performs a selection strategy:
    
    Inputs:
    ---------
    generation - a numpy array, where generation[i] puts out i-th solution
    fitness - a numpy array of all n fitness values for each solution
    elitsm - a boolean indicating wether an elitism strategy is performed     
    elitism_rate - a float between 0 and 1 indicating which fraction of the 
                   solutions shoulb be save
 
    """
    @abstractmethod
    def select(self, generation, fitness, elitism = False, elitisim_rate=0.1):
        pass
    
    """
    elitism() function performs standard elitsm strategy and finds the 
    solutions with the 10% highest fitness values.
    
    Inputs: 
    ---------
    same as in select but without the boolean elitism
    ---------
    Output: an one dimensional np.array containing the 10% best solution
    """
    
    def elitism(self, generation, fitness, eltism_rate=0.1):
        n = int(len(fitness) * eltism_rate)
        nlargest_idx = np.argpartition(fitness,-n)[-n:]
        return generation[nlargest_idx]

        
        
=======
    def select(self, population, trainingset):
        pass
>>>>>>> 2f0df9248763f9faaaf0a5f1e8f49bab2a3658a0
