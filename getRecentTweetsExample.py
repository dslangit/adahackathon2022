import tweepy

if __name__ == '__main__':

    bearer_token = open("BearerToken.txt").read()

    client = tweepy.Client(bearer_token)
    search_query = "(#BorisJohnson) -is:retweet"
    tweets = client.search_recent_tweets(query=search_query,max_results=25)     #returns Response Object

    for tweet in tweets[0]:     #Tweets are stored in the zeroth element of the Response Object
        print(str(tweet.id)+": " +str(tweet.text) + "\n")
        print("/" * 100 + "\n")