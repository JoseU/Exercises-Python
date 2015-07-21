#!/usr/bin/python
from pyfirmata import nano, util
import tweepy
import json
import time

# para buscar el puerto ls /dev/tty.* || ls /dev/ttyUS*
# 5pwm      6   7       8 luz1
# 9pwm      10 11       12 luz2
# setting arduino nano
board = nano('/dev/ttyUSB0')
pin5 = board.get_pin('d:5:p')
pin9 = board.get_pin('d:9:p')


# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = 'QI1FdMAtp5nabO7Hyb3OatfUu'
consumer_secret = 'dYqie8GQg3J2rtHE8l1jc0wRRKOuDeNTiIhaRuK7UHTf8rNhf6'
access_token = '197481156-OufHbI2EdEp32mF9rQGCftl9pcFbiWrmKWyWGEAe'
access_token_secret = 'MXjqQaUCGXtwFZImYh4JYaPUPORGIkM6FUVxRHah5VCYw'


# This is the listener, resposible for receiving data
if __name__ == '__main__':

    try : 

        def rampaMotor1 (rampa_) : 
            rampaLen = len(rampa_)
            pwm = 0
            delay = 0
            for x in xrange(0,rampaLen):

                #encendido de luz 1
                if x == 0 : 
                    board.digital[8].write(1)
                #apagado de luz 1 con delay
                    
                elif x == (rampaLen - 1) :
                    time.sleep(rampa_[rampaLen-1] + 0.2)
                    board.digital[8].write(0)

                if x%2 == 0 :
                    pwm = rampa_[x]
                    pin5.write(pwm)
                    
                elif x%2 == 1 :
                    time.sleep(rampa_[x])
                    delay = rampa_[x]
                print "|MAQUINA TIERRA| pwm = ", pwm, "time = ", delay

        def rampaMotor2 (rampa_) : 
            rampaLen = len(rampa_)
            pwm = 0
            delay = 0
            for x in xrange(0,rampaLen):
                
                #encendido de luz 2
                if x == 0 :
                    board.digital[12].write(1)

                #apagado de luz 2 con delay
                elif x == (rampaLen - 1) :
                    time.sleep(rampa_[rampaLen-1] + 0.2)
                    board.digital[12].write(0)

                if x%2 == 0 :
                    pwm = rampa_[x]
                    pin9.write(pwm)
                    
                elif x%2 == 1 :
                    time.sleep(rampa_[x])
                    delay = rampa_[x]
                print "|MAQUINA AGUA| pwm = ", pwm, "time = ", delay

                # encendido de luz 2

        def maquinaRaices(sentido):

            if sentido in ['izq'] :
                board.digital[6].write(1)
                board.digital[7].write(0)
            elif sentido in ['der'] : 
                board.digital[6].write(0)
                board.digital[7].write(1)   

            elif sentido in ['parar'] :
                pin5.write(0)
                board.digital[6].write(0)
                board.digital[7].write(0)
                board.digital[8].write(0)   

        def maquinaAgua(sentido):

            if sentido in ['izq'] :
                board.digital[10].write(1)
                board.digital[11].write(0)
            elif sentido in ['der'] : 
                board.digital[10].write(0)
                board.digital[11].write(1)  

            elif sentido in ['parar'] : 
                pin9.write(0)
                board.digital[10].write(0)
                board.digital[11].write(0)
                board.digital[12].write(0)  


        class StdOutListener1(tweepy.StreamListener):

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

                    if prueba1.find('raices') != -1 : #prender motor 1, defecha 50% PWM
                        maquinaRaices("izq")
                        rampa1 = [0.2, 1.1, 0.1, 0.5, 0.17, 0.8, 0.21, 0.1, 0, 0.1]
                        rampaMotor1(rampa1)  
                  
                    elif prueba1.find('agua') != -1 :
                        maquinaAgua("izq")
                        rampa2 = [0.5, 1.1, 0.3, 1.5, 0.1, 1.5, 0.2, 1, 0, 1]
                        rampaMotor2(rampa2)

                    else :
                        print "No entiendo tu tweet"
                        maquinaAgua("parar")
                        maquinaRaices("parar")
                
                return True


            def on_error(self, status):
                print status

        class StdOutListener2(tweepy.StreamListener):

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

                    if prueba1.find('raices') != -1 : #prender motor 1, defecha 50% PWM
                        maquinaRaices("izq")
                        rampa1 = [0.2, 1.1, 0.1, 0.5, 0.17, 0.8, 0.21, 0.1, 0, 0.1]
                        rampaMotor1(rampa1)  
                  
                    elif prueba1.find('agua') != -1 :
                        maquinaAgua("izq")
                        rampa2 = [0.5, 1.1, 0.3, 1.5, 0.1, 1.5, 0.2, 1, 0, 1]
                        rampaMotor2(rampa2)

                    else :
                        print "No entiendo tu tweet"
                        maquinaAgua("parar")
                        maquinaRaices("parar")
                
                return True


            def on_error(self, status):
                print status
           

        l1 = StdOutListener1()
        l2 = StdOutListener2()

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        print "Mostrando todos los tweets para #ea5:"

            # There are different kinds of streams: public stream, user stream, multi-user streams
            # In this example follow #programming tag
            # For more details refer to https://dev.twitter.com/docs/streaming-apis
        stream1 = tweepy.Stream(auth, l1)
        stream1.filter(track=['#ea5'])

        stream2 = tweepy.Stream(auth, l2)
        stream2.filter(track=['#ea5'])



    except KeyboardInterrupt:
        print "Interrupted"
        maquinaAgua("parar")
        maquinaRaices("parar")







 	
