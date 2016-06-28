import numpy as np
import timeit
from scipy.special import expit
import math

class FeedforwardNetwork():
    chromosome = None

    def __init__(self, chromosome):
        self.chromosome = chromosome

    def sigm(self, x):
        return 1/(1+np.exp(-x))

    def calculateOutput(self, data):
        input = np.mat(data)
        ones = np.transpose(np.mat(np.ones(input.shape[0])))
        input = np.append(ones, input, axis=1)                                         #add bias unit
        hiddenLayer_input = input * self.chromosome.firstLevelMatrix#  /self.chromosome.firstLevelMatrix.shape[0}

        hiddenLayer_output = np.mat(np.apply_along_axis(self.sigm, 0, hiddenLayer_input))
        ones = np.transpose(np.mat(np.ones(hiddenLayer_output.shape[0])))

        hiddenLayer_output = np.append(ones, hiddenLayer_output, axis=1)               #add bias unit


        outputLayer_input = hiddenLayer_output * self.chromosome.secondLevelMatrix# / self.chromosome.secondLevelMatrix.shape[0]
        outputLayer_output = np.mat(np.apply_along_axis(self.sigm, 0, outputLayer_input))       #elementwise sigmoid

        return outputLayer_output
