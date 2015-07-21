import RPi.GPIO as GPIO
import time

x = 0

while x < 1:
	
	# to use Raspberry Pi board pin numbers
	GPIO.setmode(GPIO.BOARD)
	# set up GPIO output channel
	GPIO.setup(13, GPIO.OUT)
	GPIO.setup(12, GPIO.OUT)
	GPIO.setup(11, GPIO.OUT)
	# blinking function
	GPIO.output(13, GPIO.HIGH)
	GPIO.output(12,GPIO.HIGH)
	GPIO.output(11,GPIO.HIGH)
	time.sleep(2)
	GPIO.output(13,GPIO.LOW)
	GPIO.output(12,GPIO.LOW)
	GPIO.output(11,GPIO.LOW)
	time.sleep(2)


GPIO.cleanup() 