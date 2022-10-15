from pydoc import cli
import tweepy
from textblob import TextBlob
import pandas as pd
import matplotlib as plt

class TweetCollector:
    
    def __init__(self,client) -> None:
        self.client = client

    def get_recent_tweets(self,search_query,end_time,start_time):
        tweets = client.search_recent_tweets(query=search_query, max_results=100)

    def get_users_tweets(self,id,start_time,end_time):
        tweets = client.get_users_tweets(id=id,end_time=end_time,start_time=start_time)
    


    # Read in tweets


#should each class talk to the csv file
#e.g. DataClean creates new @BorisJohnsonCleanData.csv

# or should DataAnalysis request from DataClean which requests from TweetCollector


class DataClean:
    # Strip text of special characters
    pass

class DataAnalysis:
    # Perform sentiment (polarity and subjectivity) analysis on data

    text = "this is  good"
    polarityAsFloat = TextBlob(text).sentiment.polarity

    # Tweet, Polarity, Subjectivity

class DataVisualiser:
    #pie chart from nouns
    #nounFrequencies as pie chart, maybe only take top ten nouns.
    tweets = ["I love Boris."]

    allNouns = []
    for tweet in tweets:
        for (word, partOfSpeech) in TextBlob(tweet).pos_tags:
            if partOfSpeech[0] == 'N' and not (word == "@"):
                allNouns.append(word)

    nounFrequencies = {}
    for noun in allNouns:
        if noun in nounFrequencies:
            nounFrequencies[noun] += 1
        else:
            nounFrequencies[noun] = 1
    print(nounFrequencies)

    
    
    #live graph of tweet sentiments (for specific search term)
    # x axis time, y axis polarity

    #scatter graph (different colours)
    borisJohnsonData = pd.read_csv("@BorisJohnson.csv")
    keirStarmerData = pd.read_csv("@Keir_Starmer.csv")
    bdf = pd.DataFrame(borisJohnsonData)
    kdf = pd.DataFrame(keirStarmerData)

    plt.scatter(bdf['Subjectivity'], bdf['Polarity'])
    plt.scatter(kdf['Subjectivity'], kdf['Polarity'])

    plt.show()

