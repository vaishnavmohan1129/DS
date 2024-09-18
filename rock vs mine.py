#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# In[2]:


# loading the dataset


# In[8]:


sonar_data = pd.read_csv('sonar_data.csv', header = None)


# In[9]:


sonar_data.head()


# In[13]:


sonar_data[60].value_counts()


# In[10]:


sonar_data.shape


# In[11]:


sonar_data.describe()


# In[12]:


sonar_data.isnull().sum()


# In[14]:


sonar_data.groupby(60).mean()


# In[15]:


#seprating data and lable


# In[16]:


X = sonar_data.drop(columns = 60, axis= 1)
Y = sonar_data[60]


# In[17]:


print(X)
print(Y)


# In[18]:


#split the train and test data


# In[19]:


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, stratify=Y ,random_state=1)


# In[20]:


print(X.shape, X_train.shape)


# In[21]:


# Model training -- > LogisticRegression


# In[22]:


model = LogisticRegression()


# In[23]:


model.fit(X_train, Y_train)


# In[24]:


#Accuracy of the data


# In[28]:


X_train_preditcton = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_preditcton, Y_train)


# In[29]:


print('Accuracy on training data:',training_data_accuracy)


# In[32]:


X_test_preditcton = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_preditcton, Y_test)


# In[33]:


print('Accuracy on test data:',test_data_accuracy)


# In[34]:


#Predcative system


# In[44]:


input_data=(0.1313,0.2339,0.3059,0.4264,0.4010,0.1791,0.1853,0.0055,0.1929,0.2231,0.2907,0.2259,0.3136,0.3302,0.3660,0.3956,0.4386,0.4670,0.5255,0.3735,0.2243,0.1973,0.4337,0.6532,0.5070,0.2796,0.4163,0.5950,0.5242,0.4178,0.3714,0.2375,0.0863,0.1437,0.2896,0.4577,0.3725,0.3372,0.3803,0.4181,0.3603,0.2711,0.1653,0.1951,0.2811,0.2246,0.1921,0.1500,0.0665,0.0193,0.0156,0.0362,0.0210,0.0154,0.0180,0.0013,0.0106,0.0127,0.0178,0.0231)
input_data_numpy = np.asarray(input_data)
input_data_reshape= input_data_numpy.reshape(1,-1)
prdicit = model.predict(input_data_reshape)
print(prdicit)

if(prdicit[0]=='R'):
        print("Rock")
else:
        print("Mine")


# In[ ]:




