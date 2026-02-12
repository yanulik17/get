import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

led = 26

GPIO.setup(led, GPIO.OUT)

out = 6

GPIO.setup(out, GPIO.IN)

while True:
    out = not out
    GPIO.output(led, out)
    time.sleep(2.0)