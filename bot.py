import pyautogui, webbrowser
from time import sleep

webbrowser.open('http://web.whatsapp.com/send?phone=+5492945693128')
sleep(2)

with open('song.txt') as file:
    for line in file:
        pyautogui.typewrite(line)
        pyautogui.press('enter')
