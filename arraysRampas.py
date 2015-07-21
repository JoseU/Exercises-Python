#!/usr/bin/python
import time



rampa1 = [0.5, 1.1, 0.3, 1.5, 0.1, 1.5, 0.2, 3, 0.1, 5]

def rampaMotor1 (rampa_) : 
	rampaLen = len(rampa_)
	pwm = 0
	delay = 0
	for x in xrange(0,rampaLen):
		
		if x%2 == 0 :
			pwm = rampa_[x]
			pin10.write(pwm)
			
		elif x%2 == 1 :
			time.sleep(rampa_[x])
			delay = rampa_[x]
		print "pwm = ", pwm, "time = ", delay
			

rampaMotor1(rampa1)

	#print(rampa[x])
