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


    selector = Selector.RouletteSelector.RouletteSelector()
    mutator = Mutator.NormalMutator.NaiveMutator()
    crossover = Crossover.RowCrossover.RowCrossover()
    regularizer = Regularization.RidgeL2.RidgeL2()

    #Parameters
    amountGenerations = 5
    populationSize = 100

    mutationRate = 0.05
    mutationRange = (-0.05, 0.05)
    crossoverRate = 0.05

    weightDecay = 1e-5

    avgSolutions = np.array([])
    bestSolutions = np.array([])

    def solve(self):
        path = "/Users/maximilianandres/Downloads/training.csv"
        data = pd.read_csv(path)
        y = data['returnBin']
        X = data.drop(['returnBin', 'Unnamed: 0'], axis=1)
        seed = np.random.seed(3007)
        np.random.seed(seed)
        shuffle = np.arange(len(y))
        np.random.shuffle(shuffle)
        X = X.values[shuffle]
        y = y[shuffle]
        subset = 100000
        X = X[0:subset]
        y = y[0:subset]


        #IMPLEMENT CV HERE!!!

        self.trainNeuralNetwork(X,y)
        #Plotter.plotLearningCurve(self.bestSolutions, self.avgSolutions)

        pickle.dump(self.bestSolutions, open("/Users/maximilianandres/Google Drive/Humboldt/2. Semester/Applied Predictive Modelling/bestSolutions.pickle","wb"), protocol=2)
        pickle.dump(self.avgSolutions, open("/Users/maximilianandres/Google Drive/Humboldt/2. Semester/Applied Predictive Modelling/avgSolutions.pickle","wb"), protocol=2)

    def initializePopulation(self, inputUnits):
        print "initialize population ... "
        population = np.array([])
        for i in range(self.populationSize):
            chromosome = Chromosome.Chromosome(inputUnits, 200, 1)
            chromosome.initialize()
            population = np.append(population, chromosome)
        return population

    def trainNeuralNetwork(self, X, y):
        #TODO: implement more sophisticated stop condition
        population = self.initializePopulation(X.shape[1])
        for i in range(self.amountGenerations):
            print "Process Generation #" + str(i)
            population = self.processPopulation(population, X, y)

    def processPopulation(self, population, X, y):
        fitness = self.calculateFitnessVector(population, X, y)
        print("\t Fittest Chromosome: " + str(np.max(fitness)))
        self.bestSolutions = np.append(self.bestSolutions, np.max(fitness))
        self.avgSolutions = np.append(self.avgSolutions, np.mean(fitness))
        #fitness = np.array((0.5,0.7,0.1,0.3,0.9,0.8,0.5,0.7,0.1,0.3,0.9,0.8,0.1,0.4,0.5,0.2))
        print "\t Selection ..."
        print("\t Avg Fitness before selection: " + str(np.mean(fitness)))
        newPopulation = self.selector.select(population, fitness, perform_elitism=True)
        #print("Avg Fitness after selection: " + str(np.mean(self.calculateFitnessVector(newPopulation, X, y))))
        print "\t Crossover ..."
        crossoverIndices = random.sample(range(0, population.size), int(population.size*self.crossoverRate))
        newPopulation[crossoverIndices] = self.crossover.crossover(newPopulation[crossoverIndices])

        print "\t Mutation ..."
        mutatedPopulation = self.mutator.mutate(newPopulation, self.mutationRate, self.mutationRange)
        #print "mutated population: "
        #print mutatedPopulation.size
        return mutatedPopulation
        #return newPopulation
    def testNeuralNetwork(self, chromosome, X, y):
        chromosome = chromosome[0]
        fnn = FeedforwardNetwork.FeedforwardNetwork(chromosome)
        output = fnn.calculateOutput(X)
        target = TargetFunction.TargetFunction()
        regularizationTerm = self.regularizer.regularize(chromosome)
        auc = target.getAUC(output, y, regularizationTerm, self.weightDecay)
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
