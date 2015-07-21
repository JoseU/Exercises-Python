#!/usr/bin/python
from pyfirmata import Arduino, util

# para buscar el puerto ls /dev/tty.*
import time




if __name__ == '__main__':

	try : 
		board = Arduino('/dev/tty.usbserial-A400eMcd')
		pin10 = board.get_pin('d:10:p')
		pin11 = board.get_pin('d:11:p')

		def rampaMotor1 (rampa_) : 
			rampaLen = len(rampa_)
			pwm = 0
			delay = 0
			for x in xrange(0,rampaLen):

				#encendido de luz 1
				if x == 0 : 
					board.digital[6].write(1)
				#apagado de luz 1 con delay
					
				elif x == (rampaLen - 1) :
					time.sleep(rampa_[rampaLen-1] + 0.2)
					board.digital[6].write(0)

				if x%2 == 0 :
					pwm = rampa_[x]
					pin10.write(pwm)
					
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
					board.digital[7].write(1)

				#apagado de luz 2 con delay
				elif x == (rampaLen - 1) :
					time.sleep(rampa_[rampaLen-1] + 0.2)
					board.digital[7].write(0)

				if x%2 == 0 :
					pwm = rampa_[x]
					pin11.write(pwm)
					
				elif x%2 == 1 :
					time.sleep(rampa_[x])
					delay = rampa_[x]
				print "|MAQUINA AGUA| pwm = ", pwm, "time = ", delay

				# encendido de luz 2

		def maquinaRaices(sentido):

			if sentido in ['izq'] :
				board.digital[2].write(1)
				board.digital[3].write(0)
			elif sentido in ['der'] : 
				board.digital[2].write(0)
				board.digital[3].write(1)	

			elif sentido in ['parar'] :
				board.digital[2].write(0)
				board.digital[3].write(0)				

		def maquinaAgua(sentido):

			if sentido in ['izq'] :
				board.digital[4].write(1)
				board.digital[5].write(0)
			elif sentido in ['der'] : 
				board.digital[4].write(0)
				board.digital[5].write(1)	

			elif sentido in ['parar'] : 
				board.digital[4].write(0)
				board.digital[5].write(0)				


		while True :

			consulta = raw_input('cual es el tweet: ')

			#print consulta
			
			if consulta.lower() in ['raices', 'tierra'] : #prender motor 1, defecha 50% PWM
				maquinaRaices("izq")
				rampa1 = [0.5, 0.1, 0.1, 0.5, 0.1, 0.2, 0.2, 0.1, 0, 0.1]
				rampaMotor1(rampa1)
				
				
				
			

			elif consulta.lower() in ['agua', 'mar'] :
				maquinaAgua("izq")
				rampa2 = [0.5, 1.1, 0.3, 1.5, 0.1, 1.5, 0.2, 3, 0, 5]
				rampaMotor2(rampa2)
				
				

			else :
				print "No entiendo tu tweet"
				maquinaAgua("parar")
				maquinaRaices("parar")





	except KeyboardInterrupt:
		print "Interrupted"
		maquinaAgua("parar")
		maquinaRaices("parar")

		board.digital[6].write(0)
		board.digital[7].write(0)
		pin10.write(0)



	