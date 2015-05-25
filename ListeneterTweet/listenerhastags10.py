#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pandas as pd

#Variables that contains the user credentials to access Twitter API 
access_token = "197481156-OufHbI2EdEp32mF9rQGCftl9pcFbiWrmKWyWGEAe"
access_token_secret = "MXjqQaUCGXtwFZImYh4JYaPUPORGIkM6FUVxRHah5VCYw"
consumer_key = "O82viv9gqRgStE2FKzPswFDH0"
consumer_secret = "wr78xh1jgVB01k7yJTY14yPuzfyo8QDXr4IKEBes8BdiSWnbcl"


class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['#ea5'])


tweets_data_path = '../Desktop/twitter_data.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
        
print len(tweets_data)