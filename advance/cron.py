import schedule

import time

import os
import random
from pdfminer.high_level import extract_text

_list = ["mujibat is a fine girl hiya hiya oooo ", "abdullah is a ", "Ismail is a ", " dami is  a " ]
_professional = ['cow', 'goat', 'dog', 'puppy', 'kitten']
print("="*20)



def fitbitsteps():
	print("Break Time .......")
	os.system(f'Say Ramadan kareem')


schedule.every(0.1).seconds.do(fitbitsteps)

while True:
	schedule.run_pending()
	time.sleep(1)