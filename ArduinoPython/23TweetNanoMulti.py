#!/usr/bin/python
from pyfirmata import nano, util
import tweepy
import json
import time
import threading

# para buscar el puerto ls /dev/tty.* || ls /dev/ttyUS*
# 5pwm      6   7       8 luz1
# 9pwm      10 11       12 luz2
# setting arduino nano
"""board = nano('/dev/tty.usbserial-A400eMcd')
pin5 = board.get_pin('d:5:p')
pin9 = board.get_pin('d:9:p')

pin11 = board.get_pin('d:11:p')
pin3 = board.get_pin('d:3:p')"""

# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = 'FWwZ3f0LC2aOpzBUeE9Pbxp10'
consumer_secret = 'fei2g0ljpcSnnvB8gtzogHP6sV4sWnNsikp4ZCz9oAYhfeb5S8'
access_token = '197481156-OufHbI2EdEp32mF9rQGCftl9pcFbiWrmKWyWGEAe'
access_token_secret = 'MXjqQaUCGXtwFZImYh4JYaPUPORGIkM6FUVxRHah5VCYw'


class maquinaRaiz(object) : 
    ordCount = 0



    def __init__(self, sentido, rampa):

        self.rampa = rampa
        self.sentido = sentido

        maquinaRaiz.ordCount += 1
       
    def encender(self):

        if self.sentido in ['izq'] :
            #board.digital[6].write(1)
            #board.digital[7].write(0)

            print "Raiz izquierda"
        elif self.sentido in ['der'] : 
            #board.digital[6].write(0)
            #board.digital[7].write(1)   
            print "Raiz derecha"

        elif self.sentido in ['parar'] :
            #pin5.write(0)
            #board.digital[6].write(0)
            #board.digital[7].write(0)
            #board.digital[8].write(0) 
            print "Raiz parar"

    def linea (self) : 
        rampaLen = len(self.rampa )
        pwm = 0
        delay = 0


        
        for x in xrange(0,rampaLen):

            #encendido de luz 1
            if x == 0 : 

                #board.digital[8].write(1)
                #pin3.write(1.0)
                print "inicio de rampa "

            #apagado de luz 1 con delay
              
            elif x == (rampaLen - 1) :
                time.sleep(self.rampa [rampaLen-1] + 0.2)
                #board.digital[8].write(0)
                #pin3.write(0)

            if x%2 == 0 :
                pwm = self.rampa [x]
                #pin5.write(pwm)
              
            elif x%2 == 1 :
                time.sleep(self.rampa [x])
                delay = self.rampa [x]
            print "|MAQUINA TIERRA| pwm = ", pwm, "time = ", delay

            # encendido de luz 2 """

class maquinaAgua(object): 
    'Common base class for all employees'
    ordCount = 0



    def __init__(self, sentido, rampa):

        self.rampa = rampa
        self.sentido = sentido

        maquinaAgua.ordCount += 1
       

    def encender(self):

        if self.sentido in ['izq'] :
            #board.digital[10].write(1)
            #board.digital[13].write(0)
            print "Agua izquierda"

        elif self.sentido in ['der'] : 
            #board.digital[10].write(0)
            #board.digital[13].write(1)  
            print "Agua derecha"

        elif self.sentido in ['parar'] : 
            #pin9.write(0)
            #board.digital[10].write(0)
            #board.digital[13].write(0)
            #board.digital[12].write(0)  
            print "Agua parar"


    def linea (self) : 
        rampaLen = len(self.rampa )
        pwm = 0
        delay = 0

        

        for x in xrange(0,rampaLen):
          
            #encendido de luz 2
            if x == 0 :
                #board.digital[12].write(1)
                #pin11.write(1.0)
                print "inicio de rampa"


            #apagado de luz 2 con delay
            elif x == (rampaLen - 1) :
                time.sleep(self.rampa [rampaLen-1] + 0.2)
                #board.digital[12].write(0)
                #pin11.write(0)

            if x%2 == 0 :
                pwm = self.rampa [x]
                #pin9.write(pwm)
              
            elif x%2 == 1 :
                time.sleep(self.rampa[x])
                delay = self.rampa[x]
            print "|MAQUINA AGUA| pwm = ", pwm, "time = ", delay

            # encendido de luz 2 """

