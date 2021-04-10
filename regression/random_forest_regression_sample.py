# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 21:32:30 2021

@author: Jordi Corbilla
"""
from __future__ import print_function, division
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# load the dataset
df = pd.read_csv('C:/Users/thund/Source/Repos/natural-language-processing/regression/data/airfoil_self_noise.dat', 
                 sep='\t', 
                 header=None)

# show the first few values
print(df.head())
print(df.info())

# output
#       0    1       2     3         4        5
# 0   800  0.0  0.3048  71.3  0.002663  126.201
# 1  1000  0.0  0.3048  71.3  0.002663  125.201
# 2  1250  0.0  0.3048  71.3  0.002663  125.951
# 3  1600  0.0  0.3048  71.3  0.002663  127.591
# 4  2000  0.0  0.3048  71.3  0.002663  127.461

# 0 to 4 is the data, 5 is the target

data = df[[0, 1, 2, 3, 4]].values
target = df[5].values

# Learning component
# split the data 1/3 of it will be for training
X_train, X_test, y_train, y_test = train_test_split(data,
                                                    target,
                                                    test_size=0.33)

# define the classifier that we will use
model = RandomForestRegressor()

# train the model
model.fit(X_train, y_train)

# obtain the score for the trained data (this is R^2, better closer to 1)
result = model.score(X_train, y_train)
print('Train Score: %s' % result)

# obtain the score for the test data (this is R^2, better closer to 1)
result = model.score(X_test, y_test)
print('Test Score: %s' % result)

# now, let's predict
prediction = model.predict(X_test)

print('Predictions:')
print(prediction)
