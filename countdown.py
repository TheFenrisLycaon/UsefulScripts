#~/Apps/anaconda3/bin.python
import time
import subprocess
from sys import argv

if len(argv) <= 1:
    time.sleep(int(input('Enter time (in seconds)::\t')))
else:
    time.sleep(int(argv[-1]))

proc = subprocess.Popen(['aplay', './src/alarm.wav'])
input()
proc.kill()
