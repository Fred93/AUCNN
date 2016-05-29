__author__ = 'D059348'

import Selector.NaiveSelector
import Mutator.NaiveMutator
import Crossover.NaiveCrossover
import Population
import TargetFunction

class GeneticNeuralNetwork():

    amountGenerations = 100000
    generationSize = 1000
    selector = Selector.NaiveSelector.NaiveSelector()
    mutator = Mutator.NaiveMutator.NaiveMutator()
    crossover = Crossover.NaiveCrossover.NaiveCrossover()

    def initializeGeneration(self):
        generation = []
        for i in range(self.generationSize):
            population = Population()
            population.initialize()
            generation.append(population)
        return generation

    def trainNeuralNetwork(self, trainingset):
        #TODO: implement more sophisticated stop condition
        generation = self.initializeGeneration()
        for i in range(self.amountGenerations):
            generation = self.processGeneration(generation, trainingset)

    def processGeneration(self, generation, trainingset):
        survivors = self.selector.select(generation, trainingset)

        #TODO: Clever Mutation Candidate selection (Random??)
        mutatedPopulation = self.mutator.mutate(survivors[0])

        #TODO: Clever Crossover candidate selection (Random??)
        crossoveredPopulation = self.crossover.crossover(survivors[0], survivors[1])

        return mutatedPopulation + crossoveredPopulation

    def calculateNetworkOutput(self, population, data):
            return 1

    def testNeuralNetwork(self, network, testset):
        Ys = None
        output = self.calculateNetworkOutput(network, testset)
        target = TargetFunction()
        auc = target.getAUC(output, Ys)
        return auc
