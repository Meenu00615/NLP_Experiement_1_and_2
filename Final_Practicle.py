#!/usr/bin/env python
# coding: utf-8

# In[2]:


import nltk
nltk.download('punkt')


# In[4]:


nltk.download('wordnet')


# In[18]:


import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter

with open('Opp_story.txt', 'r') as file:
    text = file.read()

#Tokenization
word_tokens = word_tokenize(text)
sent_tokens = sent_tokenize(text)

#POS Tagging
pos_tags = nltk.pos_tag(word_tokens)

#Initialize stemmer and lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

#Stemming
stemmed_tokens = [stemmer.stem(token) for token in word_tokens]

#Lemmatization
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in word_tokens]

#Frequency analysis
word_freq = Counter(word_tokens)

#Download stopwords list
nltk.download('stopwords')

#Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in word_tokens if token.lower() not in stop_words]


# In[19]:


print("Word Tokens:", word_tokens)   


# In[20]:


print("\nSentence Tokens:", sent_tokens)


# In[21]:


print("\nPOS Tags:", pos_tags)


# In[22]:


print("\nStemmed Tokens:", stemmed_tokens)


# In[23]:


print("\nLemmatized Tokens:", lemmatized_tokens)


# In[24]:


print("\nWord Frequency:", word_freq)


# In[25]:


print("\nFiltered Tokens (Without Stopwords):", filtered_tokens)

