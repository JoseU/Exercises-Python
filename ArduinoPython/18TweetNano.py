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

# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = 'QI1FdMAtp5nabO7Hyb3OatfUu'
consumer_secret = 'dYqie8GQg3J2rtHE8l1jc0wRRKOuDeNTiIhaRuK7UHTf8rNhf6'
access_token = '197481156-OufHbI2EdEp32mF9rQGCftl9pcFbiWrmKWyWGEAe'
access_token_secret = 'MXjqQaUCGXtwFZImYh4JYaPUPORGIkM6FUVxRHah5VCYw'


class maquinaRaiz(object):
   'Common base class for all employees'
   ordCount = 0



   def __init__(self, rampa, sentido):
      
      self.rampa = rampa
      self.sentido = sentido

      forAction.ordCount += 1
   
   def rampaMotor1 (self) : 
      rampaLen = len(self.rampa )
      pwm = 0
      delay = 0
      for x in xrange(0,rampaLen):

          #encendido de luz 1
          if x == 0 : 
              board.digital[8].write(1)
          #apagado de luz 1 con delay
              
          elif x == (rampaLen - 1) :
              time.sleep(self.rampa [rampaLen-1] + 0.2)
              board.digital[8].write(0)

          if x%2 == 0 :
              pwm = self.rampa [x]
              pin5.write(pwm)
              
          elif x%2 == 1 :
              time.sleep(self.rampa [x])
              delay = self.rampa [x]
          print "|MAQUINA TIERRA| pwm = ", pwm, "time = ", delay

          # encendido de luz 2

   def maquinaRaices(self, sentido):

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


class maquinaAgua(object):

   'Common base class for all employees'
   ordCount = 0



   def __init__(self, rampa, sentido):
      
      self.rampa = rampa
      self.sentido = sentido

      forAction.ordCount += 1


   def rampaMotor2 (self) : 
      rampaLen = len(self.rampa )
      pwm = 0
      delay = 0
      for x in xrange(0,rampaLen):
          
          #encendido de luz 2
          if x == 0 :
              board.digital[12].write(1)

          #apagado de luz 2 con delay
          elif x == (rampaLen - 1) :
              time.sleep(self.rampa [rampaLen-1] + 0.2)
              board.digital[12].write(0)

          if x%2 == 0 :
              pwm = self.rampa [x]
              pin9.write(pwm)
              
          elif x%2 == 1 :
              time.sleep(self.rampa[x])
              delay = self.rampa[x]
          print "|MAQUINA AGUA| pwm = ", pwm, "time = ", delay

          # encendido de luz 2



   def maquinaAgua(sentido):

      if self.sentido in ['izq'] :
          board.digital[10].write(1)
          board.digital[11].write(0)
      elif self.sentido in ['der'] : 
          board.digital[10].write(0)
          board.digital[11].write(1)  

      elif self.sentido in ['parar'] : 
          pin9.write(0)
          board.digital[10].write(0)
          board.digital[11].write(0)
          board.digital[12].write(0)  



# This is the listener, resposible for receiving data
if __name__ == '__main__':

    try : 


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

                    if prueba1.find('raices') + prueba1.find('agua') <= 1 :

                        print "No entiendo tu tweet"

                    if prueba1.find('raices') != -1 : #prender motor 1, defecha 50% PWM
                        
                        rampa1 = [0.2, 1.1, 0.1, 0.5, 0.17, 0.8, 0.21, 0.1, 0, 0.1]
                       
                        maquinaRaiz(ramp1, "izq")
                        
                  
                    if prueba1.find('agua') != -1 :
                        rampa2 = [0.5, 1.1, 0.3, 1.5, 0.1, 1.5, 0.2, 1, 0, 1]
                        maquinaAgua(rampa2, "der")
                        

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







 	
