import random
rand = random.Random()
rand.seed(None)
import numpy as np

a = [5,6,7,8]
b = [9,10,11,12]
c = [13,14,15,16]
d = [17,18,19,20]

e = np.matrix([a,b,c,d])

print(e[0])

