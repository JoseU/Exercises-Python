
import RPi.GPIO as GPIO    #Importamos la libreria RPi.GPIO

import tweepy
import json
import time

# Raspberry Comunication

GPIO.setmode(GPIO.BOARD)   #Ponemos la Raspberry en modo BOARD
GPIO.setup(21,GPIO.OUT)    #Ponemos el pin 21 como salida
p = GPIO.PWM(21,50)        #Ponemos el pin 21 en modo PWM i enviamos 50 senales por segundo
p.start(7.5)               #Enviamos un pulso del 7.5% para centrar el servo

# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = 'u1tnIUk5TGXBNP7YytcSuW970'
consumer_secret = 'HwSoaw0HPu1FMCh9gjpqy14a1C7n6ItHUC2hQI2xkY5BYbNU3y'
access_token = '197481156-OufHbI2EdEp32mF9rQGCftl9pcFbiWrmKWyWGEAe'
access_token_secret = 'MXjqQaUCGXtwFZImYh4JYaPUPORGIkM6FUVxRHah5VCYw'


# This is the listener, resposible for receiving data


class StdOutListener(tweepy.StreamListener):

    def __init__(self):
        time.sleep(4)
        self.contador = 0
        

    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        prueba = '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        prueba1= decoded['text'].encode('ascii', 'ignore')
        if prueba1 != "" :
           self.contador += 1

           # ciclos raspeberry
        if self.contador == 0 :
            p.ChangeDutyCycle(7.5) 
            print "primer ciclo"
        elif self.contador == 1 :
            p.ChangeDutyCycle(4.5)
            print "segundo ciclo" 
        elif self.contador == 2:
            p.ChangeDutyCycle(10.5) 
            print "tercer ciclo"
        elif self.contador == 3:
            p.ChangeDutyCycle(7.5)
            print "cuarto ciclo"
        
        print prueba
        self.contador = self.contador % 4
        print self.contador
        return True
    
    def clean_GPIO (self) :
        if KeyboardInterrupt :         #Si el usuario pulsa CONTROL+C entonces...
            p.stop()                      #Detenemos el servo 
            GPIO.cleanup()                #Limpiamos los pines GPIO de la Raspberry y cerramos el script

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







 	