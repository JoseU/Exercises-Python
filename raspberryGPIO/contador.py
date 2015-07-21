import time
counter = 1
pregunta = 1

	
try:
	while True :
   		mode = int(raw_input('Input:'))

except ValueError:
    print ("Not a number")

except KeyboardInterrupt:
    print ("KeyboardInterrupt detected!")