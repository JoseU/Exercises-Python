#OSC library
import argparse

#OSC library
from pythonosc import osc_message_builder
from pythonosc import udp_client
#OSC library

#Tweepy libraries

import tweepy
import json
import time

# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = 'Dnr9OK64SlYUJDQ7QjCFVL4HQ'
consumer_secret = '42tTaW7FA9JcR5605Es2oKYBOlqCw1MN43Q4fhWfDjXg744MKi'
access_token = '197481156-OufHbI2EdEp32mF9rQGCftl9pcFbiWrmKWyWGEAe'
access_token_secret = 'MXjqQaUCGXtwFZImYh4JYaPUPORGIkM6FUVxRHah5VCYw'

parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="127.0.0.1",
    help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=8001,
    help="The port the OSC server is listening on")
args = parser.parse_args()
client = udp_client.UDPClient(args.ip, args.port)


# This is the listener, resposible for receiving data


class StdOutListener(tweepy.StreamListener):

    def __init__(self):

        time.sleep(4)
        self.text = ''
        

    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        self.text = decoded['text'].encode('ascii', 'ignore')
             
        print (self.text)
        return True

    def on_error(self, status):
        print (status)

    def osc_messages(self) :
        
        msg = osc_message_builder.OscMessageBuilder(address = "/mesTweet")
        msg.add_arg(self.text)
        msg = msg.build()
        client.send(msg)
        print (msg)
        
   

if __name__ == "__main__": 
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    print ("Mostrando todos los tweets para #ea5:")

        # There are different kinds of streams: public stream, user stream, multi-user streams
        # In this example follow #programming tag
        # For more details refer to https://dev.twitter.com/docs/streaming-apis
    stream = tweepy.Stream(auth, l)
    stream.filter(track=['#ea5'])

    # Init OSC









 	