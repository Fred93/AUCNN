import numpy as np

class Chromosome:

    #TODO: use correct numbers
    amountInputUnits = None
    amountHiddenUnits = None
    amountOutputUnits = None

    def __init__(self, amountInputUnits, amountHiddenUnits, amountOutputUnits):
        self.amountInputUnits = amountInputUnits
        self.amountHiddenUnits = amountHiddenUnits
        self.amountOutputUnits = amountOutputUnits

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
        
