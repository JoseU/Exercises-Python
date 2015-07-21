import time



def latido(tiempoTotal, iluminar = 0) :
	
	pasos = 10
	pasosPwm = 1.0 / pasos
	print "pasos", pasosPwm

	while True : 
	
		
		#board.digital[12].write(1)

		iluminar = iluminar + pasosPwm 

		print iluminar
		#pin11.wrie(iluminar)


		time.sleep (tiempoTotal/pasos)

		if iluminar >= 0.9 : 
			break
		#	board.digital[12].write(0)


latido(0.2)
