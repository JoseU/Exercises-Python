#!/usr/bin/env python

# -*- coding: latin-1 -*-


import RPi.GPIO as GPIO    #Importamos la libreria RPi.GPIO

import time

# Raspberry Comunication

GPIO.setmode(GPIO.BOARD)   #Ponemos la Raspberry en modo BOARD

# set up GPIO output channel
GPIO.setup(12, GPIO.OUT) #Para usar el PWM

GPIO.setup(13, GPIO.OUT) #Para controlar direccion del motor
GPIO.setup(15, GPIO.OUT)

GPIO.setup(11, GPIO.OUT) #Para controlar la luz
GPIO.setup(16, GPIO.OUT)


GPIO.output(11, GPIO.LOW) # configurar en un sentido la luz
GPIO.output(16, GPIO.HIGH) # positivo


p = GPIO.PWM(12,50)        #Ponemos el pin 21 en modo PWM i enviamos 50 senales por segundo
               #Enviamos un pulso del 7.5% para centrar el servo


while True:

    listener = input("que modulo desea (1, 2, 3, 4 y 5)")

    listenerInt = int(listener)


    if listenerInt == 1 :
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)
        p.start(38.0) #control Pwm
        time.sleep(0.4)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)
        p.start(41.0)
        time.sleep(0.2) 
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW) 
        

    elif listenerInt == 2 : 
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)
        p.start(39.0) #control Pwm
        time.sleep(0.1)
        p.start(37.0)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)
        time.sleep(0.2) 
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)

        # otro 
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)
        p.start(38.0) #control Pwm
        time.sleep(0.08)
        p.start(29.0)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)
        time.sleep(0.2) 
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)

    elif listenerInt == 3 : 
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)
        time.sleep(0.75)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)
        p.start(33.0) #control Pwm
        time.sleep(0.1)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)
        p.start(39.0)
        time.sleep(0.05)  
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
        time.sleep(0.05) 
        p.start(25.0)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)
        time.sleep(0.54)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)


    elif listenerInt == 4 : 
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)
        p.start(60.0) #control Pwm
        time.sleep(0.1)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)
        p.start(32.0)
        time.sleep(0.8)  
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)
        p.start(25.0)
        time.sleep(0.3) 
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)

    elif listenerInt == 5 : 
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)
        p.start(32.0) #control Pwm
        time.sleep(0.67)
        p.start(29.0)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)
        time.sleep(0.8) 
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW) 
        p.start(32.0)
        time.sleep(0.03) 
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)
        p.start(28.0)
        time.sleep(3.45) 
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)







 	
