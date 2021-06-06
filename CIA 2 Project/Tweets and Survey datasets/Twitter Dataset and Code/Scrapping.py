import tweepy
import GetOldTweets3
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

# Twitter Developer Access Keys to access the tweepy.API
consumerKey = '******************************'
consumerSecret = '********************************'
accessToken = '****************************************'
accessTokeSecret = '****************************************'
authenticate = tweepy.OAuthHandler(consumerKey, consumerSecret) 
authenticate.set_access_token(accessToken, accessTokeSecret)
api = tweepy.API(authenticate, wait_on_rate_limit = True)

 # Cursor to fetch tweets based on Hashtag(#).
 n = input("Enter the number of tweets to be fetched:")
 tweets = tweepy.Cursor(api.search,
            q="TamilNaduElection2021",
            lang="en",
            exclude = 'retweets',
            tweet_mode='extended',
            since="2021-03-31",
            untill = "2021-04-05").items(n)

# Storing the tweets in a dataframe
df = pd.DataFrame([[tweet.user.screen_name, tweet.user.location,tweet.full_text] for tweet in tweets], columns=['user', "location",'Tweets'])

df.to_excel("file_name.xlsx")