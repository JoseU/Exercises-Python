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

GPIO.setup(22, GPIO.OUT)


def luzEncender (): 

    GPIO.output(11, GPIO.HIGH) # configurar en un sentido la luz
    GPIO.output(16, GPIO.LOW) # positivo
    GPIO.output(22, GPIO.HIGH)

def luzApagar (): 

    GPIO.output(11, GPIO.LOW) # configurar en un sentido la luz
    GPIO.output(16, GPIO.LOW) # positivo
    GPIO.output(22, GPIO.LOW)



def motorLeft () : 

    GPIO.output(13, GPIO.LOW) # configurar en un sentido la luz
    GPIO.output(15, GPIO.HIGH) # positivo

def motorRight () :

    GPIO.output(13, GPIO.HIGH) # configurar en un sentido la luz
    GPIO.output(15, GPIO.LOW) # positivo

def motorApagado ():

    GPIO.output(13, GPIO.LOW) # configurar en un sentido la luz
    GPIO.output(15, GPIO.LOW) # positivo


def rampa(inicio, final, tiempo) :
    
    count = inicio

    while True:
        
        print count
        p.start (count)
               

        time.sleep(tiempo)
        count += 1
        pass 

        if count >= final:
            break


p = GPIO.PWM(12,50)        #Ponemos el pin 21 en modo PWM i enviamos 50 senales por segundo
               #Enviamos un pulso del 7.5% para centrar el servo


while True:

    listener = input("que modulo desea (1, 2, 3)")

    listenerInt = int(listener)


    if listenerInt == 1 :
        motorLeft()
        luzEncender()
        p.start(38.0) #control Pwm
        GPIO.output(22, GPIO.HIGH)
        time.sleep(2)

        motorRight()
        p.start(41.0) #control Pwm
        time.sleep(3) 

        motorApagado()
        luzApagar()
        

    elif listenerInt == 2 : 
        motorLeft()
        luzEncender()
        rampa(20, 50, 0.02)
        time.sleep(3)
        motorRight()
        p.start(50.0) #control Pwm
        time.sleep(1.2) 
        motorLeft() 
        luzApagar()
        motorApagado()

    elif listenerInt == 3 : 
        motorLeft()
        luzEncender()
        p.start(38.0) #control Pwm
        time.sleep(0.8)
        motorRight()
        p.start(100.0) #control Pwm
        time.sleep(0.2) 
        motorLeft() 
        luzApagar()










 	
