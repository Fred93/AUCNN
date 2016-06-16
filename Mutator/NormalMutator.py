import AbstractMutator
import numpy as np
import random

class NaiveMutator(AbstractMutator.AbstractMutator):

    def __init__(self):
        pass

    def mutate(self, population, mutationRate, mutationRange):
        newPopulation = np.array([])
        for chromosome in population:
            newChromosome = self.mutateChromosome(chromosome, mutationRate=mutationRate, mutationRange=mutationRange)
            newPopulation = np.append(newPopulation, newChromosome)
        return newPopulation

    def mutateChromosome(self, chromosome, mutationRate, mutationRange):
        vec = chromosome.firstLevelMatrix.reshape((1,chromosome.firstLevelMatrix.shape[0]*chromosome.firstLevelMatrix.shape[1]))
        vec = np.apply_along_axis(self.mutateValue, axis=0, arr=vec, mutationRate=mutationRate, mutationRange=mutationRange)
        newMatrix = vec.reshape((chromosome.firstLevelMatrix.shape[0],chromosome.firstLevelMatrix.shape[1]))
        chromosome.firstLevelMatrix = newMatrix

        vec = chromosome.secondLevelMatrix.reshape((1,chromosome.secondLevelMatrix.shape[0]*chromosome.secondLevelMatrix.shape[1]))
        vec = np.apply_along_axis(self.mutateValue, axis=0, arr=vec, mutationRate=mutationRate, mutationRange=mutationRange)
        newMatrix = vec.reshape((chromosome.secondLevelMatrix.shape[0],chromosome.secondLevelMatrix.shape[1]))
        chromosome.secondLevelMatrix = newMatrix

        return chromosome

    def mutateValue(self, value, mutationRate, mutationRange):
        if random.random() < mutationRate:
            return value + random.uniform(mutationRange[0], mutationRange[1])
        else:
            return value
