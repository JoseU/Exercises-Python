
import RPi.GPIO as GPIO    #Importamos la libreria RPi.GPIO

import tweepy
import json
import time

# Raspberry Comunication

GPIO.setmode(GPIO.BOARD)   #Ponemos la Raspberry en modo BOARD

# set up GPIO output channel
GPIO.setup(12, GPIO.OUT) #Para usar el PWM

GPIO.setup(13, GPIO.OUT) #Para controlar 
GPIO.setup(11, GPIO.OUT)





GPIO.setup(21,GPIO.OUT)    #Ponemos el pin 21 como salida
p = GPIO.PWM(21,50)        #Ponemos el pin 21 en modo PWM i enviamos 50 senales por segundo
p.start(7.5)               #Enviamos un pulso del 7.5% para centrar el servo

# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = 'Dnr9OK64SlYUJDQ7QjCFVL4HQ'
consumer_secret = '42tTaW7FA9JcR5605Es2oKYBOlqCw1MN43Q4fhWfDjXg744MKi'
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
            print prueba1

            stringIzq = "#ea5 Izquierda"  
            stringDer = "#ea5 Derecha"  
            stringStop = "#ea5 Stop"    

            if prueba1 == stringIzq :
                print 'Izquierda'
                GPIO.output(13, GPIO.LOW)
                GPIO.output(11, GPIO.LOW)

            elif prueba1 == stringDer :   
                print 'Derecha'         
                GPIO.output(13, GPIO.HIGH)
                GPIO.output(11, GPIO.LOW)

            elif prueba1 == stringStop :
                print 'Stop' 
                GPIO.output(13, GPIO.LOW)
                GPIO.output(11, GPIO.LOW)



        """  ciclos raspeberry
        if self.contador == 0 :
            p.ChangeDutyCycle(7.5) 
            print "primer ciclo"
            time.sleep(5)
        elif self.contador == 1 :
            p.ChangeDutyCycle(4.5)
            print "segundo ciclo" 
            time.sleep(5)
        elif self.contador == 2:
            p.ChangeDutyCycle(10.5) 
            print "tercer ciclo"
            time.sleep(5)
        elif self.contador == 3:
            p.ChangeDutyCycle(7.5)
            print "cuarto ciclo"
            time.sleep(5) """
        
        
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







 	
