import numpy as np
import pandas as pd

class Population:

    #TODO: use correct numbers
    amountInputUnits = 20
    amountHiddenUnits = 30
    amountOutputUnits = 2

    firstLevelMatrix = pd.DataFrame()
    secondLevelMatrix = pd.DataFrame()

    def initialize(self):
        # Updated U(0,1) Matrices (do we really need pd.DataFrames?)
        self.firstLevelMatrix = pd.DataFrame(
        np.round(1*np.random.random_sample((self.amountInputUnits,self.amountHiddenUnits)),2)
                                            )
                                            
        self.secondLevelMatrix = pd.DataFrame(
        np.round(1*np.random.random_sample((self.amountHiddenUnits,self.amountOutputUnits)),2)
                                             )
        
