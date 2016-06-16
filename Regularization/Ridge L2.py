import random

rand = random.Random()
rand.seed(None)

import numpy as np

class RidgeRegulatization():

    def __init__(self):
        pass

    def RidgeReg(self,Chromosome):

        nrows = Chromosome.firstLevelMatrix.shape[0] #bekomme die Anzahl an Reihen
        mcolum = Chromosome.firstLevelMatrix.shape[1] #bekomme die Anzahl der Columns

        firstLevelVektor = np.reshape(Chromosome.firstLevelMatrix, nrows * mcolum) #shape firstLevelMatrix des Chromosomes zu einem Vektor
        secondLevelVektor = np.reshape(Chromosome.secondLevelMatrix, nrows * mcolum) #shape secondLevelMatrix des Chromosomes zu einem Vektor

        vektorone = np.concatenate((firstLevelVektor,secondLevelVektor),axis=1) #Verbinde firstLevelMatrix und secondLevelMatrix zu einem langen Vektor
        vektortwo = np.reshape(concrete,(concrete.shape[1],1)) #shape den zweiten verktor mit der anzahl an columns in den reihen

        regterm = np.power(vektorone*vektortwo,(1/2)) #ziehe die Wurzel von dem auf summierten Betas

        return(regterm)