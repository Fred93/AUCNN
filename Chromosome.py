import numpy as np

class Chromosome:

    
    """
    Notes on hidden units: tuning the benchmark model found that the best model 
    had 200 hidden units with a weight decay of 1e-5. 200 was the biggest number tried
    and the optimal number is probably higher. However, if computation seems to be slow
    we could decrease the hidden units as the the benchmark did not seem to be hugly sensitive
    to it (e.g. 200 hidden units gave an of auc = 0.62 and 5 hidden units of auc = 0.60)
    """
    amountInputUnits = 3
    amountHiddenUnits = 200 # updated (weight decay should be 1e-5, updated in TargetFunction as default)
    amountOutputUnits = 1

    def __init__(self, amountHiddenUnits):
        self.amountHiddenUnits = amountHiddenUnits

    firstLevelMatrix = None
    secondLevelMatrix = None

    #take care of bias units!!!
    def initialize(self):
        # Updated U(0,1) Matrices
        self.firstLevelMatrix = np.mat(
        np.round(1*np.random.random_sample((self.amountInputUnits+1,self.amountHiddenUnits)),2)
                                            )
                                            
        self.secondLevelMatrix = np.mat(
        np.round(1*np.random.random_sample((self.amountHiddenUnits+1,self.amountOutputUnits)),2)
                                             )
        
