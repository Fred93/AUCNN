import random

import AbstractCrossover
import numpy as np


class RowCrossover(AbstractCrossover.AbstractCrossover):

    #ROW_CROSSOVER


    rand = random.Random()
    rand.seed(None)

    def __init__(self):
        pass

    def crossover(self, newPopulation):

        i = 0


        while i < (len(newPopulation) - 1):
            # -1, to take care of the last cromosome of an uneven population

            randompoint = self.rand.randint(0, newPopulation[i].firstLevelMatrix.shape[0])
            #creates for each pair of first level chromosomes a new random number (starting from 0 to number of weights)
            randompointtwo = self.rand.randint(0, newPopulation[i].secondLevelMatrix.shape[0])
            # creates for each pair of second level chromosomes a new random number (starting from 0 to number of weights)

            self.exchangerow(newPopulation, i, randompoint, randompointtwo)
            #calls exchangerow function to crossover the first level matrix and second level matrix of a cromosome pair

            i = i + 2
            #jumps to the next pair

        return newPopulation
        #after all chromosome pairs are crossovered, the function returns the newPopulation


    def exchangerow(self, newPopulation, i, randompoint, randompointtwo):
        #function to crossover rows of chromosomes

        CrossoverIndices = random.sample(range(0, newPopulation[i].firstLevelMatrix.shape[0]), randompoint)
        #random chosen row indicies which will be changed (frist level matrix)
        CrossoverIndicestwo = random.sample(range(0, newPopulation[i].secondLevelMatrix.shape[0]), randompointtwo)
        # random chosen row indicies which will be changed (frist level matrix)

        #crossover for first level matrix (input to hidden layer)
        zwischenspeicher = np.matrix(newPopulation[i].firstLevelMatrix[CrossoverIndices, :])
        #caches the rows of the matrix of chromosome one
        newPopulation[i].firstLevelMatrix[CrossoverIndices, :] = newPopulation[i + 1].firstLevelMatrix[CrossoverIndices, :]
        #choromsome one gets the randomly chosen rows of chromosome two
        newPopulation[i + 1].firstLevelMatrix[CrossoverIndices, :] = zwischenspeicher
        #second chromosome get the cache

        #crossover for second level matrix (hidden to output layer)
        zwischenspeicher2 = np.matrix(newPopulation[i].secondLevelMatrix[CrossoverIndicestwo, :])
        # caches the rows of the matrix of chromosome one
        newPopulation[i].secondLevelMatrix[CrossoverIndicestwo, :] = newPopulation[i + 1].secondLevelMatrix[CrossoverIndicestwo, :] #secondLevelMatrix = [1]
        # choromsome one gets the randomly chosen rows of chromosome two
        newPopulation[i + 1].secondLevelMatrix[CrossoverIndicestwo, :] = zwischenspeicher2
        # second chromosome get the cache

        return newPopulation