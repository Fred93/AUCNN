import random
rand = random.Random()
rand.seed(None)

import numpy as np

a = np.matrix([[1, 2, 3], [4, 5, 6]])
b = np.matrix([[7, 8, 9], [10, 11, 12]])

c = np.matrix([[13,14,15],[16,17,18]])
d = np.matrix([[19,20,21], [22,23,24]])

e = [a,b]
f = [c,d]

newPopulation = [e,f]

nrows = newPopulation[0][0].shape[0] #bekomme die Anzahl an Reihen
mcolum = newPopulation[0][0].shape[1] #bekomme die Anzahl der Columns

a = np.reshape(newPopulation[0][0], nrows * mcolum) #shape es zu einem Vektor
b = np.reshape(newPopulation[1][0], nrows * mcolum) #shape es zu einem Vektor

concrete = np.concatenate ((a,b),axis=1) #Verbinde es zu einem langen Vektor

part = np.reshape(concrete,(concrete.shape[1],1)) #shape den zweiten verktor mit der anzahl an columns in den reihen

regularizationterm = np.power(concrete*part,(1/2)) #ziehe die Wurzel von dem auf summierten Betas

print(regularizationterm)