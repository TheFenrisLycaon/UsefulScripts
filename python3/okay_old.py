import time
from random import randint

import pyautogui

keys = [
    "shift",
    "pageup",
    "pagedown",
    "pagedown",
    "pagedown",
    "shift",
    "pageup",
    "pageup",
]

try:
    while True:
        time.sleep(randint(60, 300))
        print("Sleeping...")

        for i in range(randint(50, 100)):
            print("Moving cursor ... ")
            pyautogui.moveTo(randint(100, 1000), i * randint(10, 25))

        for i in range(randint(1, 3)):
            print("Key presses...")
            pyautogui.press(keys[randint(0, len(keys) - 1)], presses=randint(0, 3))
            pyautogui.press(keys[randint(0, len(keys) - 1)], presses=randint(0, 3))
            pyautogui.press(keys[randint(0, len(keys) - 1)], presses=randint(0, 3))
finally:
    pass
