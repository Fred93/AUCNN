import AbstractSelector

class NaiveSelector(AbstractSelector.AbstractSelector):

    def __init__(self):
        pass

<<<<<<< HEAD
    def select(self, generation, fitness, elitism = False, elitisim_rate=0.1):
        return generation
=======
    def select(self, population, trainingset):
        return population
>>>>>>> 2f0df9248763f9faaaf0a5f1e8f49bab2a3658a0
