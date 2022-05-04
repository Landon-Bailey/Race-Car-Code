import RPi.GPIO as GPIO
import time
import threading
from tkinter import *
import board
from adafruit_ht16k33.segments import BigSeg7x4

i2c = board.I2C()
display1 = BigSeg7x4(i2c, address = 0x70)
display2 = BigSeg7x4(i2c, address = 0x72)
main_window = Tk()

display1[0] = "-"
display1[1] = "-"
display1[2] = "-"
display1[3] = "-"
display2[0] = "-"
display2[1] = "-"
display2[2] = "-"
display2[3] = "-"

#lane 1
Beam_pin1 = 12
Beam_pin2 = 16 
#lane 2          
Beam_pin3 = 23
Beam_pin4 = 24
         

startLane1 = 0
startLane2 = 0
endLane1 = 0
endLane2 = 0

done1 = False
done2 = False

l1t = 0

def start1(pin):
    print("Lane 1 started!")
    global startLane1
    startLane1 = time.time()
    global l1t
    #l1t = threading.Thread(target=Timer, args = (done1,))
    #l1t.start()

def start2(pin):
    print("Lane 2 started!")
    global startLane2
    startLane2 = time.time()
    #l2t = threading.Thread(target=Timer, args = (done2,))
    #l2t.start()
    
def end1(pin):
    print("Lane 1 finished!")
    global endLane1
    endLane1 = time.time()
    print("Lane 1 took ", "{:.2f}".format((endLane1 - startLane1)), "seconds")
    global done1
    done1 = True
    global l1t
    #l1t = threading.Thread(target=Timer, args = (done1,))
    #l1t.start()
    Timer1(startLane1,endLane1) 
    

def end2(pin):
    print("Lane 2 finished!")
    global endLane2
    endLane2 = time.time()
    print("Lane 2 took ", "{:.2f}".format((endLane2 - startLane2)), "seconds")
    global done2
    done2 = True
    Timer2(startLane2,endLane2)
    
def Timer1(start,end):
    display_time = end - start
    final_display_time = round(display_time,2)
    display1.print(str(final_display_time))
    if final_display_time < 10:
        display1[0] = "0"

def Timer2(start,end):
    display_time = end - start
    final_display_time = round(display_time,2)
    display2.print(str(final_display_time))
    if final_display_time < 10:
        display2[0] = "0"
        
        
    
    
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

def start_button():
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
        '''
        current_Time = time.time()
        if done1 == False:
                display1.print(str(current_Time - startLane1))
        if done2 == False:
                display2.print(str(current_Time - startLane2))         '''       
                
        pass

     
    
    compareTimes()
    
    GPIO.cleanup()
    Label(main_window, text = " Race Track not ready ").grid(row = 2, column = 0)
    return
    
    
        
    
    
def end_button():
    print("Reseting Program...")
    global startLane1
    global startLane2
    global endLane1
    global endLane2
    global done1
    global done2
    startLane1 = 0
    startLane2 = 0
    endLane1 =  0
    endLane2 = 0
    display1[0] = "-"
    display1[1] = "-"
    display1[2] = "-"
    display1[3] = "-"
    display2[0] = "-"
    display2[1] = "-"
    display2[2] = "-"
    display2[3] = "-"
    done1 = False
    done2 = False
    Label(main_window, text = "Race Track ready to go").grid(row = 2, column = 0)
    
    #print("Ready to go")
    
    
def quit_program():
    print("Exiting the Program...")
    quit()
   
   
   
Label(main_window, text = "Race Car GUI Program").grid(row = 0, column = 0)
Label(main_window, text = "Status of Race Track:").grid(row = 1, column = 0)
Label(main_window, text = "Race Track ready to go").grid(row = 2, column = 0)
Button(main_window, text = "Start", bg = 'green', command = start_button).grid(row = 4, column = 3)
Button(main_window, text = "Reset", bg = 'yellow', command = end_button).grid(row = 4, column = 4)
Button(main_window, text = "Quit", bg = 'red', command = quit_program).grid(row = 5, column = 3)

main_window.mainloop()


               
