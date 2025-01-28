#!/usr/bin/env python
# coding: utf-8

# # Create bar chart or histogram to visualize the distribution of categorical or continuous variable 

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


df = sns.load_dataset('penguins')
df.head(5)


# In[8]:


df.info()


# In[10]:


df.duplicated().sum()


# In[12]:


df.columns.duplicated()


# In[14]:


df.isna().sum()


# In[16]:


numerical = df.select_dtypes(include='number')
numerical.head(5)


# In[18]:


for col in numerical:
    numerical[col] = numerical[col].fillna(numerical[col].median())

numerical


# In[20]:


categorical = df.select_dtypes(include='object')


# In[22]:


for col in categorical:
  categorical[col] = categorical[col].fillna(categorical[col].mode()[0])

categorical


# In[24]:


df = pd.concat([numerical, categorical], axis=1)
df.head()


# In[28]:


df.isna().sum()


# In[94]:


sns.countplot(x='species', data=df, palette='viridis', hue='species', legend=True)
plt.xlabel("Species")
plt.ylabel("Count")
plt.title("No. of different species", style='oblique')
plt.show()


# In[92]:


sns.countplot(x='sex', data=df, palette='coolwarm', hue='sex', legend=True)
plt.xlabel("Sex")
plt.ylabel("Count")
plt.title("No. of males and females", style='oblique')
plt.show()


# In[88]:


sns.countplot(x='island', data=df, palette='viridis', hue='island', legend=True)
plt.xlabel("Island")
plt.ylabel("Count")
plt.title("No. of different islands", style='oblique')
plt.show()


# In[90]:


sns.countplot(x='species', data=df, palette='BrBG', hue='sex', legend=True)
plt.xlabel("Species")
plt.ylabel("Count")
plt.title("No. of males and females in different species", style='oblique')
plt.show()


# In[86]:


sns.countplot(x='island', data=df, palette='Spectral', hue='species', legend=True)
plt.xlabel("Island")
plt.ylabel("count")
plt.title("No. of species in different islands", style='oblique')
plt.show()


# In[46]:


plt.hist(categorical, color=['red','green','blue'],rwidth=5,density=False, cumulative=False)
plt.show()


# In[ ]:




