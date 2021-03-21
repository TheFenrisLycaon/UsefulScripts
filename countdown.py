import time
import os

time.sleep(int(input('Enter time (in seconds)::\t')))
os.system('aplay ./src/alarm.wav')
