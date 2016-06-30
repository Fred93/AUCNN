import numpy as np
import random

class Chromosome:

    """
    Implements an individual (= 1 Neural Network) in the genetic framework.

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
        '''
        Initialized the weights of the neural network. By random (50/50 chance) it is initialized with normal or an
        uniform distribution.
        '''
        if random.random() > 0.5:

            # Updated U(-1,1) Matrices
            self.firstLevelMatrix = np.mat(
            np.round(2*np.random.random_sample((self.amountInputUnits+1,self.amountHiddenUnits)), 2) - 1)

            self.secondLevelMatrix = np.mat(
            np.round(2*np.random.random_sample((self.amountHiddenUnits+1,self.amountOutputUnits)), 2) - 1)
        else:
            # N(0,1)
            self.firstLevelMatrix = np.mat(
            np.round(np.random.normal(0.0, 1.0,(self.amountInputUnits+1,
                                                             self.amountHiddenUnits)), 2))

            self.secondLevelMatrix = np.mat(
            np.round(np.random.normal(0.0, 1.0,(self.amountHiddenUnits+1,
                                                             self.amountOutputUnits)), 2))

    def sigm(self, x):
        '''
        Efficient implementation of the sigmoid function.
        '''
        return 1/(1+np.exp(-x))

    def calculateOutput(self, data):
        '''
        Calculates the output of the neural network given a input matrix.
        The result value is a vector with class probabilities.
        '''
        input = np.mat(data)
        ones = np.transpose(np.mat(np.ones(input.shape[0])))
        input = np.append(ones, input, axis=1)                                         #add bias unit
        hiddenLayer_input = input * self.firstLevelMatrix

        hiddenLayer_output = np.mat(np.apply_along_axis(self.sigm, 0, hiddenLayer_input))
        ones = np.transpose(np.mat(np.ones(hiddenLayer_output.shape[0])))

        hiddenLayer_output = np.append(ones, hiddenLayer_output, axis=1)               #add bias unit


        outputLayer_input = hiddenLayer_output * self.secondLevelMatrix
        outputLayer_output = np.mat(np.apply_along_axis(self.sigm, 0, outputLayer_input))       #elementwise sigmoid

        return outputLayer_output