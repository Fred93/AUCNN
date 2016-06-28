from sklearn.metrics import roc_curve, auc

class TargetFunction:
    '''
    Implements the target function (AUC) of the genetic algorithm.
    '''

    def getAUC(self, prediction, labels, regularizationTerm, weightDecay=1e-5, regularize=True):
        # get False Positive and True Positive Rate using roc_curve 
        fpr, tpr, thresholds = roc_curve(labels, prediction)
        # compute the AUC and return it
        if regularize:
            return auc(fpr, tpr) - weightDecay * regularizationTerm
        else:
            return auc(fpr, tpr)

