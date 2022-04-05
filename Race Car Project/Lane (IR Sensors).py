import RPi.GPIO as GPIO
import time

#1 lane
#12 and 23 is start
Beam_pin1 = 12
#16 and 24 is end
Beam_pin2 = 16


def Break_beam(channel):
    while True:
        if GPIO.input(Beam_pin1) == False:
            start_time = time.time()
            print("beam broken")
            break 
     
    time.sleep(1)
    while True:
        if GPIO.input(Beam_pin2) == False:
            end_time = time.time()
            print("beam broken")
            break
    print ("This took ", end_time - start_time - 1, " seconds")
        

        

GPIO.setmode(GPIO.BCM)
GPIO.setup(Beam_pin1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(Beam_pin2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.add_event_detect(Beam_pin1,GPIO.BOTH,callback = Break_beam)
GPIO.add_event_detect(Beam_pin2,GPIO.BOTH,callback = Break_beam)

message = input("Press enter to quit\n\n")
GPIO.cleanup()
    