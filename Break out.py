from microbit import *
import random
import music
import math

class Ship():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def move_left(self):
        
        if self.x != 0:
            self.x -= 1
        
    def move_right(self):
        
        if self.x != 4:
            self.x += 1


def DrawGame(t):
    img = Image('00000:'*5)

    img.set_pixel(ship.x, ship.y, 7)
    
    return img
    
def ResetGame():
    display.clear()
    global score
    score = 0
    global asteroids
    asteroids = []
    global level
    level = 1
      
      
def GetTarget(n):
    working = n + 1
    working = n * working
    working = working / 2

    return working * 10
    
        
score = 0
level = 1

while True:
    display.show(Image.TARGET)
    
    if button_b.was_pressed():
        DisplayScore()
        
    if button_a.was_pressed():
        
        ResetGame()
            
        ship = Ship(2, 4)
        tick = 0
        paws = 75
        sleep(1000)
        playing = True

        while playing:
            
            #Update ship location
            
            reading = accelerometer.get_x()
            
            if reading > 100:
                ship.move_right()
                
            elif reading < -100:
                ship.move_left()
            
            i = DrawGame(tick)
            # update ticks
            tick += 1
            
            if tick == 3:
                tick = 0
                
                display.show(i)
                
            sleep(paws)    
                