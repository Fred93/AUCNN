from abc import ABCMeta, abstractmethod

class AbstractCrossover():

    __metaclass__ = ABCMeta

    @abstractmethod
    def crossover(self, population):
        pass
