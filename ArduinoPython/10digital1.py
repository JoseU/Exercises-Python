#!/usr/bin/python
from pyfirmata import Arduino, util

# para buscar el puerto ls /dev/tty.*
import time

board = Arduino('/dev/tty.usbserial-A400eMcd')
pin5 = board.get_pin('d:5:p')
pin9 = board.get_pin('d:9:p')

pin11 = board.get_pin('d:11:p')
pin3 = board.get_pin('d:3:p')

contadorAgua = 0
contadorRaices = 0


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
		    board.digital[11].write(0)
		elif self.sentido in ['der'] : 
		    board.digital[10].write(0)
		    board.digital[11].write(1)  

		elif self.sentido in ['parar'] : 
		    pin9.write(0)
		    board.digital[10].write(0)
		    board.digital[11].write(0)
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






"""def latido(tiempoTotal, iluminar = 0) :
	
	
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
contadorAgua = 0 """


if __name__ == '__main__':

	try : 





		while True :

			consulta = raw_input('cual es el tweet: ')

			#print consulta

			
			
			
			if consulta.lower() in ['raices', 'tierra'] : #prender motor 1, defecha 50% PWM
				
				contadorRaices = contadorRaices + 1
				print "ContandoRaices: ", contadorRaices

				if contadorRaices%3 == 0 :

					
					#		pwm tiempo
					rampa1 = [0.3, 0.1, 0.2, 1, 0.13, 1.4, 0.125, 2, 0, 0]
					
					r0= maquinaRaiz("izq", rampa1)
					r0.encender()
					r0.linea()

				elif contadorRaices%3 == 1 :
					#		pwm tiempo
					rampa1 = [0.4, 0.05, 0, 0.2, 0.4, 0.1, 0, 0.2,  0.2, 0.8, 0.15, 1.44, 0.125, 2, 0, 0]
					r0 = maquinaRaiz("der", rampa1)
					r0.encender()
					r0.linea()
					


				
			

			elif consulta.lower() in ['agua', 'mar'] :
				contadorAgua = contadorAgua + 1

				if contadorAgua%2 == 0 :

					rampa2 = [0.2, 1, 0.1, 0.2, 0, 0]
					m = maquinaAgua("der", rampa2)
					m.encender()
					m.linea()
					

				if contadorAgua%2 == 1 :

					rampa2 = [0.6, 1.4, 0.5, 0.2, 0, 0]
					m = maquinaAgua("izq", rampa2)
					m.encender()
					m.linea()
					


			else :
				print "No entiendo tu tweet"
				"""latido(2.2)
				maquinaAgua("parar")
				maquinaRaices("parar")"""





	except KeyboardInterrupt:
		print "Interrupted"
		maquinaAgua("parar")
		maquinaRaices("parar")




	