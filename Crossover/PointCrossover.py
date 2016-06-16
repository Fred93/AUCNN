import random
rand = random.Random()
rand.seed(None)
import AbstractCrossover
import numpy as np

def exchangepoint(newPopulation, i, randompoint, nrows, mcolum):

    # have to access data by newPopulation[i].firstLevelMatrix?????

    #crossover for each chromosome pair attributes up to the randompoint of first level matrix
    #reshape into matrix with 1 row
    newPopulation[i].firstLevelMatrix = np.reshape(newPopulation[i].firstLevelMatrix, nrows * mcolum) # [0] = firstLevelMatrix()
    newPopulation[i + 1].firstLevelMatrix = np.reshape(newPopulation[i + 1].firstLevelMatrix, nrows * mcolum)
    #crossover up to the random points of the first level matrix
    zwischenspeicher = np.matrix(newPopulation[i].firstLevelMatrix[:,0:randompoint])
    newPopulation[i].firstLevelMatrix[:, 0:randompoint] = newPopulation[i+1].firstLevelMatrix[:,0:randompoint]
    newPopulation[i+1].firstLevelMatrix[:, 0:randompoint] = zwischenspeicher
    #reshape matrix with 1 row into original shape
    newPopulation[i].firstLevelMatrix=newPopulation[i].firstLevelMatrix.reshape((nrows, mcolum))
    newPopulation[i+1].firstLevelMatrix=newPopulation[i+1].firstLevelMatrix.reshape((nrows, mcolum))

    # crossover for each chromosome pair attributes up to the randompoint of second level matrix
    # reshape into matrix with 1 row

    #[1]
    newPopulation[i].secondLevelMatrix = np.reshape(newPopulation[i].secondLevelMatrix, nrows * mcolum)
    newPopulation[i + 1].secondLevelMatrix = np.reshape(newPopulation[i + 1].secondLevelMatrix, nrows * mcolum)
    # crossover up to the random points of the second level matrix
    zwischenspeicher = np.matrix(newPopulation[i].secondLevelMatrix[:, 0:randompoint])
    newPopulation[i].secondLevelMatrix[:, 0:randompoint] = newPopulation[i + 1].secondLevelMatrix[:, 0:randompoint]
    newPopulation[i + 1].secondLevelMatrix[:, 0:randompoint] = zwischenspeicher
    # reshape matrix with 1 row into original shape
    newPopulation[i].secondLevelMatrix=newPopulation[i].secondLevelMatrix.reshape((nrows, mcolum))
    newPopulation[i+1].secondLevelMatrix=newPopulation[i + 1].secondLevelMatrix.reshape((nrows, mcolum))

    return newPopulation

class PointCrossover(AbstractCrossover.AbstractCrossover):

    def __init__(self):
        pass


    def crossover(self, newPopulation):
        i = 0

        while i < (len(newPopulation) - 1):  # -1 um bei ungeraden row matrizen die letzte Einheit stehen zu lassen

            randompoint = rand.randint(0, newPopulation[i].firstLevelMatrix.shape[0])

            nrows = newPopulation[i].firstLevelMatrix.shape[0] #is to cash the original size of the matrix
            mcolum = newPopulation[i].firstLevelMatrix.shape[1] #is to cash the original size of the matrix

            exchangepoint(newPopulation, i, randompoint, nrows, mcolum)

            i = i + 2

        print('PointCroschover isch over, gel')
        return newPopulation