import RPi.GPIO as GPIO
import time
import threading

#lane 1
Beam_pin1 = 12
Beam_pin2 = 16 #Hardware Issue
#lane 2          
Beam_pin3 = 23
Beam_pin4 = 24





startLane1 = 0
startLane2 = 0
endLane1 = 0
endLane2 = 0

done1 = False
done2 = False

def start1(pin):
    print("Lane 1 started!")
    global startLane1
    startLane1 = time.time()

def start2(pin):
    print("Lane 2 started!")
    global startLane2
    startLane2 = time.time()

def end1(pin):
    print("Lane 1 finished!")
    global endLane1
    endLane1 = time.time() 
    print("Lane 1 took ", "{:.2f}".format((endLane1 - startLane1)), "seconds")
    global done1
    done1 = True
    

def end2(pin):
    print("Lane 2 finished!")
    global endLane2
    endLane2 = time.time()
    print("Lane 2 took ", "{:.2f}".format((endLane2 - startLane2)), "seconds")
    global done2
    done2 = True
    
def compareTimes():
    global startLane1
    global startLane2
    global endLane1
    global endLane2
    Lane1Time = endLane1 - startLane1
    Lane2Time = endLane2 - startLane2
    #If Lane 1 finishes first
    if(Lane1Time - Lane2Time > 0):
        print("Lane 2 Wins!")
    elif(Lane2Time - Lane1Time > 0):
        print("Lane 1 Wins!")
    


GPIO.setmode(GPIO.BCM)
GPIO.setup(Beam_pin1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(Beam_pin2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(Beam_pin3, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(Beam_pin4, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.add_event_detect(Beam_pin1,GPIO.RISING,callback = start1)
GPIO.add_event_detect(Beam_pin2,GPIO.RISING,callback = end1)
GPIO.add_event_detect(Beam_pin3,GPIO.RISING,callback = start2)
GPIO.add_event_detect(Beam_pin4,GPIO.RISING,callback = end2)





while not (done1 and done2):
    pass

compareTimes()

message = input("Press enter to quit\n\n")
GPIO.cleanup()
    
               