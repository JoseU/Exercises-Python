import time
import re

pregunta = 1
contador = 1

def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search
	


try:

	while True :
		
   		tweet = input('Options 0: izquierda, 1: derecha, 0: set pwm : ')
   		w = findWholeWord('izquierda')(tweet) 
   		print (w)
   		if tweet in 'izquierda':
   			print ('izquierda')
	   		
	   
	   	elif tweet == 1:
	   		print ('derecha')
   		
   		elif tweet == 2:
   			pwm = int(input ("Set PWM: "))
	   		print (pwm)
   		

except ValueError:
    print ("Not a number")

except KeyboardInterrupt:
    print ("KeyboardInterrupt detected!")