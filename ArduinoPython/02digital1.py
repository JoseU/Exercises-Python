from pyfirmata import Arduino, util

pin10 = board.get_pin('d:10:p')
pin11 = board.get_pin('d:11:p')


if __name__ == '__main__':

	try : 
		board = Arduino('/dev/tty.usbmodem1431')


		while True :

			consulta = input('Escoja 1 enceder todos y 0 para apagar: ')


			if consulta == 1 : #prender motor 1, defecha 50% PWM

				board.digital[2].write(1)
				board.digital[3].write(0)
				pin10.write(10)
			

			elif consulta == 2 :
				board.digital[2].write(0)
				board.digital[3].write(1)
				pin10.write(10)


			elif consulta == 2 :

	

	except KeyboardInterrupt:
        print 'Interrupted'
        sys.exit(0)

	