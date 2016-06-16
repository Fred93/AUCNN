from sympy.polys.polyoptions import Gen
import Selector.NaiveSelector
import Mutator.NaiveMutator
import Crossover.NaiveCrossover
import Chromosome
import TargetFunction
import FeedforwardNetwork
import numpy as np
import random

class GeneticNeuralNetwork():


    selector = Selector.NaiveSelector.NaiveSelector()
    mutator = Mutator.NaiveMutator.NaiveMutator()
    crossover = Crossover.NaiveCrossover.NaiveCrossover()

    #Parameters
    amountGenerations = 500
    populationSize = 200

    mutationRate = 0.01
    mutationRange = (-0.2, 0.2)
    crossoverRate = 0.25

    def solve(self):
        self.trainNeuralNetwork(np.arange(18).reshape((6,3)))

    def initializePopulation(self):
        print "initialize population ... "
        population = np.array([])
        for i in range(self.populationSize):
            chromosome = Chromosome.Chromosome()
            chromosome.initialize()
            population = np.append(population, chromosome)
        return population

    def trainNeuralNetwork(self, trainingset):
        #TODO: implement more sophisticated stop condition
        population = self.initializePopulation()
        for i in range(self.amountGenerations):
            population = self.processPopulation(population, trainingset)

    def processPopulation(self, population, trainingset):
        print "Process Population"
        #fitness = self.calculateFitnessVector(population, trainingset)
        fitness = np.array((0.5,0.7,0.1,0.3,0.9,0.8))
        newPopulation = self.selector.select(population, fitness)
        crossoverIndices = random.sample(range(0, population.size), int(population.size*self.crossoverRate))
        newPopulation[crossoverIndices] = self.crossover.crossover(newPopulation[crossoverIndices])

        mutatedPopulation = self.mutator.mutate(newPopulation, self.mutationRate, self.mutationRange)

        return mutatedPopulation

    def testNeuralNetwork(self, chromosome, testset):
        print chromosome
        print "hey"
        Ys = np.transpose(np.mat(np.array((1,0,0,1,0,1))))
        fnn = FeedforwardNetwork.FeedforwardNetwork(chromosome)
        output = fnn.calculateOutput(testset)
        print output
        target = TargetFunction.TargetFunction()
        auc = target.getAUC(output, Ys)
        return auc

    def calculateFitnessVector(self, population, testset):
        vec = np.array
        for chromosome in population:
            np.append(vec, self.testNeuralNetwork(chromosome, testset))
        return  vec

if __name__ == "__main__":
    gnn = GeneticNeuralNetwork()
    gnn.solve()
