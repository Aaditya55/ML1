#!/usr/bin/env python
# coding: utf-8

from lepara import *
import pandas as pd
dataset = pd.read_csv('Churn_Modelling.csv')

y = dataset['Exited']
X = dataset[['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
       'IsActiveMember', 'EstimatedSalary']]

geo = dataset['Geography']
geo = pd.get_dummies(geo, drop_first=True )
gender = dataset['Gender']
gender = pd.get_dummies(gender, drop_first=True )
X = pd.concat([X,gender,geo], axis=1)
X.info()
from keras.optimizers import Adam
# X.isnull()
from keras import metrics

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

from keras.models import Sequential
model = Sequential()
from keras.layers import Dense
model.add(Dense(units=6, input_dim=11, activation='relu' ))
model.add(Dense(units=6, activation='relu'))
#model.add(Dense(units=6, activation='relu'))
model.add(Dense(units=1,  activation='sigmoid' ))
model.compile(optimizer=Adam(learning_rate=0.000001),loss='binary_crossentropy' )
model.fit(X_train,y_train , epochs=200 , verbose=0)
df_loss = pd.DataFrame(model.history.history)

accuracy_var=history.history['accuracy'][9]

import os
os.environ['ACCR']=str(accuracy_var)  

os.system("ACCR= {0}".format(str(accuracy_var)))
print(accuracy_var)
