#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import nltk
import pickle


# In[2]:


negative_tweets=pd.read_csv('C://Users/venkteshpc/Downloads/neg_twt_res.csv')
positive_tweets=pd.read_csv('C://Users/venkteshpc/Downloads/pos_twt_res.csv')


# In[6]:


negative_tweets.columns


# In[34]:


positive_tweets.columns


# In[3]:


neg_twt_list=list(negative_tweets['is upset that he can\'t update his Facebook by texting it and might cry as a result  School today also Blah'])
pos_twt_list=list(positive_tweets['I LOVE @Health4UandPets u guys r the best!! '])


# In[4]:


neg_twt=list(neg_twt_list[:100000])
pos_twt=list(pos_twt_list[:100000])


# In[6]:


len(neg_twt)


# In[5]:


tweets=[]
test_tweets=[]


# In[6]:


def create_list_of_tweets_split(tweet_array,sentiment):
    for words in tweet_array:
        words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
        tweets.append((words_filtered, sentiment))


# In[7]:


def create_list_of_test_tweets_split(tweet_array,sentiment):
    for words in tweet_array:
        words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
        test_tweets.append((words_filtered, sentiment))


# In[8]:


#creating "tweets" array of tweets to train the machine on
create_list_of_tweets_split(pos_twt,'positive')
create_list_of_tweets_split(neg_twt,'negative')


# In[9]:


#creating test tweets array
create_list_of_test_tweets_split(pos_twt[100000:100500],'positive')
create_list_of_test_tweets_split(neg_twt[100000:100500],'negative')


# In[10]:


#to add all the words in the tweet[] list into one linear array
def get_words_in_tweets(tweets):
    all_words=[]
    for (words,sentiment) in tweets:
        all_words.extend(words)
    return all_words


# In[11]:


#to take the array of words,plot frequncy of occurence of words and arrange them in decreasing order of occurence
def get_word_features(wordlist):
    wordlist=nltk.FreqDist(wordlist)
    word_features=wordlist.keys()
    return word_features


# In[12]:


word_features=get_word_features(get_words_in_tweets(tweets))


# In[70]:


#to save word_features wordlist for later use
word_features_list=[]
for i in word_features:
    word_features_list.append(i)
pickle.dump(word_features_list,open("F://word_features.txt", "wb"))


# In[13]:


#to label whether a word exists within sample tweet or not
def extract_features(document):
    document_words=set(document)
    features={}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


# In[14]:


#to create a training set
training_set = nltk.classify.apply_features(extract_features, tweets)
#train the classifier on the training set
classifier = nltk.NaiveBayesClassifier.train(training_set)


# In[16]:


#pickling the classifier for future use
import pickle
model_path="F://twitter_100000.model"
pickle.dump(classifier,open(model_path,"wb"))


# <h2>tests</h2>

# In[17]:


tweet='hello good friend'
classifier.classify(extract_features(tweet.split()))


# In[18]:


tweet='I had been to lucy\'s place and it was horrific! bodies strewn across the floor!'
classifier.classify(extract_features(tweet.split()))


# In[19]:


tweet='fuck you'
classifier.classify(extract_features(tweet.split()))


# In[53]:


for i in range(0,100):
    pos_chk.append(classifier.classify(extract_features(pos_twt_list[100000+i].split())))


# In[54]:


for i in range(0,100):
    neg_chk.append(classifier.classify(extract_features(neg_twt_list[100000+i].split())))


# In[52]:


pos_chk=[]
neg_chk=[]
count=0


# In[55]:


#positive tweets check:100 tweets used
count=0
for i in pos_chk:
    if i=='positive':
        count=count+1
print(count)


# In[56]:


#negative tweets check:100 tweets used
count=0
for i in neg_chk:
    if i=='negative':
        count=count+1
print(count)


# In[64]:


abc=[]


# In[65]:


for i in word_features:
    abc.append(i)


# In[ ]:




