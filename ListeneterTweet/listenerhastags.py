from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key = 'O82viv9gqRgStE2FKzPswFDH0'
consumer_secret = 'wr78xh1jgVB01k7yJTY14yPuzfyo8QDXr4IKEBes8BdiSWnbcl'
access_token = '197481156-OufHbI2EdEp32mF9rQGCftl9pcFbiWrmKWyWGEAe'
access_token_secret = 'MXjqQaUCGXtwFZImYh4JYaPUPORGIkM6FUVxRHah5VCYw'

class listener(StreamListener):

   def on_data(self, data):

        jsonData = json.loads(data)
        text = jsonData['text']
        text2 = jsonData['entities']['hashtags']
        for hashtag in text2:
             text2 = hashtag['text']
        print text + str(text2)
        return True

    def on_error(self, status):
        print status

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitterStream = Stream(auth, listener())
twitterStream.filter(follow=[23], track=["#ea5"])



