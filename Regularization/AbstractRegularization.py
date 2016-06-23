from abc import ABCMeta, abstractmethod

class AbstractRegularization:

    __metaclass__ = ABCMeta

    @abstractmethod
    def regularize(self, chromosome):
        pass