#!/usr/bin/python
from pyfirmata import nano, util

# para buscar el puerto ls /dev/tty.*  linux ls /dev/ttyUS*
import time
# 5pwm 		6 	7 		8 luz1
# 9pwm 		10 11 		12 luz2



if __name__ == '__main__':

	try : 
		board = nano('/dev/tty.usbserial-A400eMcd')
		pin5 = board.get_pin('d:5:p')
		pin9 = board.get_pin('d:9:p')

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
								


		while True :

			consulta = raw_input('cual es el tweet: ')

			#print consulta
			
			if consulta.lower() in ['raices', 'tierra'] : #prender motor 1, defecha 50% PWM
				maquinaRaices("izq")
				rampa1 = [0.2, 1.1, 0.1, 0.5, 0.17, 0.8, 0.21, 0.1, 0, 0.1]
				rampaMotor1(rampa1)
				
				
				
			

			elif consulta.lower() in ['agua', 'mar'] :
				maquinaAgua("izq")
				rampa2 = [0.5, 1.1, 0.3, 1.5, 0.1, 1.5, 0.2, 1, 0, 1]
				rampaMotor2(rampa2)
				
				

			else :
				print "No entiendo tu tweet"
				maquinaAgua("parar")
				maquinaRaices("parar")





	except KeyboardInterrupt:
		print "Interrupted"
		maquinaAgua("parar")
		maquinaRaices("parar")





	