import random
import AbstractRegularization

rand = random.Random()
rand.seed(None)

import numpy as np

class RidgeL2(AbstractRegularization.AbstractRegularization):

    def __init__(self):
        pass

    def regularize(self,chromosome):

        nrows = chromosome.firstLevelMatrix.shape[0] #bekomme die Anzahl an Reihen
        mcolum = chromosome.firstLevelMatrix.shape[1] #bekomme die Anzahl der Columns

        firstLevelVektor = np.reshape(chromosome.firstLevelMatrix, (1,nrows * mcolum)) #shape firstLevelMatrix des Chromosomes zu einem Vektor

        nrows = chromosome.secondLevelMatrix.shape[0] #bekomme die Anzahl an Reihen
        mcolum = chromosome.secondLevelMatrix.shape[1] #bekomme die Anzahl der Columns
        secondLevelVektor = np.reshape(chromosome.secondLevelMatrix, (1,nrows * mcolum)) #shape secondLevelMatrix des Chromosomes zu einem Vektor

        vektorone = np.concatenate((firstLevelVektor,secondLevelVektor),axis=1) #Verbinde firstLevelMatrix und secondLevelMatrix zu einem langen Vektor


        #vektortwo = np.reshape(vektorone,(vektorone.shape[1],1)) #shape den zweiten verktor mit der anzahl an columns in den reihen
        vektortwo = np.transpose(vektorone)
        squaredSum = (np.mat(vektorone) * np.mat(vektortwo)).item()
        regterm = np.sqrt(squaredSum) #ziehe die Wurzel von dem auf summierten Betas

        return(regterm)