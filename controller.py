import RPi.GPIO as GPIO
from time import sleep

relay_pin = 26

GPIO.setmode(GPIO.BCM)

GPIO.setup(relay_pin, GPIO.OUT)

try:
    while True:
        GPIO.output(relay_pin, GPIO.LOW)
        print("Relay is ON")
        sleep(5)  # Wait for 5 seconds

        GPIO.output(relay_pin, GPIO.HIGH)
        print("Relay is OFF")
        sleep(5)  # Wait for 5 seconds

except KeyboardInterrupt:
    print("KeyboardInterrupt: Cleaning up GPIO")
    GPIO.cleanup()

GPIO.cleanup()
