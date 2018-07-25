from sense_hat import SenseHat
from pygame.locals import *
import pygame
import time
import random

sense = SenseHat()
sense.clear()

class stack():
	def __init__(self):
		pygame.init()
		pygame.display.set_mode((640,480))
		self.gaming = True
	
	def startGame(self):
		pygame.time.set_timer(USEREVENT +1, 800)
		x = 0
		v = 1
		row = 7
		previousX = 99
		while self.gaming:

			if not v == 0 and row >= 0:
				#sense.set_pixel((x-v)%8,row, (0,0,0) )
				sense.set_pixel(x,row, (0,0,255) )
				time.sleep(.05)
				sense.set_pixel(x,row, (0,0,0) )
				time.sleep(.05)
				x = (x+v)%7
			elif row >= 0:
				sense.set_pixel(x,row, (0,0,255) )
				if previousX == 99:
					previousX = x
				if previousX == x:
					v = 1
					x += 1
					row -= 1
					print 'Goal column:',x
				else:
					sense.show_message('You lose!', .05, text_colour = (255,255,0), back_colour = (0,0,255))
					print 'Your column was',x
					sense.clear()
					exit()
			if row == -1:
				sense.show_message('You win!', .05, text_colour = (255,255,0), back_colour = (0,0,255))
				sense.clear()
				exit()
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					v = 0

if __name__ == "__main__":
	try:
		game = stack()
		game.startGame()
	except KeyboardInterrupt:
		sense.clear()
