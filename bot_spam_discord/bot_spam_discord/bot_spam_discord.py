import pyautogui
import time

time.sleep (5)

f = open("mesaj.txt", "r")

for world in f:
    pyautogui.typewrite(world)
    pyautogui.press("enter")
