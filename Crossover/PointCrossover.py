import numpy as np
import random
rand = random.Random()
rand.seed(None)
import AbstractCrossover

class PointCrossover(AbstractCrossover.AbstractCrossover):

    def __init__(self):
        pass


    def pointcrossover(self, ABlist, BClist):
        'ABlist liste mit arrays von A nach B, BClist array mit Matrizen von B nach C'

        for i in 0:len(ABlist): #funktioniert noch nicht! for muss noch angepasst werden und dann zu apply!

            randompoint = rand.randint(0, (len(ABlist[i]))) #ohne minus da, da python 0:4 als bis zur 4ten Zahl definiert

            zwischenspeicher = ABlist[i][0:randompoint]
            ABlist[i][0:randompoint] = ABlist[i+1][0:randompoint]
            ABlist[i+1][0:randompoint] = zwischenspeicher