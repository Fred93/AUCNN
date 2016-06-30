from abc import ABCMeta, abstractmethod

class AbstractMutator:
    '''
    Abstract class. Defines the interface of mutators in order to enable strategy pattern.
    '''

    __metaclass__ = ABCMeta

    @abstractmethod
    def mutate(self, population, mutationRate, mutationRange):
        '''
        Defines interface of mutate-function.
        '''
        pass