# Import dependencies
from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import win32api, win32con

# Convert resolution if needed (Currently working for 2560x1600 only)
def convertResolution(x, y):
    return int(x * resolution_x / 2560), int(y * resolution_y / 1600)

# Click function
def click(x, y):
    x, y = convertResolution(x, y)
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) # TODO: Randomize the sleep time
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# Set resolution
resolution_x, resolution_y = pyautogui.size()
print(f'Resolution: {resolution_x}x{resolution_y}')

while not keyboard.is_pressed('q'):
    # Check if the 'Start Race Event' button is visible
    while not keyboard.is_pressed('q'):
        try:
            start_race_event = pyautogui.locateOnScreen('/images/startraceevent.png', grayscale=True, confidence=0.8)
            if start_race_event:
                for _ in range(10): # Multiple clicks to ensure the button is clicked
                    click(448, 586)
                    time.sleep(0.1)
                break
        except pyautogui.ImageNotFoundException:
            continue

    if keyboard.is_pressed('q'):
        break
    
    # Check if the race has finished
    while not keyboard.is_pressed('q'):
        keyboard.press('w')
        try:
            finished = pyautogui.locateOnScreen('/images/finished.png', grayscale=True, confidence=0.8)
            if finished:
                keyboard.release('w') # Release the 'W' key once the race has finished
                break
        except pyautogui.ImageNotFoundException:
            continue

    if keyboard.is_pressed('q'):
        break

    # Check if the 'Restart' button is visible
    while not keyboard.is_pressed('q'):
        try:
            restart = pyautogui.locateOnScreen('/images/restart.png', grayscale=True, confidence=0.8)
            if restart:
                keyboard.press('x') # Shortcut for 'Restart' button
                time.sleep(0.3)
                keyboard.release('x')
                time.sleep(0.3)
                for _ in range(10): # Multiple clicks to ensure the button is clicked
                    click(1263, 879)
                    time.sleep(0.1)
                win32api.SetCursorPos((448, 586))   # Move the cursor towards `Start Race Event` button
                break
        except pyautogui.ImageNotFoundException:
            continue

    if keyboard.is_pressed('q'):
        break

print('Q is pressed. Terminating program...')