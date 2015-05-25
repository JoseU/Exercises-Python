
import tweepy
import json
import time

# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = '9Hpa5kfxYkKOPfrqQqUK3e5Fp'
consumer_secret = 'KIWF9uchUP4GRtx9apluiY8Xv9HjpEyQFVUGTP3aXxwkEZ6VRd'
access_token = '197481156-OufHbI2EdEp32mF9rQGCftl9pcFbiWrmKWyWGEAe'
access_token_secret = 'MXjqQaUCGXtwFZImYh4JYaPUPORGIkM6FUVxRHah5VCYw'

# This is the listener, resposible for receiving data
dataText = {}

class StdOutListener(tweepy.StreamListener):

    def __init__(self):
        time.sleep(4)
        

    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        #print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        #print ''
        return True

    def on_error(self, status):
        print status
    def return_Ttext(self) : # to return only the text from  tweets
        tweet_text_full = decoded['text'].encode('ascii', 'ignore')
        return tweet_text_full

l = StdOutListener()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

print "Mostrando todos los tweets para #ea5:"

    # There are different kinds of streams: public stream, user stream, multi-user streams
    # In this example follow #programming tag
    # For more details refer to https://dev.twitter.com/docs/streaming-apis
stream = tweepy.Stream(auth, l)
stream.filter(track=['#ea5'])

print l.return_Ttext() 






 	