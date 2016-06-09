import random
rand = random.Random()
rand.seed(None)
import AbstractCrossover
import numpy as np

class ColumCrossover(AbstractCrossover.AbstractCrossover): 'Tauscht die Gewichte für die B-Knoten aus, bei der Annahme: B1 ... Bn stehen in den Spalten,'


    def __init__(self):
        pass


    def ColumCrossover(self, e):'Annamhme: e ist ein array mit Matrizen von A nach B oder B nach C'

        i = 0

        while i < (e[0].shape[1] - 1):  ' -1 um bei ungeraden arrays die letzte Einheit stehen zu lassen'

            randompoint = rand.randint(0, e[i].shape[1])

            zwischenspeicher = np.matrix(e[i][:, 0:randompoint])
            e[i][:, 0:randompoint] = e[i + 1][:, 0:randompoint]
            e[i + 1][:, 0:randompoint] = zwischenspeicher

            i = i + 2

        return e

        print('ColuuumCroschover isch ready to rumble')

