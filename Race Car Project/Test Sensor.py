import RPi.GPIO as GPIO
Beam_pin = 16



def Break_beam(channel):
    while True:
        if GPIO.input(Beam_pin) == False:
            print("beam broken")
     
     
    
GPIO.setmode(GPIO.BCM)
GPIO.setup(Beam_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.add_event_detect(Beam_pin,GPIO.BOTH,callback = Break_beam)

message = input("Press enter to quit\n\n")
GPIO.cleanup()

