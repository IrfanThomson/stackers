#this script demonstrates conversion of string (str) to integer (int)
from  sense_hat import SenseHat
sense = SenseHat()
import time

red = (255, 0, 0)

i = 1
number = str(i)
sense.show_letter(number, red)
number = int(number)
time.sleep(number)

i += 1
number = str(i)
sense.show_letter(number, red)
number = int(number)
time.sleep(number)

sense.clear()
