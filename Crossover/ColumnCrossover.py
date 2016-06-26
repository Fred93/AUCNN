import random
import AbstractCrossover
import numpy as np

class ColumnCrossover(AbstractCrossover.AbstractCrossover):

    rand = random.Random()
    rand.seed(None)

    def __init__(self):
        pass


    def crossover(self, newPopulation):

        i = 0

        while i < (len(newPopulation) - 1):   #-1 to take care of the last cromosome of a uneven population

            randompoint = self.rand.randint(0, newPopulation[i].firstLevelMatrix.shape[1])  # creates for each pair of chromosomes a new random number, also be possible to be 0
            randompointtwo = self.rand.randint(0, newPopulation[i].secondLevelMatrix.shape[1])

            self.exchangecolum(newPopulation, i, randompoint, randompointtwo)  # calls exchangerow function to crossover the first level matrix and second level matrix of a cromosome pair

            i = i + 2  # jumps to the next pair

        return newPopulation  # after all chromosome pairs are crossovered, the function returns the newPopulation


    def exchangecolum(self, newPopulation, i, randompoint, randompointtwo): #function to crossover colums of chromosomes

        CrossoverIndices = random.sample(range(0, newPopulation[i].firstLevelMatrix.shape[1]), randompoint)
        CrossoverIndices2 = random.sample(range(0, newPopulation[i].secondLevelMatrix.shape[1]), randompointtwo)

        #crossover for first level matrix (input to hidden layer)
        zwischenspeicher = np.matrix(newPopulation[i].firstLevelMatrix[:, CrossoverIndices])
        newPopulation[i].firstLevelMatrix[:, CrossoverIndices] = newPopulation[i + 1].firstLevelMatrix[:, CrossoverIndices] #.firstLevelMatrix() = [0]
        newPopulation[i + 1].firstLevelMatrix[:, CrossoverIndices] = zwischenspeicher

        #crossover for second level matrix (hidden to output layer)
        zwischenspeicher2 = np.matrix(newPopulation[i].secondLevelMatrix[:,CrossoverIndices2])
        newPopulation[i].secondLevelMatrix[:, CrossoverIndices2] = newPopulation[i + 1].secondLevelMatrix[:, CrossoverIndices2] #.secondLevelMatix() = [1]
        newPopulation[i + 1].secondLevelMatrix[:, CrossoverIndices2] = zwischenspeicher2

        return newPopulation




