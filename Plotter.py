__author__ = 'D059348'
from ggplot import *
import pandas as pd

def plotLearningCurve(bestSolutions, avgSolutions):
    df = pd.DataFrame()
    df['Generation'] = range(len(bestSolutions))
    df['BestSolutions'] = bestSolutions
    df['AvgSolutions'] = avgSolutions
    plot = ggplot(aes(x = 'Generation'), data=df) + geom_line(aes(y='BestSolutions', colour="red")) + geom_line(aes(y='AvgSolutions', colour="blue")) + ggtitle('Learning Curve')
    print plot

