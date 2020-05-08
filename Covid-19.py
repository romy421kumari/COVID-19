
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


file=pd.read_csv('population_india_census2011.csv')
file.head()


# In[3]:


file['Percentage of Rural population in state']=((file['Rural population'])/(file['Population']))*100
file['Percentage of Urban population in state']=((file['Urban population'])/(file['Population']))*100
file.head(13)


# In[4]:


max(file['Population'])


# In[5]:


print("Maximun Gender ratio : ", file[file['Gender Ratio']==max(file['Gender Ratio'])]['State / Union Territory'])


# In[6]:


urban=file[['State / Union Territory','Percentage of Urban population in state']]
urban.head()


# In[7]:


x=[]
y=[]
label=[]
for i in file['State / Union Territory']:
    label.append(i)
for i in file['Percentage of Urban population in state']:
    y.append(i)
for i in range(36):
    x.append(i)
plt.xticks(x,label) 
plt.plot(x,y)
plt.show()


# In[8]:


file1=pd.read_csv('StatewiseTestingDetails.csv')
file1.head()


# In[9]:


file1[file1['Negative']==max(file1['Negative'])][['State','Date']]


# In[10]:


file1[file1['Positive']==max(file1['Positive'])][['State','Date']]


# In[11]:


file1['Ratio negative']=file1['Negative']/file1['TotalSamples']
file1.head()


# In[12]:


file1['Ratio positive']=file1['Positive']/file1['TotalSamples']
file1.head()


# In[13]:


print("Maximum negative ratio: ", max(file1['Ratio negative']))
print("Maximum positive ratio: ", max(file1['Ratio positive']))
file1.shape

