#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import sys

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



if len(sys.argv) > 1:
    line_generator = open(sys.argv[1])
else:
    line_generator = sys.stdin

for stream in line_generator:
    line_object = json.loads(stream)
    try:
        actor_id_string = line_object["text"]["id"]
        actor_id = int( actor_id_string.split(":")[2] )
        language_code = line_object["twitter_lang"]
    excepy KeyError, e:
        actor_id = -1
        language_code = "Null"
    print_string = "{0:12d}, {1:2s}".format(actor_id,language_code)
    print(print_string)

