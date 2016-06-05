import numpy as np
from scipy.special import expit

def calculateOutput(chromosome, data):
    input = np.mat(data)
    input = np.append(np.mat(1), input, axis=1)                                         #add bias unit

    hiddenLayer_input = input * chromosome.firstLevelMatrix
    hiddenLayer_output = np.mat(np.apply_along_axis(expit, 0, hiddenLayer_input))       #elementwise sigmoid
    hiddenLayer_output = np.append(np.mat(1), hiddenLayer_output, axis=1)               #add bias unit

    outputLayer_input = hiddenLayer_output * chromosome.secondLevelMatrix
    outputLayer_output = np.mat(np.apply_along_axis(expit, 0, outputLayer_input))       #elementwise sigmoid

    return outputLayer_output
