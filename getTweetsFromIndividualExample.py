import tweepy


if __name__ == '__main__':
    bearer_token = open("BearerToken.txt").read()
    client = tweepy.Client(bearer_token)

    tweets = client.get_users_tweets(id="117777690", end_time="2021-06-25T00:00:40Z", max_results=30)
    for tweet in tweets[0]:
        print(tweet.text)