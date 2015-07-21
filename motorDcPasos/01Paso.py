
import RPi.GPIO as GPIO    #Importamos la libreria RPi.GPIO

import time

# Raspberry Comunication

GPIO.setmode(GPIO.BOARD)   #Ponemos la Raspberry en modo BOARD

# set up GPIO output channel
GPIO.setup(12, GPIO.OUT) #Para usar el PWM

GPIO.setup(13, GPIO.OUT) #Para controlar 
GPIO.setup(15, GPIO.OUT)



p = GPIO.PWM(12,50)        #Ponemos el pin 21 en modo PWM i enviamos 50 senales por segundo
               #Enviamos un pulso del 7.5% para centrar el servo


while True:

    listener = input("que modulo desea (1, 2, 3, 4 y 5)")

    listenerInt = int(listener)


    if listenerInt == 1 :
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)
        p.start(50.0) #control Pwm
        time.sleep(0.1)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)
        time.sleep(0.2) 
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW) 
        

    elif listenerInt == 2 : 
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)
        p.start(50.0) #control Pwm
        time.sleep(0.1)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)
        time.sleep(0.4)  
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW) 

    elif listenerInt == 3 : 
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)
        p.start(50.0) #control Pwm
        time.sleep(0.1)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)
        time.sleep(0.8)  
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW) 

    elif listenerInt == 4 : 
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)
        p.start(60.0) #control Pwm
        time.sleep(0.1)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)
        time.sleep(1.6)  
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)

    elif listenerInt == 5 : 
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)
        p.start(70.0) #control Pwm
        time.sleep(0.1)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)
        time.sleep(10)  
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)  







 	
