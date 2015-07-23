#!/usr/bin/python
from pyfirmata import nano, util
import tweepy
import json
import time

# para buscar el puerto ls /dev/tty.* || ls /dev/ttyUS*
# 5pwm      6   7       8 luz1
# 9pwm      10 11       12 luz2
# setting arduino nano
board = nano('/dev/tty.usbserial-A400eMcd')
pin5 = board.get_pin('d:5:p')
pin9 = board.get_pin('d:9:p')

pin11 = board.get_pin('d:11:p')
pin3 = board.get_pin('d:3:p')

# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = 'QI1FdMAtp5nabO7Hyb3OatfUu'
consumer_secret = 'dYqie8GQg3J2rtHE8l1jc0wRRKOuDeNTiIhaRuK7UHTf8rNhf6'
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
            board.digital[6].write(1)
            board.digital[7].write(0)
        elif self.sentido in ['der'] : 
            board.digital[6].write(0)
            board.digital[7].write(1)   

        elif self.sentido in ['parar'] :
            pin5.write(0)
            board.digital[6].write(0)
            board.digital[7].write(0)
            board.digital[8].write(0) 

    def linea (self) : 
        rampaLen = len(self.rampa )
        pwm = 0
        delay = 0


        
        for x in xrange(0,rampaLen):

            #encendido de luz 1
            if x == 0 : 

                board.digital[8].write(1)
                pin3.write(1.0)

            #apagado de luz 1 con delay
              
            elif x == (rampaLen - 1) :
                time.sleep(self.rampa [rampaLen-1] + 0.2)
                board.digital[8].write(0)
                pin3.write(0)

            if x%2 == 0 :
                pwm = self.rampa [x]
                pin5.write(pwm)
              
            elif x%2 == 1 :
                time.sleep(self.rampa [x])
                delay = self.rampa [x]
            print "|MAQUINA TIERRA| pwm = ", pwm, "time = ", delay

            # encendido de luz 2 

class maquinaAgua(object): 
    'Common base class for all employees'
    ordCount = 0



    def __init__(self, sentido, rampa):

        self.rampa = rampa
        self.sentido = sentido

        maquinaAgua.ordCount += 1
       

    def encender(self):

        if self.sentido in ['izq'] :
            board.digital[10].write(1)
            board.digital[13].write(0)
        elif self.sentido in ['der'] : 
            board.digital[10].write(0)
            board.digital[13].write(1)  

        elif self.sentido in ['parar'] : 
            pin9.write(0)
            board.digital[10].write(0)
            board.digital[13].write(0)
            board.digital[12].write(0)  


    def linea (self) : 
        rampaLen = len(self.rampa )
        pwm = 0
        delay = 0

        

        for x in xrange(0,rampaLen):
          
            #encendido de luz 2
            if x == 0 :
                board.digital[12].write(1)
                pin11.write(1.0)


            #apagado de luz 2 con delay
            elif x == (rampaLen - 1) :
                time.sleep(self.rampa [rampaLen-1] + 0.2)
                board.digital[12].write(0)
                pin11.write(0)

            if x%2 == 0 :
                pwm = self.rampa [x]
                pin9.write(pwm)
              
            elif x%2 == 1 :
                time.sleep(self.rampa[x])
                delay = self.rampa[x]
            print "|MAQUINA AGUA| pwm = ", pwm, "time = ", delay

            # encendido de luz 2



# This is the listener, resposible for receiving data
if __name__ == '__main__':

    try : 


        class StdOutListener(tweepy.StreamListener):

            def __init__(self):
                time.sleep(4)
                #contadorRaices = 0
                #contadorAgua = 0


                

            def on_data(self, data):
                # Twitter returns data in JSON format - we need to decode it first
                decoded = json.loads(data)

                # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
                prueba = '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
                prueba1= decoded['text'].encode('ascii', 'ignore')
                if prueba1 != "" :
                    print prueba1
                    prueba2 = prueba1.lower()

                    if prueba1.find("tierra") != -1: #prender motor 1, defecha 50% PWM
                        
                        #self.contadorRaices = self.contadorRaices + 1
                        
                        #print "ContandoRaices: ", self.contador1

                        #if self.contadorRaices%3 == 0 :

                            
                            #       pwm tiempo
                        rampa1 = [0.3, 0.1, 0.2, 1, 0.13, 1.4, 0.125, 2, 0, 0]
                        
                        r0= maquinaRaiz("izq", rampa1)
                        r0.encender()
                        r0.linea()

                        #elif self.contadorRaices%3 == 1 :
                            #       pwm tiempo
                         #   rampa1 = [0.4, 0.05, 0, 0.2, 0.4, 0.1, 0, 0.2,  0.2, 0.8, 0.15, 1.44, 0.125, 2, 0, 0]
                          #  r0 = maquinaRaiz("der", rampa1)
                           # r0.encender()
                            #r0.linea()
                            

                    elif prueba1.find("agua") != -1 :
                        #self.contadorAgua = self.contadorAgua + 1

                        #if self.contadorAgua%2 == 0 :

                        rampa2 = [0.2, 1, 0.1, 0.2, 0.7, 2, 0, 0]
                        m = maquinaAgua("izq", rampa2)
                        m.encender()
                        m.linea()
                            

                        #if self.contadorAgua%2 == 1 :

                            #rampa2 = [0.6, 1.4, 0.5, 0.2, 0, 0]
                            #m = maquinaAgua("izq", rampa2)
                            #m.encender()
                            #m.linea()

                            #else :
                                
                               # maquinaAgua("parar")
                                #maquinaRaices("parar")
                        
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
        maquinaAgua("parar")
        maquinaRaices("parar")







 	
