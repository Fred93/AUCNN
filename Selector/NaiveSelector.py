import AbstractSelector

class NaiveSelector(AbstractSelector.AbstractSelector):

    def __init__(self):
        pass

    def select(self, generation, trainingset):
        return generation