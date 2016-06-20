import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import SGD, Adam, Adadelta, Adagrad
from keras.regularizers import l1, l2
from keras.utils import np_utils
from sklearn.preprocessing import StandardScaler 
from sklearn import metrics
from sklearn.cross_validation import KFold
import itertools # for grid


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

def shuffle(X, y, subset = 200000, seed=3007):
    np.random.seed(seed)
    shuffle = np.arange(len(y))
    np.random.shuffle(shuffle)
    X = X[shuffle]
    y = y[shuffle]
    return X[0:subset], y[0:subset]

def createGrid(tuning_parameters):
    grid = []
    for element in itertools.product(*tuning_parameters):
        grid.append(element)
    return grid
    
# get a random subset of 200.000 observation
X = X.values
y = y.values
#X, y = shuffle(X, y)


# quick preprocessing
Y = np_utils.to_categorical(y)

## Model building with Keras
def buildModel(weight_decay1, weight_decay2, nodes_per_layer, activation_functions=['sigmoid','sigmoid'], 
               solver='Adadelta', regulization_method='l2'):
    
    # Sequential to get a linear layer structure as in feedforward networks
    model = Sequential()
    
    if(regulization_method is 'l1'):
            # input to hidden layer
            model.add(Dense(input_dim=X_train.shape[1], # input dimension
                      output_dim=nodes_per_layer, # output dimension
                      init='uniform', # initialization of the weights
                      activation=activation_functions[0], # activation function,
                      W_regularizer=l1(weight_decay1),  # weight decay on the first level conncetion weight
                      b_regularizer=l1(weight_decay1)   # weight decay for bias unit              
                      ))
            # hidden to output layer
            model.add(Dense(input_dim=nodes_per_layer, # input dimension must match the previous output_dim
                            output_dim=2, # output dimension must match the target dimension
                            init='uniform', # initialization of the weights
                            activation=activation_functions[1], # activation function,
                        W_regularizer=l1(weight_decay2),  # weight decay 
                        b_regularizer=l1(weight_decay2)   # weight decay for bias unit              
                        ))
    else:
        # input to hidden layer
        model.add(Dense(input_dim=X_train.shape[1], # input dimension
                        output_dim=nodes_per_layer, # output dimension
                        init='uniform', # initialization of the weights
                        activation=activation_functions[0], # activation function,
                        W_regularizer=l2(weight_decay1),  # weight decay on the first level conncetion weight
                        b_regularizer=l2(weight_decay1)   # weight decay for bias unit              
                        ))
        
        # hidden to output layer
        model.add(Dense(input_dim=nodes_per_layer, # input dimension must match the previous output_dim
                        output_dim=2, # output dimension must match the target dimension
                        init='uniform', # initialization of the weights
                        activation=activation_functions[1], # activation function,
                        W_regularizer=l2(weight_decay2),  # weight decay 
                        b_regularizer=l2(weight_decay2)   # weight decay for bias unit              
                        ))
    
    # setup solver 
    if(solver is 'Adam'):
        bp = Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08)
    if(solver is 'Adadelta'):
        bp = Adadelta(lr=1.0, rho=0.95, epsilon=1e-08)
    if (solver is 'Adagrad'):
        bp = Adagrad(lr=0.01, epsilon=1e-08)
    else:
        bp = SGD(lr=0.01)  
        # learning rate recommended to tune, but was found to have no influenceas long it is between 0.01 and 0.1
    
    # compile model    
    model.compile(loss='binary_crossentropy', optimizer=bp, class_mode="binary")
    return model

#----------------------------------------------------------------------------------------------------------#

################################## Actual Model Training #################################################

# prepare input and out dimension
input_dim = X.shape[1]
output_dim = 2

# specifying tuning parameters
nodes_per_layer = [200] # the bigger the better 
batch_size = 10000 # was varied from 16, 32 to 10000, but no difference so far
epoch = 1000  # mainly computational but above 500 I did not see any improvements
hidden_activation = ["sigmoid", "tanh"] # activation for input to hidden, so far only sigmoid tried
output_activation = ["sigmoid", "tanh"] # activation for hidden to output: so far only sigmoid tried
solver = ['Adagrad', 'Adadelta']  
weight_decay1 = [1e-5]  # could be set different for each connection between two layers 
weight_decay = weight_decay1 # setting both weight decays equal
regulization_method = ['l1','l2'] 

# specify parameters to tune in grid search
tuning_parameters = [nodes_per_layer,weight_decay, regulization_method]

# create grid of parameters
grid = createGrid(tuning_parameters)

max_auc = 0.62  # best auc so far 
best_parameter = {'nodes': 200, 'weight decay': 1e-5} 
average_aucs = np.array([]) # array to store all average aucs for different parameters
sd_aucs = np.array([]) # to store all standard deviation of aucs
for i in range(len(grid)):    
    
    print('---'*30)
    print('remaining iterations:', len(grid) - i)
    print('best auc so far is:', max_auc)
    print('best set of parameters are', best_parameter)
    
    next_parameters = {'nodes': grid[i][0], 'weight decay': grid[i][1],'regulization': grid[i][2]}
    print('Now try: ', next_parameters)
    
    nb_folds = 5
    kfolds = KFold(len(y), nb_folds)
    #av_roc = 0.
    
    auc = np.array([]) # array to store all aucs in each fold
    f = 0
    for train, valid in kfolds:
        
        print('---'*20)
        print('Fold', f+1)
        
        # counting folds
        f += 1
        # splitting the folds
        X_train = X[train]
        X_valid = X[valid]
        Y_train = Y[train]
        Y_valid = Y[valid]
        y_valid = y[valid] # for auc calculation
        
        print("Building model...")#
        model = buildModel(
                           nodes_per_layer=grid[i][0], 
                           weight_decay1=grid[i][1],
                           weight_decay2=grid[i][1],
                           regulization_method = grid[i][2],
                           solver='Adadelta'
                           )
        
        print("Training model...")
        
        # fitting the model
        model.fit(X_train,
                  Y_train, 
                  nb_epoch=epoch,  # number of epoch: 300, 500 and 1000 tried no difference so far
                  batch_size=batch_size,  # possible parameter to tune afterwards
                  validation_data=(X_valid, Y_valid), 
                  verbose=0
                  )
        # prediction         
        valid_preds = model.predict_proba(X_valid, verbose=0)
        valid_preds = valid_preds[:, 1]
        auc_iteration = metrics.roc_auc_score(y_valid, valid_preds)
        print("AUC:", auc_iteration)
        print('---'*20)
        
        # save auc score of current iteration
        auc = np.append(auc,auc_iteration)
    
    if np.mean(auc) > max_auc:
        max_auc = np.mean(auc)
        best_parameter = {'nodes': grid[i][0], 'weight decay': grid[i][1], 'regulization': grid[i][2]}
    
    average_aucs = np.append(average_aucs, np.mean(auc)) 
    sd_aucs = np.append(sd_aucs, np.std(auc))
    
    print('****'*20)
    print('****'*20)
    print('Average AUC:', np.mean(auc))   
    print('Parameters: ', next_parameters)
    print('****'*20)
    print('****'*20)    



model_results =  np.column_stack((average_aucs, sd_aucs,np.array(grid))) 
print model_results