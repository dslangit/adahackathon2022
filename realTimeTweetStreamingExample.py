import tweepy
import time


class MyTweepyStreamer(tweepy.StreamingClient):
    def on_connect(self):
        print("Connected successfully")

    def on_tweet(self, tweet):
        print(tweet.text)
        print("/" * 100)
        time.sleep(0.5)

    def add_search_terms(self, search_terms):
        if not (self.get_rules()[0] is None):
            self.delete_rules(self.get_rules()[0])

        for term in search_terms:
            self.add_rules(tweepy.StreamRule(term))

if __name__ == '__main__':
    bearer_token = open("BearerToken.txt").read()
    streamer = MyTweepyStreamer(bearer_token=bearer_token)
    search_terms = ["Iran", "#Ukraine"]

    streamer.add_search_terms(search_terms)
    streamer.filter()  # starts streaming