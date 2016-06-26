import random

import AbstractCrossover
import numpy as np


class RowCrossover(AbstractCrossover.AbstractCrossover):

    rand = random.Random()
    rand.seed(None)

    def __init__(self):
        pass

    def crossover(self, newPopulation):

        i = 0


        while i < (len(newPopulation) - 1):  # -1 to take care of the last cromosome of a uneven population

            randompoint = self.rand.randint(0, newPopulation[i].firstLevelMatrix.shape[0]) #creates for each pair of chromosomes a new random number, also be possible to be 0
            randompointtwo = self.rand.randint(0, newPopulation[i].secondLevelMatrix.shape[0])

            self.exchangerow(newPopulation, i, randompoint, randompointtwo) #calls exchangerow function to crossover the first level matrix and second level matrix of a cromosome pair
            i = i + 2 #jumps to the next pair

        return newPopulation #after all chromosome pairs are crossovered, the function returns the newPopulation

    def exchangerow(self, newPopulation, i, randompoint, randompointtwo): #function to crossover rows of chromosomes

        CrossoverIndices = random.sample(range(0, newPopulation[i].firstLevelMatrix.shape[0]), randompoint) #sample mit Anzahl, randompoint, von einer randomanzahl an columns
        CrossoverIndicestwo = random.sample(range(0, newPopulation[i].secondLevelMatrix.shape[0]), randompointtwo)

        #crossover for first level matrix (input to hidden layer)
        zwischenspeicher = np.matrix(newPopulation[i].firstLevelMatrix[CrossoverIndices, :])
        newPopulation[i].firstLevelMatrix[CrossoverIndices, :] = newPopulation[i + 1].firstLevelMatrix[CrossoverIndices, :] #firstLevelMatrix = [0]
        newPopulation[i + 1].firstLevelMatrix[CrossoverIndices, :] = zwischenspeicher

        #crossover for second level matrix (hidden to output layer)
        zwischenspeicher2 = np.matrix(newPopulation[i].secondLevelMatrix[CrossoverIndicestwo, :])
        newPopulation[i].secondLevelMatrix[CrossoverIndicestwo, :] = newPopulation[i + 1].secondLevelMatrix[CrossoverIndicestwo, :] #secondLevelMatrix = [1]
        newPopulation[i + 1].secondLevelMatrix[CrossoverIndicestwo, :] = zwischenspeicher2

        return newPopulation