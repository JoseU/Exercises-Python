
import tweepy
import json
import time

# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = 'j6xiio1x6d8HBwy9OopSHuKcN'
consumer_secret = 'rjIhseK7cgrXMCWQyVFcjItKvTWl4UWTDAazwYyGDVxViZRX1K'
access_token = '197481156-OufHbI2EdEp32mF9rQGCftl9pcFbiWrmKWyWGEAe'
access_token_secret = 'MXjqQaUCGXtwFZImYh4JYaPUPORGIkM6FUVxRHah5VCYw'

# This is the listener, resposible for receiving data


class StdOutListener(tweepy.StreamListener):

    def __init__(self):
        time.sleep(4)
        

    def on_data(self, data):

        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        #print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        #print ''
        decoded_2 = decoded['text'].encode('ascii', 'ignore')
        return decoded_2
        return True

    def on_error(self, status):
        print status


l = StdOutListener()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

print "Mostrando todos los tweets para #ea5:"

    # There are different kinds of streams: public stream, user stream, multi-user streams
    # In this example follow #programming tag
    # For more details refer to https://dev.twitter.com/docs/streaming-apis
stream = tweepy.Stream(auth, l)


texto = stream.filter(track=['#ea5'])
print texto








 	