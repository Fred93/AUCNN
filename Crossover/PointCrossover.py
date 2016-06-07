import random as rand
import numpy as np


class AbstractCrossover():

    __metaclass__ = ABCMeta

    @abstractmethod
    def crossover(self, population):
        pass
