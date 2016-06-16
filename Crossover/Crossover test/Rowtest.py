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

l = [e, f, z]


crossoverIndices = random.sample(range(0, len(l)), 2)

print(crossoverIndices)