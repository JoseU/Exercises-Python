#!/usr/bin/python
from pyfirmata import nano, util
import tweepy
import json
import time


# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = 'QI1FdMAtp5nabO7Hyb3OatfUu'
consumer_secret = 'dYqie8GQg3J2rtHE8l1jc0wRRKOuDeNTiIhaRuK7UHTf8rNhf6'
access_token = '197481156-OufHbI2EdEp32mF9rQGCftl9pcFbiWrmKWyWGEAe'
access_token_secret = 'MXjqQaUCGXtwFZImYh4JYaPUPORGIkM6FUVxRHah5VCYw'


# This is the listener, resposible for receiving data
if __name__ == '__main__':

    try : 


        class StdOutListener(tweepy.StreamListener):

            def __init__(self):
                time.sleep(4)
                

            def on_data(self, data):
                # Twitter returns data in JSON format - we need to decode it first
                decoded = json.loads(data)

                # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
                prueba = '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
                prueba1= decoded['text'].encode('ascii', 'ignore')
                if prueba1 != "" :
                    print prueba1

                    if prueba1.find('raices') + prueba1.find('agua') <= 1 :

                        print "No entiendo tu tweet"

                    if prueba1.find('raices') != -1 : #prender motor 1, defecha 50% PWM
                        print "RAICES"

                  
                    if prueba1.find('agua') != -1 :
                        print "AGUA"

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
        stream.filter(track=['#ea5'])

    except KeyboardInterrupt:
        print "Interrupted"








 	
