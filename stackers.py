from sense_hat import SenseHat
import time
from pygame.locals import *
import pygame
# this script demonstrates how to create a class structure for gaming mode
sense = SenseHat()
sense.clear()

class stack():
        def __init__(self):
            pygame.init()
            pygame.display.set_mode((640,480))
            self.gaming = True
        
        def startGame(self):
            pygame.time.set_timer(USEREVENT+1, 800)
            while self.gaming:
                for i in range(0,8):
			sense.set_pixel(i,7,(0,0,255))
			time.sleep(0.5)
			sense.clear()
    
if __name__ == "__main__":
    try:
        game = stack()
        game.startGame()
    except KeyboardInterrupt:
        sense.clear()
