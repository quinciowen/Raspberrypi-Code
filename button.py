import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setwarnings(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if GPIO.input(23) == GPIO.HIGH:
        print("button pushed")
        break