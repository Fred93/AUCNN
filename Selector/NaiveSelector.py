import AbstractSelector

class NaiveSelector(AbstractSelector.AbstractSelector):

    def __init__(self):
        pass

    def select(self, population, fitness, elitism = False, elitisim_rate=0.1):
        return population
