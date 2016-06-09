import random

rand = random.Random()
rand.seed(None)

import numpy as np

a = np.matrix([[1, 2, 3], [4, 5, 6]])
b = np.matrix([[7, 8, 9], [10, 11, 12]])

c = np.matrix([[13,14,15],[16,17,18]])
d = np.matrix([[19,20,21], [22,23,24]])

y = np.matrix([[25,26,27],[28,29,30]])
z = np.matrix([[31,32,33],[34,35,36]])

e = [a, b]
f = [c, d]
x = [y, z]

newPopulation = [e, f, z]


def exchangepoint(newPopulation, i, randompoint, nrows, ncolum):

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

i = 0
while i < (len(newPopulation) - 1):  # -1 um bei ungeraden row matrizen die letzte Einheit stehen zu lassen

    randompoint = rand.randint(0, newPopulation[i][0].shape[0])
    print(randompoint)
    nrows = newPopulation[i][0].shape[0]
    mcolum = newPopulation[i][0].shape[1]
    exchangepoint(newPopulation, i, randompoint,nrows,mcolum)

    i = i + 2


print(newPopulation)



