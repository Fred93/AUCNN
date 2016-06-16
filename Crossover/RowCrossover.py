import random
rand = random.Random()
rand.seed(None)
import AbstractCrossover
import numpy as np


def exchangerow(newPopulation, i, randompoint): #function to crossover rows of chromosomes

    #crossover for first level matrix (input to hidden layer)
    zwischenspeicher = np.matrix(newPopulation[i].firstLevelMatrix[0:randompoint, :])
    newPopulation[i].firstLevelMatrix[0:randompoint, :] = newPopulation[i + 1].firstLevelMatrix[0:randompoint, :] #firstLevelMatrix = [0]
    newPopulation[i + 1].firstLevelMatrix[0:randompoint, :] = zwischenspeicher

    #crossover for second level matrix (hidden to output layer)
    zwischenspeicher = np.matrix(newPopulation[i].secondLevelMatrix[0:randompoint, :])
    newPopulation[i].secondLevelMatrix[0:randompoint, :] = newPopulation[i + 1].secondLevelMatrix[0:randompoint, :] #secondLevelMatrix = [1]
    newPopulation[i + 1].secondLevelMatrix[0:randompoint, :] = zwischenspeicher

    return newPopulation

class ColumCrossover(AbstractCrossover.AbstractCrossover):

    def __init__(self):
        pass

    def crossover(self, newPopulation):

        i = 0

        while i < (len(newPopulation) - 1):  # -1 to take care of the last cromosome of a uneven population

            randompoint = rand.randint(0, newPopulation[i].firstLevelMatrix.shape[0]) #creates for each pair of chromosomes a new random number, also be possible to be 0
            exchangerow(newPopulation, i, randompoint) #calls exchangerow function to crossover the first level matrix and second level matrix of a cromosome pair
            i = i + 2 #jumps to the next pair

        print('Da Rowcroshi isch au durch, gel')  # and is printing an over message
        return newPopulation #after all chromosome pairs are crossovered, the function returns the newPopulation

