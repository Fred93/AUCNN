import random
rand = random.Random()
rand.seed(None)
import AbstractCrossover

class PointCrossover(AbstractCrossover.AbstractCrossover):

    def __init__(self):
        pass


    def pointcrossover(self, list):
        'Annamhme: list array mit Matrizen von A nach B oder B nach C'

        while i < (len(list)-1): #-1 um bei ungeraden arrays die letzte Einheit stehen zu lassen

            randompoint = rand.randint(0, (len(list[i]))) #ohne minus isch ok, des läuft

            zwischenspeicher = list[i][0:randompoint]
            list[i][0:randompoint] = list[i+1][0:randompoint]
            list[i+1][0:randompoint] = zwischenspeicher

            i = i + 2

        print('pointcroschover isch over, gel')