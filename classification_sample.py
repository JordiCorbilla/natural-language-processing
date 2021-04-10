# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 20:59:18 2021

@author: Jordi Corbilla
"""
from __future__ import print_function, division
from future.utils import iteritems
from builtins import range, input
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn

# load the dataset
data = load_breast_cancer()

# Show characteristics of the data set

print(type(data))
print(data.keys())
# two dimensional array
print(data.data.shape)
# Column names and data
print(data.feature_names)
print(data.data)
# target as 0-1 values
print(data.target)
# name of the target values
# ['malignant' 'benign']
print(data.target_names)
# Every input sample will have a corresponding target
print(data.target.shape)

# Learning component
# split the data 1/3 of it will be for training
X_train, X_test, y_train, y_test = train_test_split(data.data, 
                                                     data.target, 
                                                     test_size=0.33)

# define the classifier that we will use
model = RandomForestClassifier()

# train the model
history = model.fit(X_train, y_train)

# obtain the score for the trained data
result = model.score(X_train, y_train)
print('Train Score: %s' % result)

# obtain the score for the test data
result = model.score(X_test, y_test)
print('Test Score: %s' % result)

# now, let's predict
prediction = model.predict(X_test)

print('Predictions:')
print(prediction)

# obtain the accuracy of the predictions
N = len(y_test)
print('Accuracy:')
print(np.sum(prediction == y_test) / N)

conf_mat = confusion_matrix(y_test, prediction, labels=[0, 1])
print(conf_mat)

plt.figure(figsize = (10,7))
seaborn.heatmap(conf_mat, annot=True)
plt.show()




