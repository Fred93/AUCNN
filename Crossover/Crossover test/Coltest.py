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

newPopulation = [e, f, x]



def exchangecolum(newPopulation, i, randompoint):  # function to crossover colums of chromosomes

    CrossoverIndices = random.sample(range(0, newPopulation[i][0].shape[1]), randompoint)
    print(CrossoverIndices)
    # crossover for first level matrix (input to hidden layer)
    zwischenspeicher = np.matrix(newPopulation[i][0][:, CrossoverIndices])
    newPopulation[i][0][:, CrossoverIndices] = newPopulation[i + 1][0][:,CrossoverIndices]  # .firstLevelMatrix() = [0]
    newPopulation[i + 1][0][:, CrossoverIndices] = zwischenspeicher

    # crossover for second level matrix (hidden to output layer)
    zwischenspeicher = np.matrix(newPopulation[i][1][:, CrossoverIndices])
    newPopulation[i][1][:, CrossoverIndices] = newPopulation[i + 1][1][:,CrossoverIndices]  # .secondLevelMatix() = [1]
    newPopulation[i + 1][1][:, CrossoverIndices] = zwischenspeicher

    return newPopulation

i = 0

while i < (len(newPopulation) - 1):  # -1 to take care of the last cromosome of a uneven population

    randompoint = rand.randint(0, newPopulation[i][0].shape[1])  # creates for each pair of chromosomes a new random number, also be possible to be 0
    print(randompoint)
    exchangecolum(newPopulation, i,randompoint)  # calls exchangerow function to crossover the first level matrix and second level matrix of a cromosome pair
    i = i + 2  # jumps to the next pair

print (newPopulation)
