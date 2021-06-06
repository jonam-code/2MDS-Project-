import tweepy
import GetOldTweets3
from textblob import TextBlob
import pandas as pd
import numpy as np
import re
import os
import string
import matplotlib.pyplot as plt


data = pd.read_excel("TN2021.xlsx" ,engine='openpyxl')

# Removing #,@ RT and hyperlink
def cleanTxt(text):
 text = re.sub('@[A-Za-z0–9]+', '', text) #Removing @mentions
 text = re.sub('#', '', text) # Removing '#' hash tag
 text = re.sub('RT[\s]+', '', text) # Removing RT
 text = re.sub('https?:\/\/\S+', '', text) # Removing hyperlink
  
 return text

df['Tweets'] = df['Tweets'].apply(cleanTxt)

# Removing all kind of emoji 
def remove_emojis(text):
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f" 
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', text)

data['Tweets'] = data['Tweets'].apply(remove_emojis)

# Converting to lowercase
data['Tweets'] = data['Tweets'].str.lower()

# Removing Stopwords
from stop_words import get_stop_words
stop_words = get_stop_words('en')
data['Tweets'] = data['Tweets'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))

#Removing punctuations
data['Tweets'] = data['Tweets'].str.replace('[^\w\s]','')

# Some punctuations wasnt removed with regex so we use string module to remove the punctuations
def remove_punctuations(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    return text

data['Tweets'] = data['Tweets'].apply(remove_punctuations)


# removing numbers
from string import digits
data['Tweets'] = data['Tweets'].str.replace('\d+', '')

# removing non english
import nltk
words = set(nltk.corpus.words.words())
data['Tweets'] = [" ".join(w for w in nltk.wordpunct_tokenize(x) 
                       if w.lower() in words or not w.isalpha()) 
                       for x in data['Tweets']]


# Writing to Excel
data.to_excel("file_name.xlsx")