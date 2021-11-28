#!/usr/bin/python3
#
# evdev_keyboard.py
# Injecting input events. Display "hello" on the console
#
# http://python-evdev.readthedocs.org/en/latest/tutorial.html

import time
from evdev import UInput, ecodes as e

ui = UInput()

#ui.write(e.EV_KEY, e.KEY_LEFTSHIFT, 1)
#ui.write(e.EV_KEY, e.KEY_EQUAL, 1)
#ui.write(e.EV_KEY, e.KEY_EQUAL, 0) 
ui.write(e.EV_KEY, e.KEY_MINUS, 1)
ui.write(e.EV_KEY, e.KEY_MINUS, 0) 
#ui.write(e.EV_KEY, e.KEY_LEFTSHIFT, 0)
time.sleep(0.2)

ui.syn()
ui.close()
