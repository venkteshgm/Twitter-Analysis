#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import pickle
import nltk
import os


# In[2]:


#classifier built in phase 2
model_path="F://twitter_100000.model"
classifier=pickle.load(open(model_path,"rb"))


# In[5]:


#just in case word_features didn't get pickled
negative_tweets=pd.read_csv('C://Users/venkteshpc/Downloads/neg_twt_res.csv')
positive_tweets=pd.read_csv('C://Users/venkteshpc/Downloads/pos_twt_res.csv')
neg_twt_list=list(negative_tweets['is upset that he can\'t update his Facebook by texting it and might cry as a result  School today also Blah'])
pos_twt_list=list(positive_tweets['I LOVE @Health4UandPets u guys r the best!! '])
neg_twt=list(neg_twt_list[:100000])
pos_twt=list(pos_twt_list[:100000])
tweets=[]
test_tweets=[]
def create_list_of_tweets_split(tweet_array,sentiment):
    for words in tweet_array:
        words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
        tweets.append((words_filtered, sentiment))
create_list_of_tweets_split(pos_twt,'positive')
create_list_of_tweets_split(neg_twt,'negative')
def get_words_in_tweets(tweets):
    all_words=[]
    for (words,sentiment) in tweets:
        all_words.extend(words)
    return all_words
def get_word_features(wordlist):
    wordlist=nltk.FreqDist(wordlist)
    word_features=wordlist.keys()
    return word_features
word_features=get_word_features(get_words_in_tweets(tweets))
def extract_features(document):
    document_words=set(document)
    features={}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


# In[3]:


#list of words
word_features=pickle.load(open("F://word_features.txt","rb"))


# In[4]:


#to label whether a word exists within sample tweet or not
def extract_features(document):
    document_words=set(document)
    features={}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


# In[5]:


tweet='I had been to lucy\'s place and it was horrific! bodies strewn across the floor!'
classifier.classify(extract_features(tweet.split()))


# In[5]:


if not os.path.exists('secret_twitter_credentials.pkl'):
    Twitter={}
    Twitter['Consumer Key'] = 'JXbxf7ZvBmZqCX2dV95rL0awU'
    Twitter['Consumer Secret'] = 'yljFWsDwbIaJsokXad7Nt4KjcikL8z1yHYRTe3kXJd8pCDrHOq'
    Twitter['Access Token'] = '3166795783-hjxdXZuyHbx3vgKk3OEsX61rhmZ6uyojIJjs3Ex'
    Twitter['Access Token Secret'] = 'xaK9isiXbNyjnWc3qqmoCz9CRpgtYQBnLsQ4vhUYt0bK8'
    with open('secret_twitter_credentials.pkl','wb') as f:
        pickle.dump(Twitter, f)
else:
    Twitter=pickle.load(open('secret_twitter_credentials.pkl','rb'))


# In[6]:


import twitter

auth = twitter.oauth.OAuth(Twitter['Access Token'],
                           Twitter['Access Token Secret'],
                           Twitter['Consumer Key'],
                           Twitter['Consumer Secret'])

twitter_api = twitter.Twitter(auth=auth)

# Nothing to see by displaying twitter_api except that it's now a
# defined variable

print(twitter_api)


# In[7]:


def search_using_keywords(keywords,count):
    return twitter_api.search.tweets(q=keywords, count=count)


# In[64]:


search_results=search_using_keywords('#venom',100)
statuses=search_results['statuses']


# In[65]:


#filtering out duplicate tweets
all_text = []
filtered_statuses = []
for s in statuses:
    if not s["text"] in all_text:
        filtered_statuses.append(s)
        all_text.append(s["text"])
statuses = filtered_statuses


# In[62]:


text=statuses[1]['text']


# In[21]:


#building a word filter
import string
useless_words = nltk.corpus.stopwords.words("english") + list(string.punctuation)


# In[16]:


text=str(text)


# In[26]:


text2=((text.strip(string.punctuation)).replace('.','')).strip(string.punctuation)


# In[76]:


classifier.classify(extract_features(statuses[1]['text'].split()))


# In[81]:


abc=[]


# In[66]:


#fiiltered text semantic pushed into abc array
for i in statuses:
    abc.append(classifier.classify(extract_features(filter(i['text']).split())))


# In[50]:


def filter(text):
    return text.strip(string.punctuation).replace('.','')


# In[84]:


count=0
for i in abc:
    if(i=='positive'):
        count=count+1


# In[85]:


count


# In[82]:


for i in statuses:
    abc.append(classifier.classify(extract_features(i['text'].split())))


# In[91]:


statuses[8]['text']


# In[86]:


abc


# In[80]:


len(statuses)


# In[92]:


46/61


# In[ ]:




