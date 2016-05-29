__author__ = 'D059348'

import AbstractCrossover

class NaiveCrossover(AbstractCrossover.AbstractCrossover):

    def __init__(self):
            pass

    def crossover(self, population1, population2):
        return population1 + population2

