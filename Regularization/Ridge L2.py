import random
rand = random.Random()
rand.seed(None)

from sklearn import linear_model
import numpy as np

trainingsdata = np.matrix([[2, 9, 10, 11, 12, 12],[22,8,9,10,11,12]])

targetvalues = np.matrix([[12],[22]])

nnregularization= linear_model.Ridge(alpha=1.0).fit(trainingsdata,targetvalues)

