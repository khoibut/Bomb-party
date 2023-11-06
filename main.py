from PIL import Image
from pyautogui import *
import time
import pyperclip
import pyautogui
import keyboard
import pytesseract
import numpy
import cv2
import win32api, win32con
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#box 286 809 849 841
#Word Location:627 146 813 257
fi = open("dic.txt", "r")
dick = []
alr = {}
typed=False
while True:
    temp = fi.readline()
    if len(temp) == 0:
        break
    dick.append(temp)
keyboard.wait("F2")
while True:
    i = -1
    while pyautogui.pixel(627,843)[0]!=22 and pyautogui.pixel(678,825)[1]!=19 and pyautogui.pixel(678,825)[2]!=17:
        typed=False
    click(570,482)
    pyautogui.hotkey("ctrl","a")
    pyautogui.hotkey("ctrl","c")
    click(562,831)
    word=pyperclip.paste()
    n=word[22:25]
    n=n.lower()
    if ord(n[len(n) - 1]) == 13:
        n=n[:-1]
    found = False
    while True:
        if typed:
            break
        i = i + 1
        if dick[i] not in alr:
            for j in range(0, len(dick[i]) - len(n) + 1):
                if n == dick[i][j:j + len(n)]:
                    found = True
        if found:
            alr[dick[i]] = 1
            #pyperclip.copy(dick[i])
            #pyautogui.hotkey("ctrl","v")
            pyautogui.typewrite(dick[i],interval=0.)
            pyautogui.press("enter")
            break
        elif i >= 267750:
            print("fuck you")
            break
    time.sleep(1)
