# Import dependencies
from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while not keyboard.is_pressed('q'):
    # Check if start race event is visible
    while not keyboard.is_pressed('q'):
        try:
            start_race_event = pyautogui.locateOnScreen('startraceevent.png', grayscale=True, confidence=0.8)
            if start_race_event:
                for _ in range(10):
                    click(448, 586)
                    time.sleep(0.1)
                break
        except pyautogui.ImageNotFoundException:
            continue

    if keyboard.is_pressed('q'):
        break

    while not keyboard.is_pressed('q'):
        keyboard.press('w')
        try:
            finished = pyautogui.locateOnScreen('finished.png', grayscale=True, confidence=0.8)
            if finished:
                keyboard.release('w')
                break
        except pyautogui.ImageNotFoundException:
            continue

    if keyboard.is_pressed('q'):
        break

    # Check if restart is visible
    while not keyboard.is_pressed('q'):
        try:
            restart = pyautogui.locateOnScreen('restart.png', grayscale=True, confidence=0.8)
            if restart:
                keyboard.press('x')
                time.sleep(0.3)
                keyboard.release('x')
                time.sleep(0.3)
                for _ in range(10):
                    click(1263, 879)
                    time.sleep(0.1)
                win32api.SetCursorPos((448, 586))
                break
        except pyautogui.ImageNotFoundException:
            continue

    if keyboard.is_pressed('q'):
        break

print('Q is pressed. Terminating program...')