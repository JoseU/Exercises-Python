from pyfirmata import Arduino, util

board = Arduino('/dev/tty.usbmodem1431')

consulta = input('Escoja 1 enceder todos y 0 para apagar: ')

while True :

	if consulta == 1 :

		board.digital[2].write(1)
		board.digital[3].write(1)
		board.digital[4].write(1)
		board.digital[5].write(1)
		board.digital[6].write(1)
		board.digital[7].write(1)

	else
		board.digital[2].write(1)
		board.digital[3].write(1)
		board.digital[4].write(1)
		board.digital[5].write(1)
		board.digital[6].write(1)
		board.digital[7].write(1)