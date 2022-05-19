import RPi.GPIO as GPIO
import time
import threading
GPIO.setmode(GPIO.BCM)


def main():
    start_time = Lane_Start(18)
    end_time = Lane_Finish(26)
    print(end_time - start_time)
    
    



def Lane_Start(pin):
    resistorPin = pin

    while True:
        GPIO.setup(resistorPin, GPIO.OUT)
        GPIO.output(resistorPin, GPIO.LOW)
        
        GPIO.setup(resistorPin, GPIO.IN)
        currentTime = time.time()
        diff = 0
        
        while(GPIO.input(resistorPin) == GPIO.LOW):
            diff  = time.time() - currentTime
        diff = int(diff * 10000)
        print(diff)
        time_thing = check_Start(18,diff)
        time.sleep(0.05)
        return time_thing
        
def check_Start(pin,diff):
    GPIO.setup(pin,GPIO.OUT)
    if(diff > 1):
        start_time = time.time()
        time.sleep(0.5)
        return start_time
        

def Lane_Finish(pin):
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
        time_thing = check_End(26,diff)
        time.sleep(0.05)
        return time_thing
        

def check_End(pin,diff):
    GPIO.setup(pin,GPIO.OUT)
    if(diff > 1):
        end_time = time.time()
        GPIO.output(pin,True)
        time.sleep(3)
        GPIO.output(pin,False)
        return end_time


main()