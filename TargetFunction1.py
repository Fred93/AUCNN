__author__ = 'D059348'

class TargetFunction:

    def getAUC(self,prediction,labels):
        
        # import metric functions
        from sklearn.metrics import roc_curve, auc # maybe import outside of function or class?
        
        # get False Positive and True Positive Rate using roc_curve 
        fpr, tpr, thresholds = roc_curve(labels, prediction)
        # compute the AUC and return it
        return auc(fpr, tpr)

