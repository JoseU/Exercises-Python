import RPi.GPIO as GPIO
import time

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(12, GPIO.OUT)
# blinking function
GPIO.output(12,GPIO.HIGH)
time.sleep(2)
GPIO.output(12,GPIO.LOW)
time.sleep(2)


GPIO.cleanup() 