__author__ = 'D059348'

from abc import ABCMeta, abstractmethod

class AbstractCrossover():

    __metaclass__ = ABCMeta

    @abstractmethod
    def crossover(self, population1, population2):
        pass
