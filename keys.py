import pydirectinput
import time

def keys():
    limit = 100
    time.sleep(5)
    for i in range(0, limit):
        pydirectinput.press('up')
        time.sleep(0.2)
        pydirectinput.press('left')
        time.sleep(0.2)
        pydirectinput.press('down')
        time.sleep(0.2)
        pydirectinput.press('right')
        time.sleep(0.2)


keys()