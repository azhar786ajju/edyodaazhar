#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# # Dataset link :
# Url = https://raw.githubusercontent.com/SR1608/Datasets/main/coviddata.csv

# # 1. Import the dataset using Pandas from above mentioned url.

# In[2]:


df = pd.read_csv('https://raw.githubusercontent.com/SR1608/Datasets/main/covid-data.csv')
df.head()


# # 2. High Level Data Understanding:

# # a. Find no. of rows & columns in the dataset

# In[3]:


df.shape


# # b. Data types of columns.
# 

# In[4]:


df.dtypes


# # c. Info & describe of data in dataframe.

# In[5]:


df.info()


# In[6]:


df.describe()


# # 3. Low Level Data Understanding :

# # a. Find count of unique values in location column.

# In[7]:


df['location'].nunique()


# # b. Find which continent has maximum frequency using values counts.

# In[9]:


df['continent'].value_counts()


# # c. Find maximum & mean value in 'total_cases'.

# In[10]:


# maximum value in 'total_cases'
df['total_cases'].max()


# In[11]:


#mean value in 'total_cases'
df['total_cases'].mean()


# # d. Find 25%,50% & 75% quartile value in 'total_deaths'.

# In[12]:


df['total_deaths'].describe()


# In[13]:


# 25% quartile value in 'total_deaths'

df.total_deaths.quantile(0.25)


# In[14]:


# 50% quartile value in 'total_deaths'

df.total_deaths.quantile(0.5)


# In[15]:


# 75% quartile value in 'total_deaths'

df.total_deaths.quantile(0.75)


# # e. Find which continent has maximum 'human_development_index'.

# In[16]:


df.groupby('continent')['human_development_index'].max('human_development_index').reset_index(name = 'human_development_index')

# Hence Europe has maximum 'human_development_index'.


# In[17]:


# checking which continent has maximum 'human_development_index', max value will returns True

df.groupby('continent')['human_development_index'].max() == max(df['human_development_index'])

# Europe returns True


# # f. Find which continent has minimum 'gdp_per_capita'.

# In[18]:


df.groupby('continent')['gdp_per_capita'].min()

# Hence Africa has minimum 'gdp_per_capita'


# In[19]:


# checking which continent has minimum 'gdp_per_capita'. min value will returns True

df.groupby('continent')['gdp_per_capita'].min() == min(df['gdp_per_capita'])

# Africa returns True


# # 4. Filter the dataframe with only this columns
# 
# ['continent','location','date','total_cases','total_deaths','gdp_per_capita','human_development_index'] 
# and update the data frame.

# In[20]:


df_filtered = df[['continent','location','date','total_cases','total_deaths','gdp_per_capita','human_development_index']]


# In[21]:


df_filtered


# # 5. Data Cleaning

# # a. Remove all duplicates observations

# In[8]:


df.drop_duplicates


# # b. Find missing values in all columns
# 

# In[9]:


df.isnull().sum().reset_index(name = "missing values")


# # C. Remove all observations where continent column value is missing
#  Tip : using subset parameter in dropna

# In[10]:



df.dropna(subset = ['continent'])
df.head()


# # d. Fill all missing values with 0

# In[11]:


df.fillna(0, inplace=True)
df.head()


# # 6. Date time format 

# # a. Convert date column in datetime format using pandas.to_datetime

# In[26]:


# Creating columns by converting the date column into a datetime format
df['date'] = pd.to_datetime(df['date'])
df.dtypes


# # b. Create new column month after extracting month data from date column.

# In[27]:


df['Month'] = pd.DatetimeIndex(df['date']).month
df.head()


# # 7. Data Aggregation:

# # a. Find max value in all columns using groupby function on 'continent' column
#         Tip: use reset_index() after applying groupby

# In[13]:


result = df.groupby("continent").max('continent').reset_index()
result


# # b. Store the result in a new dataframe named 'df_groupby'.

# In[14]:


df_groupby = result
df_groupby


# # 8. Feature Engineering :

# # a. Create a new feature 'total_deaths_to_total_cases' by ratio of 'total_deaths' column to 'total_cases'
# 

# In[30]:


df['total_deaths_to_total_cases'] = df['total_deaths']/df['total_cases']


# In[31]:


df['total_deaths_to_total_cases']


# # 9. Data Visualization :

# # a. Perform Univariate analysis on 'gdp_per_capita' column by plotting histogram using seaborn dist plot.

# In[23]:


# IMPORTING LIBRARIES

import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[33]:


# Univariate analysis on 'gdp_per_capita' column by plotting histogram using seaborn dist plot

sns.distplot(df["gdp_per_capita"],color='darkorange') 


# In[34]:


# histogram plot

sns.histplot(df["gdp_per_capita"],color='darkorange') 


# In[36]:


# displot
np.random.seed(7)
gdp_per_capita = np.random.randn(700)
gdp_per_capita = pd.Series(gdp_per_capita, name = 'gdp_per_capita')

# Histogram Plot
sns.distplot(gdp_per_capita, kde = False)


# # b. Plot a scatter plot of 'total_cases' & 'gdp_per_capita'

# In[37]:


# scatter plot of 'total_cases' & 'gdp_per_capita'

x = df['gdp_per_capita']
y = df['total_cases']

# Set the fugure size in inches
plt.figure(figsize = (8,6))

plt.scatter(x, y, label = 'Points', c = 'red')
plt.xlabel('gdp_per_capita')
plt.ylabel('total_cases')
plt.title('Scatter Plot')
plt.legend()
plt.show()


# # c. Plot Pairplot on df_groupby dataset.

# In[ ]:


# Pair plot
# coolwarm : color coding scheme
sns.pairplot(df, hue = df_groupby, palette = 'coolwarm')


# In[ ]:


sns.pairplot(df_groupby, hue ='size')


# # d. Plot a bar plot of 'continent' column with 'total_cases' .
#  Tip : using kind='bar' in seaborn catplot

# In[ ]:


sns.barplot(x = 'continent', y = 'total_cases', data = ['continent','total_cases'], hue = 'class')


# # 10.Save the df_groupby dataframe in your local drive using pandas.to_csv function .

# In[19]:


df_groupby.to_csv()

