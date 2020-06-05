#!/usr/bin/env python
# coding: utf-8
from parameters import *
import pandas as pd
dataset = pd.read_csv('Churn_Modelling.csv')
#dataset.columns
y = dataset['Exited']
X = dataset[['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
       'IsActiveMember', 'EstimatedSalary']]
geo = dataset['Geography']

geo = pd.get_dummies(geo, drop_first=True )

gender = dataset['Gender']

gender = pd.get_dummies(gender, drop_first=True )
X = pd.concat([X,gender,geo], axis=1)
#X.info()
from keras.optimizers import Adam
from keras import metrics
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
from keras.models import Sequential
from keras.layers import Dense

import tensorflow as tf
tf.get_logger().setLevel('ERROR')
tf.autograph.set_verbosity(0)


# In[19]:
model =Sequential()

model.add(Dense(units=6, input_dim=11, activation='relu' ))


# In[20]:


model.add(Dense(units=3, activation='relu'))
#model.add(Dense(units=2, activation='relu'))
#model.add(Dense(units=2,  activation='relu' ))
model.add(Dense(units=1,  activation='relu' ))

model.compile(optimizer=Adam(learning_rate=var_lr),loss='binary_crossentropy',metrics=['accuracy'])

#model.summary()
history=model.fit(X_train,y_train , epochs=50 , verbose=0) #aresok


# In[38]:


accuracy_variable=history.history['accuracy'][9]

import os
os.environ['ACCR']=str(accuracy_variable)  
#os.system("ACCR= {0}".format(str(accuracy_variable)))
print(accuracy_variable)

