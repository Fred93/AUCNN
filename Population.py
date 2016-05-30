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
        #TODO: values are just normal distributed
        self.firstLevelMatrix = pd.DataFrame(np.random.randn(self.amountInputUnits, self.amountHiddenUnits))
        self.secondLevelMatrix = pd.DataFrame(np.random.randn(self.amountHiddenUnits, self.amountOutputUnits))

