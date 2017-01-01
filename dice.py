from microbit import *
import random

side1 = Image("00000:"
              "00000:"
              "00900:"
              "00000:"
              "00000")
              
side2 = Image("00000:"
              "09000:"
              "00000:"
              "00090:"
              "00000")
              
side3 = Image("90000:"
              "00000:"
              "00900:"
              "00000:"
              "00009")
              
side4 = Image("00000:"
              "09090:"
              "00000:"
              "09090:"
              "00000")
              
side5 = Image("90009:"
              "00000:"
              "00900:"
              "00000:"
              "90009")
              
side6 = Image("90009:"
              "00000:"
              "90009:"
              "00000:"
              "90009")
              

sides = [side1,side2,side3,side4,side5,side6]

#display.scroll("SHAKE ME")

while True:
    
    if accelerometer.was_gesture('shake'):
        throw = random.randint(1,6)
        
        pin0.write_digital(1)
        
        display.show(Image.ALL_CLOCKS,50,wait=True)
        pin0.write_digital(0)
        
        display.show(Image.ALL_CLOCKS,50,wait=True)
        pin0.write_digital(1)
        
        display.show(sides[throw - 1])
        
        sleep(100)
        pin0.write_digital(0)
