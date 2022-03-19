#!/usr/bin/env python
# coding: utf-8

# # Import the necessary libraries

# In[106]:


import numpy as np
import pandas as pd


# # Assign it to a variable called users and use the 'user_id' as index

# In[107]:


users = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user',sep = '|').set_index('user_id')
users


# # See the first 10 and last 10 entries

# In[108]:


users.head(10),user.tail(10)


# # What is the number of observations in the dataset?

# In[109]:


# Getting number of Obseervations
print('Number of Observations : ', users.shape[0])


# # What is the number of columns in the dataset?

# In[110]:


# Getting no of the columns in Dataset
print('Number of columns  : ', users.shape[1])


# # Print the name of all the columns.

# In[111]:


print(users.keys())


# In[112]:


user.columns


# # How is the dataset indexed?

# In[113]:


users.index


# # What is the data type of each column?

# In[114]:


users.dtypes


# # Print only the occupation column

# In[115]:


print(users.occupation)


# # How many different occupations are in this dataset?

# In[122]:


print(users['occupation'].nunique())


# In[117]:


users["occupation"].value_counts().count()


# # What is the most frequent occupation?

# In[118]:


users['occupation'].value_counts()
users['occupation'].mode()


# # DataFrame Info.

# In[119]:


user.info(verbose=True)


# # Describe all the columns

# In[120]:


users.describe(include='all')  


# # Summarize only the occupation column
# 

# In[158]:


users.groupby('occupation').occupation.count()


# # What is the mean age of users?

# In[123]:


users['age'].mean()


# # What is the age with least occurrence?

# In[125]:


users['age'].value_counts().idxmin()

