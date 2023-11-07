
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
print ("LED on")
GPIO.output(18,GPIO.HIGH)
time.sleep(5)
   
GPIO.setup(21,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
print("LED on")
GPIO.output(21,GPIO.HIGH)
GPIO.output(16,GPIO.HIGH)
time.sleep(1)
print ("LED off")
GPIO.output(21,GPIO.LOW)
GPIO.setup(16,GPIO.OUT)
print("LED on")
GPIO.output(16,GPIO.HIGH)
time.sleep(4)
print ("LED off")
GPIO.output(16,GPIO.LOW)
