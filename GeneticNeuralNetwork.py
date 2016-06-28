import Selector.NaiveSelector
import Selector.RouletteSelector
import Selector.TournamentSelector
import Mutator.NaiveMutator
import Crossover.NaiveCrossover
import Crossover.ColumnCrossover
import Crossover.PointCrossover
import Crossover.RowCrossover
import Mutator.NormalMutator
import Chromosome
import Regularization.RidgeL2
import TargetFunction
import FeedforwardNetwork
import numpy as np
import pandas as pd
import random
import pickle
#import Plotter
#import dask.dataframe as dd
#import dask.multiprocessing

class GeneticNeuralNetwork():
    '''
    Main class for the Genetic Neural Network. The algorithm parameters are specified in this class.
    Manages the training of the neural network.
    '''

    dir = "C:/Users/D059348/PycharmProjects/AUCNN"

    #Selection of implemented genetic operators
    selector = Selector.RouletteSelector.RouletteSelector()
    mutator = Mutator.NormalMutator.NaiveMutator()
    crossover = Crossover.RowCrossover.RowCrossover()
    regularizer = Regularization.RidgeL2.RidgeL2()

    #Parameters
    amountGenerations = 50 #50
    populationSize = 150 #100

    mutationRate = 0.08
    mutationRange = (-0.1, 0.1)
    crossoverRate = 0.05

    mutationRateOptions = (0.01, 0.1)
    crossoverRateOptions = (0.01, 0.1)
    mutationRangeOptions = ((-0.05, 0.05), (-0.5, 0.5))

    weightDecay = 1e-5

    avgSolutions = np.array([])
    bestSolutions = np.array([])

    def solve(self, path):
        '''
        Main function of the Genetic Neural network. Must be called to create a neural network based on
        the passed data.
        '''
        path = self.dir + path
        data = pd.read_csv(path)

        #Create subset of the data
        y = data['returnBin']
        X = data.drop(['returnBin', 'Unnamed: 0'], axis=1)
        seed = np.random.seed(3007)
        np.random.seed(seed)
        shuffle = np.arange(len(y))
        np.random.shuffle(shuffle)
        X = X.values[shuffle]
        y = y[shuffle]
        subset = 50000   #40000
        X = X[0:subset]
        y = np.array(y[0:subset])

        #Test all different parameter combinations
        for crossoverRate in self.crossoverRateOptions:
            for mutationRange in self.mutationRangeOptions:
                for mutationRate in self.mutationRateOptions:
                    self.mutationRange = mutationRange
                    self.mutationRate = mutationRate
                    self.crossoverRate = crossoverRate

                    #4 fold Cross Validation
                    splits = np.array(np.split(np.arange(subset), 4))
                    results = []
                    for i in range(4):
                        inds_train = self.mergeSplits(np.array(splits[np.arange(len(splits))[np.arange(len(splits)) != i]]))
                        inds_test = np.array(splits[i])
                        X_train = X[inds_train]
                        X_test = X[inds_test]
                        y_train = y[inds_train]
                        y_test = y[inds_test]

                        self.avgSolutions = np.array([])
                        self.bestSolutions = np.array([])

                        #Train and test neural network
                        nn = self.trainNeuralNetwork(X_train,y_train)
                        auc = self.testNeuralNetwork(np.array([nn]), X_test, y_test, reg=False)[0]
                        results.append(auc)

                        #store result of single run in pickle file
                        filenameExtension = "_" + str(mutationRate) + "_" + str(mutationRange[1]) + "_" + str(crossoverRate) + "_" + str(i) + ".pickle"
                        pickle.dump(self.bestSolutions, open(self.dir + "/learningCurve/bestSolutions" + filenameExtension,"wb"), protocol=2)
                        pickle.dump(self.avgSolutions, open(self.dir + "/learningCurve/avgSolutions" + filenameExtension,"wb"), protocol=2)

                        print auc

                    #store CV result in pickle file
                    filename = "cvResult_" + str(mutationRate) + "_" + str(mutationRange[1]) + "_" + str(crossoverRate) + ".pickle"
                    pickle.dump(results, open(self.dir + "/result/" + filename,"wb"), protocol=2)

        #self.trainNeuralNetwork(X,y)
        #Plotter.plotLearningCurve(self.bestSolutions, self.avgSolutions)


    def mergeSplits(self, splits):
        mergedArray = np.array([])
        for s in splits:
            mergedArray = np.append(mergedArray, s)
        return  np.apply_along_axis(int, 0, np.mat((mergedArray)))


    def initializePopulation(self, inputUnits):
        '''
        Initializes as many individuals as specified in the population size.
        Returns all instantiated chromosomes in a numpy-array.
        '''
        print "initialize population ... "
        population = np.array([])
        for i in range(self.populationSize):
            chromosome = Chromosome.Chromosome(inputUnits, 200, 1)
            chromosome.initialize()
            population = np.append(population, chromosome)
        return population

    def trainNeuralNetwork(self, X, y):
        '''
        Trains a neural network using the genetic algorithm. Processes a generations as often as specified
        in the variable amountGenerations.
        Returns the strongest neural network of the last generation based on the training data.
        '''
        population = self.initializePopulation(X.shape[1])
        fitness = self.calculateFitnessVector(population, X, y)

        for i in range(self.amountGenerations):
            print "Process Generation #" + str(i)
            population, fitness = self.processPopulation(population, X, y, fitness)
        return population[np.argmax(fitness)]

    def processPopulation(self, population, X, y, previousFitness):
        '''
        Processes a population of one generation. The first step is the selection. Afterwards some random individuals
        are chosen for crossover (based on crossover rate). Crossovers and Mutations are executed. Afterwards
        the Post Selector is choosing the final population of one generation.
        The return value of this function is a numpy-array that contains the new generation.
        '''
        fitness = previousFitness
        print("\t Fittest Chromosome: " + str(np.max(fitness)))
        print("\t Avg Fitness before selection: " + str(np.mean(fitness)))
        self.bestSolutions = np.append(self.bestSolutions, np.max(fitness))
        self.avgSolutions = np.append(self.avgSolutions, np.mean(fitness))

        print "\t Selection ..."
        previousPopulation = population
        newPopulation = self.selector.select(population, fitness, perform_elitism=True)

        print "\t Crossover ..."
        crossoverIndices = random.sample(range(0, population.size), int(population.size*self.crossoverRate))
        newPopulation[crossoverIndices] = self.crossover.crossover(newPopulation[crossoverIndices])

        print "\t Mutation ..."
        mutatedPopulation = self.mutator.mutate(newPopulation, self.mutationRate, self.mutationRange)

        fitness = self.calculateFitnessVector(population, X, y)

        finalGenerationPopulation, finalFitness = self.getFinalGenerationPopulation(previousPopulation, previousFitness, mutatedPopulation, fitness)
        return (finalGenerationPopulation, finalFitness)

    def getFinalGenerationPopulation(self, prevPop, prevFitness, newPop, newFitness):
        '''
        Implements the Post Selector. The post selector is called after crossovers and mutations. It ensures
        that modified individuals are chosen only if they improve the value of the target function.
        '''
        finalPop, finalFitness = np.array([]), np.array([])
        for i in range(len(prevFitness)):
            if prevFitness[i] > newFitness[i]:
                finalPop = np.append(finalPop, prevPop[i])
                finalFitness = np.append(finalFitness, prevFitness[i])
            else:
                finalPop = np.append(finalPop, newPop[i])
                finalFitness = np.append(finalFitness, newFitness[i])
        return (finalPop, finalFitness)

    def testNeuralNetwork(self, chromosome, X, y, reg = True):
        '''
        Tests a neural network based on new (ideally unseen) data.
        '''
        chromosome = chromosome[0]
        fnn = FeedforwardNetwork.FeedforwardNetwork(chromosome)
        output = fnn.calculateOutput(X)
        target = TargetFunction.TargetFunction()
        regularizationTerm = self.regularizer.regularize(chromosome)
        auc = target.getAUC(output, y, regularizationTerm, self.weightDecay, reg)
        return np.array([auc])

    def calculateFitnessVector(self, population, X, y):
        '''
        Returns a fitness vector for a whole population.
        '''
        fitness = np.apply_along_axis(self.testNeuralNetwork, axis=0, arr=np.mat(population), X=X, y=y)
        return fitness[0]

if __name__ == "__main__":
    gnn = GeneticNeuralNetwork()
    gnn.solve("/Data/training.csv")
