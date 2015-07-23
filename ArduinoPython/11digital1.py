#!/usr/bin/python
from pyfirmata import Arduino, util

# para buscar el puerto ls /dev/tty.*
import time

board = Arduino('/dev/ttyUSB0')
pin5 = board.get_pin('d:5:p')
pin9 = board.get_pin('d:9:p')
pin11 = board.get_pin('d:11:p')
pin3 = board.get_pin('d:3:p')


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
        board.digital[13].write(0)
    elif sentido in ['der'] : 
        board.digital[10].write(0)
        board.digital[13].write(1)  

    elif sentido in ['parar'] : 
        pin9.write(0)
        board.digital[10].write(0)
        board.digital[13].write(0)
        board.digital[12].write(0)  

def latido(tiempoTotal, iluminar = 0) :
	
	
	board.digital[12].write(1)
	board.digital[8].write(1)

	pin11.write(0.4)
	pin3.write(0.4)

	time.sleep(tiempoTotal/4)

	board.digital[12].write(0)
	board.digital[8].write(0)

	time.sleep(tiempoTotal/4)

	board.digital[12].write(1)
	board.digital[8].write(1)

	pin11.write(0.65)
	pin3.write(0.65)


	time.sleep(tiempoTotal/8)

	board.digital[12].write(0)
	board.digital[8].write(0)

	time.sleep(tiempoTotal/8)
	pin11.write(0.4)
	pin3.write(0.4)

	board.digital[12].write(1)
	board.digital[8].write(1)

	time.sleep(tiempoTotal/2)

	board.digital[12].write(0)
	board.digital[8].write(0)

	pin11.write(0)
	pin3.write(0)



contadorRaices = 0
contadorAgua = 0


if __name__ == '__main__':

	try : 

		while True :

			consulta = raw_input('cual es el tweet: ')

			#print consulta
			
			
			if consulta.lower() in ['raices', 'tierra'] : #prender motor 1, defecha 50% PWM
				
				contadorRaices = contadorRaices + 1
				print "ContandoRaices: ", contadorRaices

				if contadorRaices%3 == 0 :

					maquinaRaices("izq")
					#		pwm tiempo
					rampa1 = [0.3, 0.1, 0.2, 1, 0.13, 1.4, 0.125, 2, 0, 0]
					rampaMotor1(rampa1) 

				elif contadorRaices%3 == 1 :
					maquinaRaices("der")
					#		pwm tiempo
					rampa1 = [0.4, 0.05, 0, 0.2, 0.4, 0.1, 0, 0.2,  0.2, 0.8, 0.15, 1.44, 0.125, 2, 0, 0]
					rampaMotor1(rampa1) 

				elif contadorRaices%3 == 2 :
					maquinaRaices("der")
					#		pwm tiempo
					rampa1 = [0.4, 0.05, 0, 0.2, 0.4, 0.15, 0, 0.2,  0.2, 0.8, 0.15, 1.44, 0.125, 2, 0, 0]
					rampaMotor1(rampa1) 
				
				
				
			

			elif consulta.lower() in ['agua', 'mar'] :
				contadorAgua = contadorAgua + 1


				maquinaAgua("der")
				#		pwm tiempo
				rampa2 = [0.2, 1, 0.1, 0.2, 0, 0]
				rampaMotor2(rampa2)

				

			else :
				print "No entiendo tu tweet"
				latido(2.2)
				maquinaAgua("parar")
				maquinaRaices("parar")





	except KeyboardInterrupt:
		print "Interrupted"
		maquinaAgua("parar")
		maquinaRaices("parar")




	