from pydoc import cli
import tweepy
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
import re
import time
from collections import defaultdict

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


info_text = []

class TweetStreamer(tweepy.StreamingClient):
    def __init__(self, client, time_limit=60):
        super(TweetStreamer, self).__init__(bearer_token)
        self.start_time = time.time()
        self.limit = time_limit
        # super(StdOutListener, self).__init__()
        self.num_tweets = 0
        self.flag = False

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
        info_text.append(tweet.text)
        self.flag = True
        return
        # print("/" * 100)

    def add_search_terms(self, search_terms):
        if not (self.get_rules()[0] is None):
            self.delete_rules(self.get_rules()[0])

        for term in search_terms:
            self.add_rules(tweepy.StreamRule(term))

    def on_response(self, response):
        if self.flag is True:
            return

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


    # text = "this is  good"
    # polarityAsFloat = TextBlob(text).sentiment.polarity

    # store tweets in this class
    def __init__(self, all_tweets) -> None:
        self.tweets = []

        for tweet in all_tweets:
            self.tweets.append(tweet)
        # print(self.tweets)

    '''
    obtain the noun frequencies across all tweets passed to this class
    returns pandas dataframe with the columns 'noun' and 'freq' for the noun and frequency of each word
    sorted in descending order of frequency
    '''
    def get_noun_frequencies(self): 

        nounFrequencies = defaultdict(int)

        for tweet in self.tweets:
            for (word, partOfSpeech) in TextBlob(tweet).pos_tags: # PoS tags for a single tweet 
                if partOfSpeech[0] == 'N' and not (word == "@"): # nouns that aren't usernames 
                    nounFrequencies[word] += 1

        noun_df = pd.DataFrame.from_dict(nounFrequencies, orient='index', columns=['freq'])
        noun_df = noun_df.sort_values(['freq'], ascending=False)
        noun_df.reset_index(inplace=True)
        noun_df.rename(columns={'index': 'noun'}, inplace=True)
        
        return noun_df

    '''
    use textblob to calculate the polarity and subjectivity of each individual tweet
    returns a dataframe with each row showing the sentiment for one tweet
    '''
    def get_sentiment(self): 
        
        sentiments = dict() 
        for tweet in self.tweets: 
            polarity = TextBlob(tweet).sentiment.polarity
            subjectivity = TextBlob(tweet).sentiment.subjectivity

            sentiments[tweet] = [polarity, subjectivity]
        
        sentiment_df = pd.DataFrame.from_dict(sentiments, orient='index', columns=['polarity', 'subjectivity'])
        print(sentiment_df.head(10))
        sentiment_df.reset_index(inplace=True)
        sentiment_df.rename(columns={'index': 'tweet_text'}, inplace=True)
        return sentiment_df


class DataVisualiser:

    # def __init__(self, tweets) -> None:
    #     self.tweets = tweets
    #     self.csv_file = noun_freqs

    
    # def __init__(self, noun_freqs) -> None:
    #     self.noun_df = noun_freqs

    def plot_figure(self, noun_df):
        # pie chart from nouns
        noun_top = noun_df.head(10)
        
        def func(pct):
            return "{:1.1f}%".format(pct)
        plt.pie(noun_top['freq'], labels = noun_top['noun'], autopct=lambda pct: func(pct))


        # live graph of tweet sentiments (for specific search term)
        # x axis time, y axis polarity
        plt.plot(noun_top['noun'], noun_top['freq'])
        

        # scatter graph (different colours)
        #scvData = pd.read_csv(csv_file)
        #df = pd.DataFrame(scvData)

        #plt.scatter(noun_df['Subjectivity'], noun_df['Polarity'])
        plt.show()


if __name__ == '__main__':
    bearer_token = open("BearerToken.txt").read()
    search_terms = "les"
    # real time information
    while info_text is not None:
        streamer = TweetStreamer(bearer_token, 2)
        streamer.add_search_terms(search_terms)
        streamer.filter(expansions="author_id",tweet_fields="created_at")  # starts streaming

    dc = DataClean(tweets)

    da = DataAnalysis(dc.texts)
    noun_freqs = da.get_noun_frequencies()

    dv = DataVisualiser()
    dv.plot_figure(noun_freqs)

    sentiments = da.get_sentiment()
    print(sentiments)

