from pydoc import cli
import tweepy
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
import re
import time


class TweetCollector:
    def __init__(self, client) -> None:
        self.client = client

    def get_recent_tweets(self, search_query, max_res):
        tweets = client.search_recent_tweets(query=search_query, max_results=max_res)
        return tweets

    def get_users_tweets(self, id, start_time, end_time):
        tweets = client.get_users_tweets(id=id, end_time=end_time, start_time=start_time)
        return tweets

    def on_connect(self):
        print("TweetCollector Connected successfully")


class TweetStreamer(tweepy.StreamingClient):
    def __init__(self, client, time_limit=60):
        super(TweetStreamer, self).__init__(bearer_token)
        self.start_time = time.time()
        self.limit = time_limit
        # super(StdOutListener, self).__init__()
        self.num_tweets = 0

    # def on_status(self, status):
    #     # record = {'Text': status.text, 'Created At': status.created_at}
    #     # print(record)  # See Tweepy documentation to learn how to access other fields
    #     self.num_tweets += 1
    #     if self.num_tweets < 20:
    #         # collection.insert(record)
    #         return True
    #     else:
    #         return False

    def on_connect(self):
        print("TweetStreamer Connected successfully")

    def on_tweet(self, tweet):
        print(tweet.text)
        # print("/" * 100)

    def add_search_terms(self, search_terms):
        if not (self.get_rules()[0] is None):
            self.delete_rules(self.get_rules()[0])

        for term in search_terms:
            self.add_rules(tweepy.StreamRule(term))

    # Read in tweets


# should each class talk to the csv file
# e.g. DataClean creates new @BorisJohnsonCleanData.csv

# or should DataAnalysis request from DataClean which requests from TweetCollector


class DataClean:
    # Strip text of special characters
    def __init__(self, tweets) -> None:
        self.tweets = tweets
        self.texts=[]
        self.ids=[]
        for tweet in self.tweets[0]:
            post=tweet.text
            post=re.sub(r'http://\S+ ', '', post)
            post = re.sub(r'http://\S+\n', '', post)
            post = re.sub(r'http://\S+', '', post)
            post = re.sub(r'https://\S+ ', '', post)
            post = re.sub(r'https://\S+\n', '', post)
            post = re.sub(r'https://\S+', '', post)
            post = re.sub(r'www\.\S+\.com', '', post)
            self.texts.append(post)
            self.ids.append(tweet.id)


    #test the class
    def test(self):
        for tweet in self.tweets[0]:
            print(str(tweet.text))


class DataAnalysis:
    # Perform sentiment (polarity and subjectivity) analysis on data

    text = "this is  good"
    polarityAsFloat = TextBlob(text).sentiment.polarity

    # Tweet, Polarity, Subjectivity


class DataVisualiser:

    def __init__(self, tweets, csv_file) -> None:
        self.tweets = tweets
        self.csv_file = csv_file

    def plot_figure(self):
        # pie chart from nouns
        # nounFrequencies as pie chart, maybe only take top ten nouns.

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

        # live graph of tweet sentiments (for specific search term)
        # x axis time, y axis polarity

        # scatter graph (different colours)
        scvData = pd.read_csv(csv_file)
        df = pd.DataFrame(scvData)

        plt.scatter(df['Subjectivity'], df['Polarity'])
        plt.show()


if __name__ == '__main__':
    bearer_token = open("BearerToken.txt").read()
    client = tweepy.Client(bearer_token)

    # history information
    tc = TweetCollector(client)
    tc.on_connect()
    search_query = "gender minority"
    tweets = tc.get_recent_tweets(search_query, 100)
    # real time information
    streamer = TweetStreamer(bearer_token, 2)
    search_terms = ["gender minority"]

    streamer.add_search_terms(search_terms)
    streamer.filter(expansions="author_id",tweet_fields="created_at")  # starts streaming
    exit()
