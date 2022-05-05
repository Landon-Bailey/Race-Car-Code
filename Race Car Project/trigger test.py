import RPi.GPIO as GPIO
import time
import threading
from tkinter import *
import board
from adafruit_ht16k33.segments import BigSeg7x4

i2c = board.I2C()
display1 = BigSeg7x4(i2c, address = 0x70)
display2 = BigSeg7x4(i2c, address = 0x72)
Beam_pin1 = 12


def action(Beam_pin1):
    print("tripped")
    

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Beam_pin1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    #GPIO.setup(Beam_pin2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    #GPIO.setup(Beam_pin3, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    #GPIO.setup(Beam_pin4, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.add_event_detect(Beam_pin1,GPIO.FALLING,callback = action)
    
    

main()