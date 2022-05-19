import RPi.GPIO as GPIO
import time
import threading
GPIO.setmode(GPIO.BCM)


def do(pin):
    resistorPin = pin

    while True:
        GPIO.setup(resistorPin, GPIO.OUT)
        GPIO.output(resistorPin, GPIO.LOW)
        time.sleep(0.1)
        
        GPIO.setup(resistorPin, GPIO.IN)
        currentTime = time.time()
        diff = 0
        
        while(GPIO.input(resistorPin) == GPIO.LOW):
            diff  = time.time() - currentTime
        diff = int(diff * 10000)
        print(diff)
        check(26,diff)
        time.sleep(0.05)
        
def check(pin,diff):
    GPIO.setup(pin,GPIO.OUT)
    if(diff < 1):
        GPIO.output(pin,True)
        time.sleep(0.5)
        GPIO.output(pin,False)
    do(18)
    
    
def main():
    do(18)
        
main()