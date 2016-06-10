import random
rand = random.Random()
rand.seed(None)
import AbstractCrossover
import numpy as np

def exchangepoint(newPopulation, i, randompoint, nrows, ncolum):

    # have to access data by newPopulation[i].firstLevelMatrix?????

    #crossover for each chromosome pair attributes up to the randompoint of first level matrix
    #reshape into matrix with 1 row
    newPopulation[i][0] = np.reshape(newPopulation[i][0], nrows * mcolum)
    newPopulation[i + 1][0] = np.reshape(newPopulation[i + 1][0], nrows * mcolum)
    #crossover up to the random points of the first level matrix
    zwischenspeicher = np.matrix(newPopulation[i][0][:,0:randompoint])
    newPopulation[i][0][:, 0:randompoint] = newPopulation[i+1][0][:,0:randompoint]
    newPopulation[i+1][0][:, 0:randompoint] = zwischenspeicher
    #reshape matrix with 1 row into original shape
    newPopulation[i][0]=newPopulation[i][0].reshape((nrows, ncolum))
    newPopulation[i+1][0]=newPopulation[i+1][0].reshape((nrows, ncolum))

    # crossover for each chromosome pair attributes up to the randompoint of second level matrix
    # reshape into matrix with 1 row
    newPopulation[i][1] = np.reshape(newPopulation[i][1], nrows * mcolum)
    newPopulation[i + 1][1] = np.reshape(newPopulation[i + 1][1], nrows * mcolum)
    # crossover up to the random points of the second level matrix
    zwischenspeicher = np.matrix(newPopulation[i][1][:, 0:randompoint])
    newPopulation[i][1][:, 0:randompoint] = newPopulation[i + 1][1][:, 0:randompoint]
    newPopulation[i + 1][1][:, 0:randompoint] = zwischenspeicher
    # reshape matrix with 1 row into original shape
    newPopulation[i][1]=newPopulation[i][1].reshape((nrows, ncolum))
    newPopulation[i+1][1]=newPopulation[i + 1][1].reshape((nrows, ncolum))

    return newPopulation

class PointCrossover(AbstractCrossover.AbstractCrossover):

    def __init__(self):
        pass


    def crossover(self, newPopulation):
        i = 0

        while i < (len(newPopulation) - 1):  # -1 um bei ungeraden row matrizen die letzte Einheit stehen zu lassen

            randompoint = rand.randint(0, newPopulation[i][0].shape[0])

            nrows = newPopulation[i][0].shape[0] #is to cash the original size of the matrix
            mcolum = newPopulation[i][0].shape[1] #is to cash the original size of the matrix

            exchangepoint(newPopulation, i, randompoint, nrows, mcolum)

            i = i + 2

        print('PointCroschover isch over, gel')
        return newPopulation