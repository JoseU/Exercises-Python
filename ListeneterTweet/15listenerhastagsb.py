#Import the necessary methods from tweepy library

import tweepy
import json

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = 'nNrwY4QrkV2Tsa8VCixSiD7HN'
consumer_secret = 's0Bmobvmb8NnwJEqyQIpH0jV7zC3vpQDp2TULJxTqLgPSdVBiC'
access_token = '197481156-OufHbI2EdEp32mF9rQGCftl9pcFbiWrmKWyWGEAe'
access_token_secret = 'MXjqQaUCGXtwFZImYh4JYaPUPORGIkM6FUVxRHah5VCYw'



# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        print ''
        countB = 0
        countB += 1
        print(countB)
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    print "Showing all new tweets for #ea5:"

    # There are different kinds of streams: public stream, user stream, multi-user streams
    # In this example follow #programming tag
    # For more details refer to https://dev.twitter.com/docs/streaming-apis
    stream = tweepy.Stream(auth, l)
    stream.filter(track=['#ea5'])

 	