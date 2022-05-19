import board
from adafruit_ht16k33.segments import BigSeg7x4
import time

i2c = board.I2C()
display1 = BigSeg7x4(i2c, address = 0x70)
display2 = BigSeg7x4(i2c, address = 0x72)

display1[0] = "F"
display2[0] = "A"
'''bc23[1] = "C"
bc23[2] = "L"
bc23[3] = "F"
'''

'''
def Timer(check):
    
    count10 = 0 #10
    count1 = 0 #1
    count0_1 = 0 #0.1
    count0__1 = 0 #0.01
    count = 1
    
    display[0] = "-"
    display[1] = "-"
    display[2] = "-"
    display[3] = "-"
    
    #time.sleep(3)
    
    display[0] = str(count10)
    display[1] = str(count1)
    display[2] = str(count0_1)
    display[3] = str(count0__1)
    
    while check == False:
        
        if count % 1000 == 0:
            if count10 != 9:
                count10 += 1
            else:
                count10 = 0;
            display[0] = str(count10)
            
        if count % 100 == 0:
            if count1 != 9:
                count1 += 1
            else:
                count1 = 0;
            display[1] = str(count1)
        
        if count % 10 == 0:
            if count0_1 != 9:
                count0_1 += 1
            else:
                count0_1 = 0;
            display[2] = str(count0_1)
        
        if count % 1 == 0:
            if count0__1 != 9:
                count0__1 += 1
            else:
                count0__1 = 0;
            display[3] = str(count0__1)
        
        time.sleep(.01)
        count += 1

check = False
Timer(check)
 '''   
    
    
    
