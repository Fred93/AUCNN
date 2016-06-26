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
import timeit
#import Plotter
#import dask.dataframe as dd
#import dask.multiprocessing

class GeneticNeuralNetwork():

    dir = "/gitdata/AUCNN"

    selector = Selector.RouletteSelector.RouletteSelector()
    mutator = Mutator.NormalMutator.NaiveMutator()
    crossover = Crossover.RowCrossover.RowCrossover()
    regularizer = Regularization.RidgeL2.RidgeL2()

    #Parameters
    amountGenerations = 50 #50
    populationSize = 100 #100


    mutationRate = 0.08
    mutationRange = (-0.1, 0.1)
    crossoverRate = 0.05

    mutationRateOptions = (0.01, 0.1)
    crossoverRateOptions = (0.01, 0.1)
    mutationRangeOptions = ((-0.05, 0.05), (-0.5, 0.5))

    weightDecay = 1e-5

    avgSolutions = np.array([])
    bestSolutions = np.array([])

    def solve(self):
        path = self.dir + "/Data/training.csv"
        data = pd.read_csv(path)
        y = data['returnBin']
        X = data.drop(['returnBin', 'Unnamed: 0'], axis=1)
        seed = np.random.seed(3007)
        np.random.seed(seed)
        shuffle = np.arange(len(y))
        np.random.shuffle(shuffle)
        X = X.values[shuffle]
        y = y[shuffle]
        subset = 40000   #40000
        X = X[0:subset]
        y = np.array(y[0:subset])


        for crossoverRate in self.crossoverRateOptions:
            for mutationRange in self.mutationRangeOptions:
                for mutationRate in self.mutationRateOptions:
                    self.mutationRange = mutationRange
                    self.mutationRate = mutationRate
                    self.crossoverRate = crossoverRate
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

                        nn = self.trainNeuralNetwork(X_train,y_train)
                        auc = self.testNeuralNetwork(np.array([nn]), X_test, y_test)[0]
                        results.append(auc)

                        filenameExtension = "_" + str(mutationRate) + "_" + str(mutationRange[1]) + "_" + str(crossoverRate) + "_" + str(i) + ".pickle"
                        pickle.dump(self.bestSolutions, open(self.dir + "/learningCurve/bestSolutions" + filenameExtension,"wb"), protocol=2)
                        pickle.dump(self.avgSolutions, open(self.dir + "/learningCurve/avgSolutions" + filenameExtension,"wb"), protocol=2)

                        print auc


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
        print "initialize population ... "
        population = np.array([])
        for i in range(self.populationSize):
            chromosome = Chromosome.Chromosome(inputUnits, 200, 1)
            chromosome.initialize()
            population = np.append(population, chromosome)
        return population

    def trainNeuralNetwork(self, X, y):
        population = self.initializePopulation(X.shape[1])
        fitness = self.calculateFitnessVector(population, X, y)

        for i in range(self.amountGenerations):
            print "Process Generation #" + str(i)
            population, fitness = self.processPopulation(population, X, y, fitness)
        return population[np.argmax(fitness)]

    def processPopulation(self, population, X, y, previousFitness):
        fitness = previousFitness
        print("\t Fittest Chromosome: " + str(np.max(fitness)))
        self.bestSolutions = np.append(self.bestSolutions, np.max(fitness))
        self.avgSolutions = np.append(self.avgSolutions, np.mean(fitness))
        #fitness = np.array((0.5,0.7,0.1,0.3,0.9,0.8,0.5,0.7,0.1,0.3,0.9,0.8,0.1,0.4,0.5,0.2))
        print "\t Selection ..."
        print("\t Avg Fitness before selection: " + str(np.mean(fitness)))
        previousPopulation = population
        newPopulation = self.selector.select(population, fitness, perform_elitism=True)
        #print("Avg Fitness after selection: " + str(np.mean(self.calculateFitnessVector(newPopulation, X, y))))
        print "\t Crossover ..."
        crossoverIndices = random.sample(range(0, population.size), int(population.size*self.crossoverRate))
        newPopulation[crossoverIndices] = self.crossover.crossover(newPopulation[crossoverIndices])

        print "\t Mutation ..."
        mutatedPopulation = self.mutator.mutate(newPopulation, self.mutationRate, self.mutationRange)
        #print "mutated population: "
        #print mutatedPopulation.size
        fitness = self.calculateFitnessVector(population, X, y)
        finalGenerationPopulation, finalFitness = self.getFinalGenerationPopulation(previousPopulation, previousFitness, mutatedPopulation, fitness)
        return (finalGenerationPopulation, finalFitness)
        #return newPopulation

    def getFinalGenerationPopulation(self, prevPop, prevFitness, newPop, newFitness):
        finalPop, finalFitness = np.array([]), np.array([])
        for i in range(len(prevFitness)):
            if prevFitness[i] > newFitness[i]:
                finalPop = np.append(finalPop, prevPop[i])
                finalFitness = np.append(finalFitness, prevFitness[i])
            else:
                finalPop = np.append(finalPop, newPop[i])
                finalFitness = np.append(finalFitness, newFitness[i])
        return (finalPop, finalFitness)

    def testNeuralNetwork(self, chromosome, X, y):
        chromosome = chromosome[0]
        fnn = FeedforwardNetwork.FeedforwardNetwork(chromosome)
        start_o = timeit.default_timer()
        output = fnn.calculateOutput(X)
        #print "time taken for output calc: " + str(timeit.default_timer() - start_o)
        target = TargetFunction.TargetFunction()
        start_r = timeit.default_timer()
        regularizationTerm = self.regularizer.regularize(chromosome)
        #print "time taken for output ref: " + str(timeit.default_timer() - start_r)
        start_a= timeit.default_timer()
        auc = target.getAUC(output, y, regularizationTerm, self.weightDecay)
        #print "time taken for output auc: " + str(timeit.default_timer() - start_a)
        return np.array([auc])

    def calculateFitnessVector(self, population, X, y):
        '''
        df = pd.DataFrame(population)
        dask.set_options(get=dask.multiprocessing.get)
        df = dd.from_pandas(df, npartitions=20)
        dd_result = df.apply(self.testNeuralNetwork, axis=1, args=(X,y,))
        res = dd_result.compute()
        return res[0]
        '''
        fitness = np.apply_along_axis(self.testNeuralNetwork, axis=0, arr=np.mat(population), X=X, y=y)
        return fitness[0]

if __name__ == "__main__":
    gnn = GeneticNeuralNetwork()
    gnn.solve()
