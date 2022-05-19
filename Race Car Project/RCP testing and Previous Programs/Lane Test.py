import RPi.GPIO as GPIO
import time
import threading
GPIO.setmode(GPIO.BCM)

    
    
def Lane(pin1, pin2):
    resistorPin1 = pin1
    resistorPin2 = pin2
 
    while True:
        GPIO.setup(resistorPin1, GPIO.OUT)
        GPIO.output(resistorPin1, GPIO.LOW)
        
        currentTime = time.time()
        diff = 0
        while(GPIO.input(resistorPin1) == GPIO.LOW):
            diff  = time.time() - currentTime
            print(diff)
        diff = int(diff * 10000)
        print(diff)
        if(diff < 1):
            GPIO.setup(resistorPin1, GPIO.OUT)
            GPIO.output(resistorPin1,True)
            #starts the timer
            start = time.time()
            
        #Setting up the end
        GPIO.setup(resistorPin2, GPIO.OUT)
        GPIO.output(resistorPin2, GPIO.LOW)
        
        currentTime = time.time()
        diff = 0
        
        while(GPIO.input(resistorPin2) == GPIO.LOW):
            diff  = time.time() - currentTime
        diff = int(diff * 10000)
        print(diff)
        if(diff < 1):
            GPIO.setup(resistorPin2, GPIO.OUT)
            GPIO.output(resistorPin2,False)
            #ends the time
            end = time.time()
            return(end-start)
            #prints the time elasped

def main():
    time_elasped = Lane(18,26)
    print(time_elasped)
    
    
main()