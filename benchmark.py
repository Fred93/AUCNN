# import libraries
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import SGD
from keras.regularizers import l2
from sklearn.preprocessing import StandardScaler
from keras.utils import np_utils
from sklearn import metrics
from sklearn.cross_validation import KFold


# load data and define target vector and feature matirx
df = pd.read_csv("training.csv", index_col=0)  
y = df["returnBin"]
X = df.drop('returnBin', 1)

"""
Note training.csv and validation.csv are splitted randomly from the labeled data in data2_7_full.rda. 
Specifically they includes:
- a binary target variable called returnBin and not the actual labels which are stored in acutal_label.csv
- only 35 variable instead of 50, since these are only useful for prediction
  (e.g. orderID and similar variables are excluded)
- yearQuarter was coded badly and coverted into 3 dummies 

For further information see the createData.R script 
"""

# Scale all variable except dummies 
def scale_data(X):
    scaler = StandardScaler()
    scaler.fit(X)
    X = scaler.transform(X)
    return X

def shuffle(X, y, seed=1):
    np.random.seed(seed)
    shuffle = np.arange(len(y))
    np.random.shuffle(shuffle)
    X = X[shuffle]
    y = y[shuffle]
    return X, y
    

X = X.values[0:200000]
y = y.values[0:200000]

X, y = shuffle(X, y)
X = scale_data(X)
Y = np_utils.to_categorical(y)

## Model building with Keras
def buildModel(learning_rate, weight_decay, nodes_per_layer, activation_functions=['sigmoid','sigmoid']):
    # Sequential to get a linear layer structure as in feedforward networks
    model = Sequential()

    # input to hidden layer
    model.add(Dense(input_dim=X_train.shape[1], # input dimension
                    output_dim=nodes_per_layer, # output dimension
                    init='uniform', # initialization of the weights
                    activation=activation_functions[0], # activation function,
                    W_regularizer=l2(weight_decay),  # weight decay on the first level conncetion weight
                    b_regularizer=l2(weight_decay)   # weight decay for bias unit              
                    ))

    # hidden to output layer
    model.add(Dense(input_dim=nodes_per_layer, # input dimension must match the previous output_dim
                    output_dim=2, # output dimension must match the target dimension
                    init='uniform', # initialization of the weights
                    activation=activation_functions[1], # activation function,
                    W_regularizer=l2(weight_decay),  # weight decay 
                    b_regularizer=l2(weight_decay)   # weight decay for bias unit              
                    ))

    """
    Specify the backpropagation algorithm: 
        - SGD = BP?
        - lr - learning rate
        - decay - probably not the weight decay but 
        - momentum - a term to weight t-1-th iteration insteat of the t-th iteration in the learning rate
                 (we set this to 0) 
                 """
    # compile model
    bp = SGD(lr=learning_rate)
    model.compile(loss='binary_crossentropy', optimizer=bp)
    return model

input_dim = X.shape[1]
output_dim = 2

print("Validation...")

 
# specifying tuning parameters
nodes_per_layer = [6,12,18,24]
lr = [0.01, 0.05, 0.1]
weight_decay = [0.01,0.1,0.5,1]  # could be set different for each connection between two layers 

parameter = [nodes_per_layer,lr,weight_decay]

# create grid of parameters
grid = []
import itertools
for element in itertools.product(*parameter):
    grid.append(element)

max_auc = 0.5
best_parameter = {'nodes': 1, 'lr': 1, 'weight decay':1}  
for i in range(len(grid)):
    
    print('---'*30)
    print('remaining iterations:', len(grid) - i)
    print('best auc so far is:', max_auc)
    print('best set of parameters are', best_parameter)

    nb_folds = 4
    kfolds = KFold(len(y), nb_folds)
    #av_roc = 0.
    auc = np.array([])
    f = 0
    for train, valid in kfolds:
        
        print('---'*20)
        print('Fold', f)
        print('---'*20)
    
        f += 1
        X_train = X[train]
        X_valid = X[valid]
        Y_train = Y[train]
        Y_valid = Y[valid]
        y_valid = y[valid]

        print("Building model...")
        model = buildModel(nodes_per_layer=grid[i][0],
                           learning_rate=grid[i][1], 
                           weight_decay=grid[i][2])

        print("Training model...")

        # fitting the model
        model.fit(X_train,
                  Y_train, 
                  nb_epoch=500, 
                  batch_size=16, 
                  validation_data=(X_valid, Y_valid), 
                  verbose=0)
        # prediction         
        valid_preds = model.predict_proba(X_valid, verbose=0)
        valid_preds = valid_preds[:, 1]
        auc_iteration = metrics.roc_auc_score(y_valid, valid_preds)
        #print("AUC:", auc_iteration)
        
        # save auc score of current iteration
        auc = np.append(auc,auc_iteration)
    
    
    if np.mean(auc) > max_auc:
        max_auc = np.mean(auc)
        best_parameter = {'nodes': grid[i][0], 'lr': grid[i][1], 'weight decay': grid[i][0]}
    
    print('****'*20)
    print('****'*20)
    print('Average AUC:', np.mean(auc))   
    print('Variance AUC:', np.std(auc))
    print('lr', grid[i][1])
    print('weight decay', grid[i][2])
    print('nodes', grid[i][0])
    print('****'*20)
    print('****'*20)    
    
    
    




