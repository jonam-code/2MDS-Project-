from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re   

data = pd.read_excel(r"./filename",engine='openpyxl')

data['Tweets'] = data['Tweets'].astype('str')
data['stemmed_tweets'] = data['stemmed_tweets'].astype('str')


#Calculating Subjectivity and Polarity 
def getSubjectivity(text):
   return TextBlob(text).sentiment.subjectivity
def getPolarity(text):
   return  TextBlob(text).sentiment.polarity

# Applying Subjectivity and Polarity over tweets
data['Subjectivity'] = data['Tweets'].apply(getSubjectivity)
data['Polarity'] = data['Tweets'].apply(getPolarity)

# Applying Subjectivity and Polarity over stemmed_tweet
data['Subjectivity_st'] = data['stemmed_tweets'].apply(getSubjectivity)
data['Polarity_st'] = data['stemmed_tweets'].apply(getPolarity)
df = data

# Score for Sentiments based on Polarity rate
def getAnalysis(score):
  if score < 0:
    return 'Negative'
  elif score == 0:
    return 'Neutral'
  else:
    return 'Positive'
    
df['Analysis'] = df['Polarity'].apply(getAnalysis)

# Calculating positive percentage
ptweets = df[df.Analysis == 'Positive']
ptweets = ptweets['Tweets']
print(round( (ptweets.shape[0] / df.shape[0]) * 100 , 1))

# Calculating negative percentage
ntweets = df[df.Analysis == 'Negative']
ntweets = ntweets['stemmed_tweets']
print(round( (ntweets.shape[0] / df.shape[0]) * 100, 1))

# Calculating neutral percentage 
neutweets = df[df.Analysis == 'Neutral']
neutweets = neutweets['Tweets']
print(round( (neutweets.shape[0] / df.shape[0]) * 100, 1))

# Positive Tweets Word Cloud
allWords = ' '.join([twts for twts in ptweets])
wordCloud = WordCloud(background_color = "white",width=500, height=300, random_state=21, max_font_size=110).generate(allWords)
plt.imshow(wordCloud, interpolation="bilinear")
plt.axis('off')
plt.show()

# Positive Tweets Word Cloud

allWords = ' '.join([twts for twts in ptweets])
wordCloud = WordCloud(background_color = "white",width=500, height=300, random_state=21, max_font_size=110).generate(allWords)
plt.imshow(wordCloud, interpolation="bilinear")
plt.axis('off')
plt.show()


# Neutral Tweets Word Cloud
allWords = ' '.join([twts for twts in neutweets])
wordCloud = WordCloud(background_color = "white",width=500, height=300, random_state=21, max_font_size=110).generate(allWords)
plt.imshow(wordCloud, interpolation="bilinear")
plt.axis('off')
plt.show()