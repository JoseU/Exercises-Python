import time

pregunta = 1
contador = 1
	
try:

	while True :
		
   		number = int(input('Options 0: izquierda, 1: derecha, 0: set pwm : 'x))
   		if number == 0:
   			print ('izquierda')
	   		
	   
	   	elif number == 1:
	   		print ('derecha')
   		
   		elif number == 2:
   			pwm = int(input ("Set PWM: "))
	   		print (pwm)
   		

except ValueError:
    print ("Not a number")

except KeyboardInterrupt:
    print ("KeyboardInterrupt detected!")