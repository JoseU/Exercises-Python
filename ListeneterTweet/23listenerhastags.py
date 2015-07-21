# Librerias para OSC
import argparse
from pythonosc import osc_message_builder
from pythonosc import udp_client

# Librerias de Tweepy y Json para mapear
import tweepy
import json
import time

# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = 'StC5OvWsNhd53O7bt7Xof41MK'
consumer_secret = 'ylU8z2KwXv4ILkYpYLWSci6OtDzWEyWyyTkpJphZUJTIJyZwsP'
access_token = '197481156-OufHbI2EdEp32mF9rQGCftl9pcFbiWrmKWyWGEAe'
access_token_secret = 'MXjqQaUCGXtwFZImYh4JYaPUPORGIkM6FUVxRHah5VCYw'


# This is the listener, resposible for receiving data


class StdOutListener(tweepy.StreamListener):

    def __init__(self):
        time.sleep(4)
        self.contador =0
        

    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        prueba = '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        prueba1= decoded['text'].encode('ascii', 'ignore')
        if prueba1!="":
           self.contador+=1
        
 
        print (self.contador)
        return True

    def on_error(self, status):
        print (status)

    def osc_data (self) :
        # Inicializando ips 
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", default="127.0.0.1",
             help="The ip of the OSC server")
        parser.add_argument("--port", type=int, default=8000,
             help="The port the OSC server is listening on")
        args = parser.parse_args()

        client = udp_client.UDPClient(args.ip, args.port)
       
        msg = osc_message_builder.OscMessageBuilder(address = "/tecla")
        msg.add_arg(3)
        msg = msg.build()
        client.send(msg)

   
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








 	