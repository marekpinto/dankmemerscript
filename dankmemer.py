import pyautogui
import time
import threading

i = 0
while True:
    time.sleep(10)
    i = i + 1
    pyautogui.typewrite("pls gamble 88\n")
    if i%6 == 0:
        pyautogui.typewrite("pls beg\n")
        pyautogui.typewrite("pls search\n")
    if i%3 == 0:
        pyautogui.typewrite("pls trivia\n")
        time.sleep(1)
        pyautogui.typewrite("2\n")
    if i%12 == 0:
        pyautogui.typewrite("pls postmemes\n")
        time.sleep(1)
        pyautogui.typewrite("d\n")

