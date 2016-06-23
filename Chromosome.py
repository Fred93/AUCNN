import numpy as np

class Chromosome:

    """
    Notes on hidden units: tuning the benchmark model found that the best model
    had 200 hidden units with a weight decay of 1e-5. 200 was the biggest number tried
    and the optimal number is probably higher. However, if computation seems to be slow
    we could decrease the hidden units as the the benchmark did not seem to be hugly sensitive
    to it (e.g. 200 hidden units gave an of auc = 0.62 and 5 hidden units of auc = 0.60)
    """
    amountInputUnits = None
    amountHiddenUnits = None
    amountOutputUnits = None

    def __init__(self, amountInputUnits, amountHiddenUnits, amountOutputUnits):
        self.amountInputUnits = amountInputUnits
        self.amountHiddenUnits = amountHiddenUnits
        self.amountOutputUnits = amountOutputUnits

    firstLevelMatrix = None
    secondLevelMatrix = None

    def initialize(self):
        # Updated U(-1,1) Matrices
        #self.firstLevelMatrix = np.mat(
        #np.round(2*np.random.random_sample((self.amountInputUnits+1,self.amountHiddenUnits)), 2) - 1
                                            )
                                            
        #self.secondLevelMatrix = np.mat(
        #np.round(1*np.random.random_sample((self.amountHiddenUnits+1,self.amountOutputUnits)), 2) - 0.5
                                             )
        # N(0,10)
        self.firstLevelMatrix = np.mat(
        np.round(2*np.random.normal(loc=0.0, scale=10.0 (self.amountInputUnits+1,
                                                         self.amountHiddenUnits)), 2) - 1
                                            )
                                            
        self.secondLevelMatrix = np.mat(
        np.round(1*np.random.normal(loc=0.0, scale=10.0(self.amountHiddenUnits+1,
                                                        self.amountOutputUnits)), 2) - 0.5
                                             )