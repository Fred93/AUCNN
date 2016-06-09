import random

rand = random.Random()
rand.seed(None)

import numpy as np

a = np.matrix([[1, 2, 3], [4, 5, 6]])
b = np.matrix([[7, 8, 9], [10, 11, 12]])
c = np.matrix([[13,14,15],[16,17,18]])
e = [a, b, c]

# print(e[0][:,0]) #gib mir die 0te column
# print(e[0][:,1:2]) # gib mir die 1ste column

# print(e[0].shape[1])# gibt mir die Anzahl der Columns wieder von a


i = 0

while i < (e[0].shape[0] - 1):  # -1 um bei ungeraden row matrizen die letzte Einheit stehen zu lassen

    randompoint = rand.randint(0, e[i].shape[0])
    print(randompoint)

    zwischenspeicher = np.matrix(e[i][0:randompoint,:])
    e[i][0:randompoint,:] = e[i + 1][0:randompoint,:]
    e[i + 1][0:randompoint,:] = zwischenspeicher

    i = i + 2

print(e[0])
print(e[1])
print(e[2])