class StdOutListener(tweepy.StreamListener):

            def __init__(self):
                time.sleep(4)
                self.contadorTierra = 0
                self.contadorAgua = 0
                self.contadorHastags = 0


                

            def on_data(self, data):
                # Twitter returns data in JSON format - we need to decode it first
                decoded = json.loads(data)

                # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
                prueba = '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
                prueba1= decoded['text'].encode('ascii', 'ignore')
                if prueba1 != "" :
                    print prueba1

                    self.contadorHastags = self.contadorHastags + 1
                    

                    if prueba1.find("tierra") != -1: #prender motor 1, defecha 50% PWM
                        
                        self.contadorTierra = self.contadorTierra + 1

                        print "CountTweet tierra: ", self.contadorTierra

                        #1 ####### AQUI PROGRAMAS #########

                        if self.contadorTierra%4 == 0: 

                            rampa1 = [0.6, 2.1, 0.3, 1, 0.22, 1.4, 0.42, 2, 0, 0]

                            r0= maquinaRaiz("izq", rampa1)

                            tr0_e = threading.Thread(target=r0.encender, args=())
                            tr0_l = threading.Thread(target=r0.linea, args=())

                            tr0_e.start()
                            tr0_l.start()


                        #2 ####### AQUI PROGRAMAS #########
                        if self.contadorTierra%4 == 1: 

                            rampa1 = [0.6, 2.1, 0.3, 1, 0.22, 1.4, 0.42, 2, 0, 0]
                            
                            r0= maquinaRaiz("izq", rampa1)

                            tr0_e = threading.Thread(target=r0.encender, args=())
                            tr0_l = threading.Thread(target=r0.linea, args=())

                            tr0_e.start()
                            tr0_l.start()


                        #3 ####### AQUI PROGRAMAS #########
                        if self.contadorTierra%4 == 2: 

                            rampa1 = [0.6, 2.1, 0.3, 1, 0.22, 1.4, 0.42, 2, 0, 0]
                            
                            r0= maquinaRaiz("izq", rampa1)

                            tr0_e = threading.Thread(target=r0.encender, args=())
                            tr0_l = threading.Thread(target=r0.linea, args=())

                            tr0_e.start()
                            tr0_l.start()

                        #4 ####### AQUI PROGRAMAS #########
                        if self.contadorTierra%4 == 3: 

                            rampa1 = [0.6, 2.1, 0.3, 1, 0.22, 1.4, 0.42, 2, 0, 0]
                            
                            r0= maquinaRaiz("izq", rampa1)

                            tr0_e = threading.Thread(target=r0.encender, args=())
                            tr0_l = threading.Thread(target=r0.linea, args=())

                            tr0_e.start()
                            tr0_l.start()
                      
                          
                    elif prueba1.find("agua") != -1 :

                        self.contadorAgua = self.contadorAgua + 1

                        print "CountTweet agua: ", self.contadorAgua

                        #1 ####### AQUI PROGRAMAS #########
                        if self.contadorAgua%4 == 0 :

                            rampa2 = [0.2, 1, 0.1, 0.2, 0.7, 2, 0, 0]
                            a0 = maquinaAgua("izq", rampa2)
                            
                            ta0_e = threading.Thread(target=a0.encender, args=())
                            ta0_l = threading.Thread(target=a0.linea, args=())
                          
                            ta0_e.start()
                            ta0_l.start()


                        #2 ####### AQUI PROGRAMAS #########
                        if self.contadorAgua%4 == 1 :

                            rampa2 = [0.2, 1, 0.1, 0.2, 0.7, 2, 0, 0]
                            a0 = maquinaAgua("izq", rampa2)
                            
                            ta0_e = threading.Thread(target=a0.encender, args=())
                            ta0_l = threading.Thread(target=a0.linea, args=())
                          
                            ta0_e.start()
                            ta0_l.start()

                        #3 ####### AQUI PROGRAMAS #########
                        if self.contadorAgua%4 == 2 :

                            rampa2 = [0.2, 1, 0.1, 0.2, 0.7, 2, 0, 0]
                            a0 = maquinaAgua("izq", rampa2)
                            
                            ta0_e = threading.Thread(target=a0.encender, args=())
                            ta0_l = threading.Thread(target=a0.linea, args=())
                          
                            ta0_e.start()
                            ta0_l.start()

                        #4 ####### AQUI PROGRAMAS #########
                        if self.contadorAgua%4 == 3 :

                            rampa2 = [0.2, 1, 0.1, 0.2, 0.7, 2, 0, 0]
                            a0 = maquinaAgua("izq", rampa2)
                            
                            ta0_e = threading.Thread(target=a0.encender, args=())
                            ta0_l = threading.Thread(target=a0.linea, args=())
                          
                            ta0_e.start()
                            ta0_l.start()


                            
                       
                return True


            def on_error(self, status):
                print status



# This is the listener, resposible for receiving data
if __name__ == '__main__':

    try : 
        

        l = StdOutListener()
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        print "Mostrando todos los tweets para #ea5:"

            # There are different kinds of streams: public stream, user stream, multi-user streams
            # In this example follow #programming tag
            # For more details refer to https://dev.twitter.com/docs/streaming-apis
        stream = tweepy.Stream(auth, l)
        stream.filter(track=['#ea5'])

        print "tweet: ", tweet

    except KeyboardInterrupt:
        print "Interrupted"
            #pin9.write(0)
            #board.digital[10].write(0)
            #board.digital[13].write(0)
            #board.digital[12].write(0) 
            #pin5.write(0)
            #board.digital[6].write(0)
            #board.digital[7].write(0)
            #board.digital[8].write(0) 







 	
