import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)

GPIO.output(18, GPIO.HIGH)

pwm = GPIO.PWM(18, 1000)
pwm.start(50)
pwm.ChangeDutyCycle(75)

if GPIO.input(22):
    print("Pin 2 is HIGH")
else:
    print("Pin 2 is LOW")