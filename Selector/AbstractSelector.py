from abc import ABCMeta, abstractmethod

class AbstractSelector():
    __metaclass__ = ABCMeta

    @abstractmethod
    def select(self, population, trainingset):
        pass