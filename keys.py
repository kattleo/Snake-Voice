import pyautogui
import time

def keys():
    limit = 100
    time.sleep(5)
    for i in range(0, limit):
        pyautogui.hotkey('up')
        time.sleep(0.2)
        pyautogui.press('left')
        time.sleep(0.2)
        pyautogui.press('down')
        time.sleep(0.2)
        pyautogui.press('right')
        time.sleep(0.2)


keys()