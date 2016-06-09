import Selector.NaiveSelector
import Mutator.NaiveMutator
import Crossover.NaiveCrossover
import Chromosome
import TargetFunction

import numpy as np
import random

class GeneticNeuralNetwork():


    selector = Selector.NaiveSelector.NaiveSelector()
    mutator = Mutator.NaiveMutator.NaiveMutator()
    crossover = Crossover.NaiveCrossover.NaiveCrossover() #wählen und richtig importen

    #Parameters
    amountGenerations = 500
    populationSize = 200

    mutationRate = 0.01
    mutationRange = (-0.2, 0.2)
    crossoverRate = 0.25

    def initializePopulation(self):
        population = np.array([])
        for i in range(self.populationSize):
            chromosome = Chromosome()
            chromosome.initialize()
            population = np.append(population, chromosome)
        return population

    def trainNeuralNetwork(self, trainingset):
        #TODO: implement more sophisticated stop condition
        population = self.initializePopulation()
        for i in range(self.amountGenerations):
            population = self.processPopulation(population, trainingset)

    def processPopulation(self, population, trainingset):
        newPopulation = self.selector.select(population, trainingset)

        crossoverIndices = random.sample(range(0, population.size), population.size*self.crossoverRate)
        newPopulation[crossoverIndices] = self.crossover.crossover(newPopulation[crossoverIndices])

        mutatedPopulation = self.mutator.mutate(newPopulation, self.mutationRate, self.mutationRange)

        return mutatedPopulation



    def calculateNetworkOutput(self, population, data):
            return 1

    def testNeuralNetwork(self, network, testset):
        Ys = None
        output = self.calculateNetworkOutput(network, testset)
        target = TargetFunction()
        auc = target.getAUC(output, Ys)
        return auc
