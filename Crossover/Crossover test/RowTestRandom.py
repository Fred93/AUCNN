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

l = []


def exchangerow(l, i, randompoint):

    CrossoverIndices = random.sample(range(0, l[0][0].shape[0]), randompoint)
    print(CrossoverIndices)

    zwischenspeicher = np.matrix(l[i][0][CrossoverIndices, :])
    l[i][0][CrossoverIndices, :] = l[i + 1][0][CrossoverIndices, :]
    l[i + 1][0][CrossoverIndices, :] = zwischenspeicher

    zwischenspeicher = np.matrix(l[i][1][CrossoverIndices, :])
    l[i][1][CrossoverIndices, :] = l[i + 1][1][CrossoverIndices, :]
    l[i + 1][1][CrossoverIndices, :] = zwischenspeicher



i = 0

print(len(l))

while i < (len(l) - 1):  # -1 um bei ungeraden row matrizen die letzte Einheit stehen zu lassen

    randompoint = rand.randint(0, l[i][0].shape[0])
    print(randompoint)

    exchangerow(l, i, randompoint)

    i = i + 2


print(l)


