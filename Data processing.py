#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


# In[2]:


# Loading the dataset
df = pd.read_csv('diabetes.csv')


# In[3]:


df.head()


# In[4]:


# no of rows and colums 


# In[5]:


df.shape


# In[6]:


df.isnull().sum()


# In[7]:


df.describe()


# In[8]:


#spearating the features and target


# In[9]:


X = df.drop(columns='Outcome', axis = 1)
Y = df['Outcome']


# In[11]:


print(X)


# In[12]:


print(Y)


# # 0 -->> non - Diabetic
# 
# 

# # 1 -->> Diabetic

# In[13]:


# Data Standization


# In[14]:


scaler = StandardScaler()


# In[17]:


standardized_data=scaler.fit_transform(X)


# In[18]:


print(standardized_data)


# In[19]:


X =  standardized_data


# In[20]:


print(X
    )


# In[21]:


# Split it into test and train 


# In[22]:


X_train , X_test, Y_train , Y_test = train_test_split(X , Y , test_size = 0.2 , random_state =2              )


# In[23]:


print(X.shape, X_train.shape, X_test.shape)


# In[ ]:




