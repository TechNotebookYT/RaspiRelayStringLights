import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)


try:
    counter = -1
    while True:
        counter += 1
        if counter % 2 == 0:
            GPIO.output(26, GPIO.HIGH)
        elif counter % 2 != 0:
            GPIO.output(26, GPIO.LOW)
        else:
            raise Exception("Error")
        input("Press Enter to Toggle")
        
finally:
    GPIO.cleanup()
