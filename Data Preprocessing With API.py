#!/usr/bin/env python
# coding: utf-8

# # Application Programming Interface (API)

# API stands for Application Programming Interface. In the context of APIs, the word Application refers to any software with a distinct function. Interface can be thought of as a contract of service between two applications. This contract defines how the two communicate with each other using requests and responses. Their API documentation contains information on how developers are to structure those requests and responses.

# # Data Pipeline

# In[1]:


import pandas as pd
import requests


# In[2]:


response = requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page=1')


# In[9]:


response.json()


# In[10]:


response.json()['results']


# In[11]:


pd.DataFrame(response.json()['results'])


# In[14]:


df=pd.DataFrame(response.json()['results'])[['id','title','overview','release_date','popularity','vote_average','vote_count']]


# In[15]:


df.head()


# # Create Empty DataFrame

# In[16]:


df = pd.DataFrame()


# In[17]:


df


# In[18]:


for i in range(1,429):
    response = requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page={}'.format(i))
    temp_df = pd.DataFrame(response.json()['results'])[['id','title','overview','release_date','popularity','vote_average','vote_count']]
    df = df.append(temp_df,ignore_index=True)


# In[19]:


df


# In[20]:


df.shape


# # Change DataFrame to CSV Files

# In[21]:


df.to_csv('movies.csv')


# In[ ]:




