
# ******* Importing OSC libraries ********

import OSC




# ******************************************

# ****** Importing RPi.GPIO library ********
import RPi.GPIO as GPIO    
import tweepy
import json
import time, random

# Raspberry Comunication

GPIO.setmode(GPIO.BOARD)   #Ponemos la Raspberry en modo BOARD

# set up GPIO output channel
GPIO.setup(12, GPIO.OUT) #Para usar el PWM

GPIO.setup(13, GPIO.OUT) #Para controlar 
GPIO.setup(15, GPIO.OUT)

GPIO.setup(11, GPIO.OUT) #Para controlar la luz
GPIO.setup(16, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)



p = GPIO.PWM(12,50)        #Ponemos el pin 21 en modo PWM i enviamos 50 senales por segundo
                            #Enviamos un pulso del 7.5% para centrar el servo

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
        self.osc_msg = ""
        

    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        self.prueba = '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        self.prueba1= decoded['text'].encode('ascii', 'ignore')
        
        self.osc_msg = self.prueba1
        

        if self.prueba1 != "" :

            print self.prueba1

            self.contador += 1
            counterMod = self.contador % 5
            print counterMod
            
            client = OSC.OSCClient()
            client.connect( ('172.16.162.169', 9000) ) # note that the argument is a tupple and not two arguments
            msg = OSC.OSCMessage() #  we reuse the same variable msg used above overwriting it
            msg.setAddress("/print")
            msg.append(self.prueba1)
            client.send(msg) # now we dont need to tell the client the address anymore
              

            if counterMod == 1 :
                GPIO.output(13, GPIO.LOW)
                GPIO.output(15, GPIO.HIGH)
                GPIO.output(11, GPIO.LOW) # configurar en un sentido la luz
                GPIO.output(16, GPIO.HIGH)
                GPIO.output(22, GPIO.HIGH)
                p.start(38.0) #control Pwm
                time.sleep(0.4)
                GPIO.output(13, GPIO.HIGH)
                GPIO.output(15, GPIO.LOW)
                p.start(45.0)
                time.sleep(0.2) 
                GPIO.output(13, GPIO.LOW)
                GPIO.output(15, GPIO.LOW) 
                GPIO.output(11, GPIO.LOW)
                GPIO.output(16, GPIO.LOW)
                GPIO.output(22, GPIO.LOW)
            

            elif counterMod == 2 : 
                GPIO.output(13, GPIO.LOW)
                GPIO.output(15, GPIO.HIGH)
                GPIO.output(11, GPIO.LOW) # configurar en un sentido la luz
                GPIO.output(16, GPIO.HIGH)
                GPIO.output(22, GPIO.HIGH)
                p.start(43.0) #control Pwm
                time.sleep(0.1)
                GPIO.output(13, GPIO.HIGH)
                GPIO.output(15, GPIO.LOW)
                time.sleep(0.2) 
                GPIO.output(13, GPIO.LOW)
                GPIO.output(15, GPIO.LOW)

                # otro 
                GPIO.output(13, GPIO.LOW)
                GPIO.output(15, GPIO.HIGH)
                p.start(44.0) #control Pwm
                time.sleep(0.08)
                p.start(40.0)
                GPIO.output(13, GPIO.HIGH)
                GPIO.output(15, GPIO.LOW)
                time.sleep(0.2) 
                GPIO.output(13, GPIO.LOW)
                GPIO.output(15, GPIO.LOW)
                GPIO.output(11, GPIO.LOW)
                GPIO.output(16, GPIO.LOW)
                GPIO.output(22, GPIO.LOW)

            elif counterMod == 3 : 
                GPIO.output(13, GPIO.HIGH)
                GPIO.output(15, GPIO.LOW)
                GPIO.output(11, GPIO.LOW) # configurar en un sentido la luz
                GPIO.output(16, GPIO.HIGH)
                GPIO.output(22, GPIO.HIGH)
                time.sleep(0.75)
                GPIO.output(13, GPIO.LOW)
                GPIO.output(15, GPIO.HIGH)
                p.start(44.0) #control Pwm
                time.sleep(0.1)
                GPIO.output(13, GPIO.HIGH)
                GPIO.output(15, GPIO.LOW)
                time.sleep(0.05)  
                GPIO.output(13, GPIO.LOW)
                GPIO.output(15, GPIO.LOW)
                time.sleep(0.05) 
                GPIO.output(13, GPIO.LOW)
                GPIO.output(15, GPIO.HIGH)
                time.sleep(0.54)
                GPIO.output(13, GPIO.LOW)
                GPIO.output(15, GPIO.LOW)
                GPIO.output(11, GPIO.LOW)
                GPIO.output(16, GPIO.LOW)
                GPIO.output(22, GPIO.LOW)


            elif counterMod == 4 : 
                GPIO.output(13, GPIO.LOW)
                GPIO.output(15, GPIO.HIGH)
                GPIO.output(11, GPIO.LOW) # configurar en un sentido la luz
                GPIO.output(16, GPIO.HIGH)
                GPIO.output(22, GPIO.HIGH)
                p.start(60.0) #control Pwm
                time.sleep(0.1)
                GPIO.output(13, GPIO.HIGH)
                GPIO.output(15, GPIO.LOW)
                time.sleep(0.8)  
                GPIO.output(13, GPIO.LOW)
                GPIO.output(15, GPIO.HIGH)
                p.start(40.0)
                time.sleep(0.3) 
                GPIO.output(13, GPIO.LOW)
                GPIO.output(15, GPIO.LOW)
                GPIO.output(11, GPIO.LOW)
                GPIO.output(16, GPIO.LOW)
                GPIO.output(22, GPIO.LOW)

            elif counterMod == 5 : 
                GPIO.output(13, GPIO.LOW)
                GPIO.output(15, GPIO.HIGH)
                GPIO.output(11, GPIO.LOW) # configurar en un sentido la luz
                GPIO.output(16, GPIO.HIGH)
                GPIO.output(22, GPIO.HIGH)
                p.start(34.0) #control Pwm
                time.sleep(0.67)
                p.start(43.0)
                GPIO.output(13, GPIO.HIGH)
                GPIO.output(15, GPIO.LOW)
                time.sleep(0.8) 
                GPIO.output(13, GPIO.LOW)
                GPIO.output(15, GPIO.LOW) 
                time.sleep(0.03) 
                GPIO.output(13, GPIO.LOW)
                GPIO.output(15, GPIO.HIGH)
                p.start(33.0)
                time.sleep(3.45) 
                GPIO.output(13, GPIO.LOW)
                GPIO.output(15, GPIO.LOW)
                GPIO.output(11, GPIO.LOW)
                GPIO.output(16, GPIO.LOW)
                GPIO.output(22, GPIO.LOW)


       
        
        return True # Steps for each Tweet
    
    def clean_GPIO (self) :
        if KeyboardInterrupt :         #Si el usuario pulsa CONTROL+C entonces...
            p.stop()                      #Detenemos el servo 
            GPIO.cleanup()                #Limpiamos los pines GPIO de la Raspberry y cerramos el script
    #def osc_sending(self) :
    
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







 	
