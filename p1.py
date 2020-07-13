
#!/usr/bin/env python
# coding: utf-8
from lepara import *
# In[1]:


import pandas as pd


# In[2]:


dataset = pd.read_csv('Churn_Modelling.csv')


# In[3]:


dataset.columns


# In[4]:


y = dataset['Exited']


# In[ ]:





# In[5]:


X = dataset[['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
       'IsActiveMember', 'EstimatedSalary']]


# In[6]:


geo = dataset['Geography']


# In[7]:


geo = pd.get_dummies(geo, drop_first=True )


# In[8]:


gender = dataset['Gender']


# In[9]:


gender = pd.get_dummies(gender, drop_first=True )


# In[10]:


X = pd.concat([X,gender,geo], axis=1)


# In[11]:


X.info()


# In[12]:


from keras.optimizers import Adam


# In[13]:


# X.isnull()


# In[14]:


from keras import metrics


# In[15]:


from sklearn.model_selection import train_test_split


# In[16]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)


# In[17]:


from keras.models import Sequential


# In[18]:


model = Sequential()


# In[19]:


from keras.layers import Dense


# In[20]:


model.add(Dense(units=6, input_dim=11, activation='relu' ))


# In[21]:


#model.add(Dense(units=6, activation='relu'))


# In[22]:


#model.add(Dense(units=6, activation='relu'))


# In[23]:


model.add(Dense(units=1,  activation='sigmoid' ))


# In[24]:


model.compile(optimizer=Adam(learning_rate=ler_para),loss='binary_crossentropy', metrics=['accuracy'] )


# In[25]:


history=model.fit(X_train,y_train , epochs=50 , verbose=0)


# In[26]:


model.fit(X_train,y_train , epochs=100 , verbose=0)


# In[27]:


df_loss = pd.DataFrame(model.history.history)


# In[28]:


#df_loss.plot()


# In[29]:


accuracy_variable=history.history['accuracy'][9]

import os
os.environ['ACCR']=str(accuracy_variable)  

#os.system("ACCR= {0}".format(str(accuracy_variable)))
print(accuracy_variable)

