from microbit import *

driving = False

tolarance = 60
direction = 0
normal_speed = 7

    
pin16.set_analog_period(10)
pin12.set_analog_period(10)


def LeftMove(speed, forward):

    pin16.write_analog(speed*100)
    if forward:
        pin15.write_digital(1)
        pin14.write_digital(0)
    else:
        pin15.write_digital(0)
        pin14.write_digital(1)


def LeftStop():
    pin16.write_analog(0)

def RightMove(speed, forward):

    pin12.write_analog(speed*100)
    if forward:
        pin8.write_digital(1)
        pin11.write_digital(0)
    else:
        pin8.write_digital(0)
        pin11.write_digital(1)


def RightStop():
    pin12.write_analog(0)

while True:  
    
    display.show(Image.ASLEEP)
    
    if button_a.was_pressed():
        driving = True

    while driving: 
        
        left = pin0.read_analog()
        right = pin1.read_analog()
    
        if button_a.was_pressed():
            driving = False
            display.show(Image.ASLEEP)
            LeftStop()
            RightStop()
            break
            
        if abs(left - right) < tolarance:
            display.show(Image.ARROW_N)
            RightMove(normal_speed,True)
            LeftMove(normal_speed,True)
            
            
            
        elif left < right: #Left is dark so stear to the right 
            display.show(Image.ARROW_E)
            
            
            RightMove(normal_speed/2,True)
            
        elif left > right: #Right is dark so stear to the right 
            display.show(Image.ARROW_W)
            
            LeftMove(normal_speed/2,True)
            
        sleep(10)
            
        
        