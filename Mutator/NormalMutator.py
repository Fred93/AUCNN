import AbstractMutator
import numpy as np
import random

class NaiveMutator(AbstractMutator.AbstractMutator):

    def __init__(self):
        pass

    def mutate(self, population, mutationRate, mutationRange):
        newPopulation = np.apply_along_axis(self.mutateChromosome, axis=0, arr=np.mat(population), mutationRate=mutationRate, mutationRange=mutationRange)
        return newPopulation[0]

    def mutateChromosome(self, chromosome, mutationRate, mutationRange):

        chromosome = chromosome[0]
        vec = chromosome.firstLevelMatrix.reshape((1,chromosome.firstLevelMatrix.shape[0]*chromosome.firstLevelMatrix.shape[1]))
        mutateInds = np.random.choice(range(vec.shape[1]), int(mutationRate*vec.shape[1]), replace=False)
        vec[:,mutateInds] = np.apply_along_axis(self.mutateValue, axis=0, arr=vec[:,mutateInds], mutationRate=mutationRate, mutationRange=mutationRange)
        newMatrix = vec.reshape((chromosome.firstLevelMatrix.shape[0],chromosome.firstLevelMatrix.shape[1]))
        chromosome.firstLevelMatrix = newMatrix

        vec = chromosome.secondLevelMatrix.reshape((1,chromosome.secondLevelMatrix.shape[0]*chromosome.secondLevelMatrix.shape[1]))
        mutateInds = np.random.choice(range(vec.shape[1]), int(mutationRate*vec.shape[1]), replace=False)
        vec[:,mutateInds] = np.apply_along_axis(self.mutateValue, axis=0, arr=vec[:,mutateInds], mutationRate=mutationRate, mutationRange=mutationRange)
        newMatrix = vec.reshape((chromosome.secondLevelMatrix.shape[0],chromosome.secondLevelMatrix.shape[1]))
        chromosome.secondLevelMatrix = newMatrix

        return np.array([chromosome])

    def mutateValue(self, value, mutationRate, mutationRange):
        return value + random.uniform(mutationRange[0], mutationRange[1])