from sklearn.metrics import roc_curve, auc

class TargetFunction:

    def getAUC(self, prediction, labels, regularizationTerm, weightDecay=1e-5, reg=True):
        # get False Positive and True Positive Rate using roc_curve 
        fpr, tpr, thresholds = roc_curve(labels, prediction)
        # compute the AUC and return it
        if reg:
            return auc(fpr, tpr) - weightDecay * regularizationTerm
        else:
            return auc(fpr, tpr)

