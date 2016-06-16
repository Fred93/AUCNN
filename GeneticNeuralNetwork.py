from sympy.polys.polyoptions import Gen
import Selector.NaiveSelector
import Selector.RouletteSelector
import Selector.TournamentSelector
import Mutator.NaiveMutator
import Crossover.NaiveCrossover
import Crossover.ColumnCrossover
import Mutator.NormalMutator
import Chromosome
import TargetFunction
import FeedforwardNetwork
import numpy as np
import random

class GeneticNeuralNetwork():


    selector = Selector.RouletteSelector.RouletteSelector()
    mutator = Mutator.NormalMutator.NaiveMutator()
    crossover = Crossover.ColumnCrossover.ColumnCrossover()

    #Parameters
    amountGenerations = 500
    populationSize = 16

    mutationRate = 0.1
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
            print "Process Generation #" + str(i)
            population = self.processPopulation(population, trainingset)

    def processPopulation(self, population, trainingset):
        fitness = self.calculateFitnessVector(population, trainingset)
        #fitness = np.array((0.5,0.7,0.1,0.3,0.9,0.8,0.5,0.7,0.1,0.3,0.9,0.8,0.1,0.4,0.5,0.2))
        print "\t Selection ..."
        newPopulation = self.selector.select(population, fitness)
        print "\t Crossover ..."
        crossoverIndices = random.sample(range(0, population.size), int(population.size*self.crossoverRate))
        newPopulation[crossoverIndices] = self.crossover.crossover(newPopulation[crossoverIndices])

        print "\t Mutation ..."
        mutatedPopulation = self.mutator.mutate(newPopulation, self.mutationRate, self.mutationRange)
        #print "mutated population: "
        #print mutatedPopulation.size
        return mutatedPopulation

    def testNeuralNetwork(self, chromosome, testset):
        Ys = np.transpose(np.mat(np.array((1,0,0,1,0,1))))
        fnn = FeedforwardNetwork.FeedforwardNetwork(chromosome)
        output = fnn.calculateOutput(testset)
        target = TargetFunction.TargetFunction()
        auc = target.getAUC(output, Ys)
        return auc

    def calculateFitnessVector(self, population, testset):
        vec = np.array([])
        for chromosome in population:
            vec = np.append(vec, self.testNeuralNetwork(chromosome, testset))
        return  vec

if __name__ == "__main__":
    gnn = GeneticNeuralNetwork()
    gnn.solve()
