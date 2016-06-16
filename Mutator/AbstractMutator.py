from abc import ABCMeta, abstractmethod

class AbstractMutator:

    __metaclass__ = ABCMeta

    @abstractmethod
    def mutate(self, population, mutationRate, mutationRange):
        pass