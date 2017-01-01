from microbit import *
import random
import music
import math


class Asteroid():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        self.y = self.y + 1
        if self.y == 5:
            self.y = random.randint(0, 0)
            self.x = random.randint(0, 4)
            return True


class Ship():
    def __init__(self, x, y):
        self.x = x
        self.y = y


def DrawGame(t):
    img = Image('00000:'*5)

    img.set_pixel(ship.x, ship.y, 7)
    
    for asteroid in asteroids:
        img.set_pixel(asteroid.x, asteroid.y, 4)
    return img


def DisplayScore():
    display.scroll(str(level) + ":" + str(score))
    
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


asteroids = []

while True:
        display.show(Image.TARGET)
        
        if button_b.was_pressed():
            DisplayScore()
            
        if button_a.was_pressed():
            
            ResetGame()
            
            asteroids.append(Asteroid(random.randint(0, 4), 0))

            ship = Ship(2, 4)
            tick = 0
            paws = 75
            sleep(1000)
            playing = True

            while playing:
                #music.play("D4:4", wait=False, loop=True)
                if button_a.was_pressed() and ship.x != 0:
                    ship.x = ship.x - 1
                    music.pitch(400, 50)
                elif button_b.was_pressed() and ship.x != 4:
                    ship.x = ship.x + 1
                    music.pitch(400, 50)
                i = DrawGame(tick)
                # update ticks
                tick += 1
                if tick == 3:
                    tick = 0
                    
                    for asteroid in asteroids:
                        asteroid.update()
                        
                    i = DrawGame(tick)

                    for asteroid in asteroids:
                        if asteroid.y == 4:
                            if ship.x == asteroid.x:
                                playing = False
                            else:
                                score += 1
                                
                                #Check if we need to add 1 to the level
                                target = GetTarget(level)
                                
                                print(str(level) + ":" + str(target))
                                
                                if score >= target:
                                    #print(str(tick) + ":" + str(level))
                                    level += 1
                                    
                                    display.show(str(level))
                                    music.play(music.POWER_UP, wait = True)
                                    asteroids.append(Asteroid(random.randint(0,4), random.randint(0,1)))
                            
                display.show(i)
                sleep(paws)
            music.play(music.PUNCHLINE, wait=False)
            DisplayScore()
            sleep(2000)
        sleep(50)
