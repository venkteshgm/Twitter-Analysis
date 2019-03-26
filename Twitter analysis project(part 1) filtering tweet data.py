#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import nltk


# In[2]:


data=pd.read_csv("C:/Users/venkteshpc/Downloads/twitter-analysis.csv",encoding='cp1252')


# In[3]:


data.columns=['target','id','date','flag','user','text']
features=['target','id','text']
filtered_data=data[features]
filtered_data=pd.DataFrame(filtered_data)


# In[4]:


negative_tweets=pd.DataFrame(filtered_data['text'][:799999])
positive_tweets=pd.DataFrame(filtered_data['text'][799999:])


# In[5]:


neg_twt=negative_tweets['text']
pos_twt=positive_tweets['text']


# In[16]:


pos_twt=list(pos_twt)
pos_twt=pd.Series(pos_twt)


# In[6]:


import string
import nltk
useless_words = nltk.corpus.stopwords.words("english") + list(string.punctuation)


# In[7]:


type(string.punctuation)


# In[42]:


neg_twt[0]


# In[24]:


neg_twt_filtered=pd.Series()
pos_twt_filtered=pd.Series()


# In[22]:


a=''.join([i for i in neg_twt[0] if not i in string.punctuation])


# In[23]:


a


# In[ ]:


for i in range(0,len(neg_twt)):
    neg_twt[i]=''.join([j for j in neg_twt[i] if not j in string.punctuation])


# In[26]:


string.punctuation


# In[27]:


neg_twt[0]


# In[13]:


neg_twt[0].strip(string.punctuation)


# In[15]:


neg_twt[1].strip(string.punctuation)


# In[16]:


neg_twt[1]


# In[20]:


(neg_twt[0].strip(string.punctuation)).replace('.','')


# In[9]:


for i in range(0,799998):
    neg_twt[i]=(neg_twt[i].strip(string.punctuation)).replace('.','')


# In[7]:


type(neg_twt)


# In[10]:


neg_twt.to_csv("C://Users/venkteshpc/Downloads/neg_twt_res.csv",index=False, header=False)


# In[8]:


len(neg_twt)


# In[18]:


for i in range(0,799998):
    pos_twt[i]=(pos_twt[i].strip(string.punctuation)).replace('.','')


# In[19]:


pos_twt.to_csv("C://Users/venkteshpc/Downloads/pos_twt_res.csv",index=False, header=False)


# In[23]:


pos_twt_csv=pd.read_csv('C://Users/venkteshpc/Downloads/pos_twt_res.csv')


# In[2]:


data1=pd.read_csv('C://Users/venkteshpc/Downloads/pos_twt_res.csv')


# In[8]:


dat


# In[ ]:




