import RPi.GPIO as GPIO
import time
import threading
from tkinter import * # (Tkinter is for the GUI)
import board
import os
import sys
from adafruit_ht16k33.segments import BigSeg7x4

#I2C Timers and differentiating the addresses
i2c = board.I2C()
display1 = BigSeg7x4(i2c, address = 0x70)
display2 = BigSeg7x4(i2c, address = 0x72)
#Create an instance of Tkinter frame
win= Tk()
team_name1 = 'Team 1'
team_name2 = 'Team 2'

#Set the geometry of Tkinter frame
win.geometry("750x250")
win.title("Race Car Program")



#Setting the Pins

#lane 1
set1 = 12
Beam_pin1 = 12
Beam_pin2 = 16 
#lane 2
set2 = 23
Beam_pin3 = 23
Beam_pin4 = 24
         

startLane1 = 0
startLane2 = 0
endLane1 = 0
endLane2 = 0

#Checks to see if the timers have grabbed the times or not 
done1 = False
done2 = False


def setup1(set1):
    display1[0] = "-"
    display1[1] = "-"
    display1[2] = "-"
    display1[3] = "-"

def setup2(set2):
    display2[0] = "-"
    display2[1] = "-"
    display2[2] = "-"
    display2[3] = "-"


#This line of code is where if you put the racecar before pressing the start button, then it will create a line of dashes 
GPIO.setmode(GPIO.BCM)
GPIO.setup(Beam_pin1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(Beam_pin2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(Beam_pin3, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(Beam_pin4, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.add_event_detect(set1,GPIO.FALLING,callback = setup1)
GPIO.add_event_detect(set2,GPIO.FALLING,callback = setup2)



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
    global team_name1
    global team_name2
    Lane1Time = endLane1 - startLane1
    Lane2Time = endLane2 - startLane2
    #If Lane 1 finishes first
    if(Lane1Time - Lane2Time > 0):
        print("Lane 2 Wins!")
    elif(Lane2Time - Lane1Time > 0):
        print("Lane 1 Wins!")
    SavetoFile(team_name1,Lane1Time,team_name2,Lane2Time)


def start_button():
    status = ttk.Label(win, text = "Race Track ready to go").place(x = 300, y = 75)
    GPIO.remove_event_detect(set1)
    GPIO.remove_event_detect(set2)
    GPIO.add_event_detect(Beam_pin1,GPIO.RISING,callback = start1)
    GPIO.add_event_detect(Beam_pin2,GPIO.RISING,callback = end1)
    GPIO.add_event_detect(Beam_pin3,GPIO.RISING,callback = start2)
    GPIO.add_event_detect(Beam_pin4,GPIO.RISING,callback = end2)
    
    while not (done1 and done2):       
        pass

     
    
    compareTimes()
    
    #GPIO.cleanup()
    status = ttk.Label(win, text = "Race Track not ready to go").place(x = 300, y = 75)
    return
    
    
        
    
    
def end_button():
    sys.executable = "/usr/bin/python3"
    os.execv(sys.executable, ['python'] + sys.argv)
    
    #print("Ready to go")
    
    
def quit_program():
    print("Exiting the Program...")
    quit()
    

#Import the required Libraries
from tkinter import *
from tkinter import ttk



def name_1():
  global entry
  name = entry.get()
  global team_name1
  team_name1 = name
  
def name_2():
  global entry2
  name = entry2.get()
  global team_name2
  team_name2 = name

  
def SavetoFile(name1,time1,name2,time2):
    time1 = round(time1,4)
    time2 = round(time2,4)
    entry1 = "Team: " + name1 + " - Time: " + str(time1)
    entry2 = "Team: " + name2 + " - Time: " + str(time2)
    scores = open("scores.txt","a")
    scores.write(entry1+ "    |   ")
    scores.write(entry2+"\n")
    scores.close()

    ''''
    entry1 = name1,str(time1)
    entry2 = name2,str(time2)
    scores = open("scores.txt","a")
    scores.write(str(entry1)+ "   ")
    scores.write(str(entry2)+"\n")
    scores.close()
'''

#Initialize a Label to display the User Input
label= ttk.Label(win, text="Status of the Track:", font=("15"))
label.place(x = 300, y = 20)

#Create an Entry widget to accept User Input (Text Input)
entry = ttk.Entry(win, width= 20)
entry.place(x = 20, y = 50)

entry2 = ttk.Entry(win, width= 20)
entry2.place(x = 20, y = 110)

status = ttk.Label(win, text = "").place(x = 300, y = 75)


#Names
name1 = ttk.Label(win, text = "Team Name 1:").place(x = 20, y = 20)
name2 = ttk.Label(win, text = "Team Name 2:").place(x = 20, y = 80)
#Create a Button to validate Entry Widget
enter = ttk.Button(win, text= "Enter", width= 7, command = name_1).place(x = 190, y = 50)
enter2 = ttk.Button(win, text= "Enter", width= 7, command = name_2).place(x = 190, y = 110)


start = ttk.Button(win, text= "Start", width= 7, command = start_button).place(x = 25, y = 160)
reset = ttk.Button(win, text= "Reset", width= 7, command = end_button).place(x = 140, y = 160)
quit1 = ttk.Button(win, text= "Quit", width= 7, command = quit_program).place(x = 82, y = 220)



win.mainloop()


               

