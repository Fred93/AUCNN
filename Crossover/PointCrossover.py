import random
rand = random.Random()
rand.seed(None)
import AbstractCrossover

class PointCrossover(AbstractCrossover.AbstractCrossover):

    def __init__(self):
        pass


    def crossover(self, list):'Annamhme: list ist ein array mit einem array mit weights von A nach B oder B nach C'

        i = 0

        while i < (len(list)-1): '-1 um bei ungeraden arrays die letzte Einheit stehen zu lassen'

            randompoint = rand.randint(0, (len(list[i]))) 'Die Anzahl der Attribute die vertauscht werden varriert mit jedem Tausch'

            zwischenspeicher = list[i][0:randompoint]
            list[i][0:randompoint] = list[i+1][0:randompoint]
            list[i+1][0:randompoint] = zwischenspeicher

            i = i + 2

        return list
        print('PointCroschover isch over, gel')