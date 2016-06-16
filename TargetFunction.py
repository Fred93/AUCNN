from sklearn.metrics import roc_curve, auc

class TargetFunction:

    def getAUC(self,prediction,labels):
        print "prediction: "
        print prediction

        print "labels: "
        print labels
        
        # import metric functions
        
        # get False Positive and True Positive Rate using roc_curve 
        fpr, tpr, thresholds = roc_curve(labels, prediction)
        # compute the AUC and return it
        return auc(fpr, tpr)

