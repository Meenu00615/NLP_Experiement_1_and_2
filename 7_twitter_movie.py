# -*- coding: utf-8 -*-
"""10_Twitter.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1T72TAQ8aisrfW5QzwDN9FUah49dY_Bzm

#7: Sentiment Analysis: Twitter dataset

##Training and validataion
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords
#/content/twitter_training.csv

df_train = pd.read_csv('/content/twitter_training.csv', header = None)

df_train.head()

df_train.columns = ['ID', 'Category', 'Sentiment', 'Text']

df_train.columns

df_test = pd.read_csv('/content/twitter_validation.csv', header = None)

df_test.head()

df_test.columns = ['ID', 'Category', 'Sentiment', 'Text']

df_test.columns

df_train.isnull().sum()

df_test.isnull().sum()

df_train = df_train.dropna()

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def remove_html_tags(text):
    soup = BeautifulSoup(text, 'html.parser')
    return soup.get_text()

def remove_symbols(text):
    pattern = r'[^A-Za-z\s]'
    text = re.sub(pattern, '', text)
    text = ' '.join([word for word in text.split() if word.lower() not in stop_words])
    return text

# Clean text column
df_train['Text'] = df_train['Text'].apply(lambda x: remove_html_tags(x))
df_train['Text'] = df_train['Text'].apply(lambda x: remove_symbols(x))

df_test['Text'] = df_test['Text'].apply(lambda x: remove_html_tags(x))
df_test['Text'] = df_test['Text'].apply(lambda x: remove_symbols(x))

X_train = df_train['Text']
y_train = df_train.Sentiment

X_test = df_test['Text']
y_test = df_test.Sentiment

tfidf_vectorizer = TfidfVectorizer(stop_words = 'english', max_df = 0.7)

tfidf_train = tfidf_vectorizer.fit_transform(X_train)
tfidf_test = tfidf_vectorizer.transform(X_test)

pac = PassiveAggressiveClassifier(max_iter = 50)
pac.fit(tfidf_train, y_train)

y_pred = pac.predict(tfidf_test)
score = accuracy_score(y_test, y_pred)

print(f'Acc: {round(score*100, 2)}%')

confusion_matrix(y_test, y_pred, labels = ['Neutral', 'Positive', 'Negative'])

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
labels = ['Neutral', 'Positive', 'Negative']
cm = confusion_matrix(y_test, y_pred, labels=labels)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()