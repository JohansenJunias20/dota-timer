#!/usr/bin/env python3
import subprocess
import sys
from pyautogui import *
import pyautogui
from overlay import Window
import tkinter as tk
from PIL import ImageGrab
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
from textblob import TextBlob
import datetime
import ctypes
import time
from pydub import AudioSegment
from playsound import playsound
import numpy as np

win_0 = Window()
label_0 = tk.Label(win_0.root, text="Window_0123123123")
label_0.pack()
Window.launch()
win_0.destroy()
Window.destroy()
win_0.destroy_all()
Window.destroy_all()
win0 = Window()
label_0 = tk.Label(win_0.root, text="Window_011111432634631")
label_0.pack()
Window.launch()

user32 = ctypes.windll.user32
width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def correction(x):
    try:
        int(x)
        if (isinstance(int(x),int) ):
            return x
    except ValueError:
        if ( x == ":"):
            return x


label = Tkinter.Label(text='Text on the screen', font=('Times New Roman','80'), fg='black', bg='white')
label.master.overrideredirect(True)
label.master.geometry("+250+250")
label.master.lift()
label.master.wm_attributes("-topmost", True)
label.master.wm_attributes("-disabled", True)
label.master.wm_attributes("-transparentcolor", "white")

hWindow = pywintypes.HANDLE(int(label.master.frame(), 16))
# http://msdn.microsoft.com/en-us/library/windows/desktop/ff700543(v=vs.85).aspx
# The WS_EX_TRANSPARENT flag makes events (like mouse clicks) fall through the window.
exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)

label.pack()
label.mainloop()



def checkRS():
    if pyautogui.locateOnScreen('rs.png',confidence=0.8,region=(0,int(height*0.70),int(width/2),int(height)))!=None:
        print("i can see it")
        pyautogui.keyDown("altleft")
        pyautogui.click(x=width/2,y=20)
        pyautogui.keyUp("altleft")                      
    else:
        print("i cannot see it")
warn = False
onceOnly = False
while True:
    # Grab some screen
    time.sleep(0.1)
    checkRS()
    screen =  ImageGrab.grab(bbox=(width/2 -30,22,width/2 + 30,38))
    # Make greyscale
    w = screen.convert('L')

    # Save so we can see what we grabbed
    w.save('grabbed.png')

  



    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(w)
    correctedText = TextBlob(text).correct()
    correctedText = list(map(correction, correctedText))
    menit =""
    detik = ""
    limiter = False
    for i in correctedText:
        if(i==":"):
            limiter = True
            continue
        if(i==None or i == ""):
            continue
        if limiter:
            detik += str(i)
        else:
            menit += str(i)
    if(RepresentsInt(detik) == False or RepresentsInt(menit) == False):
        continue
    detik = int(detik)
    index = 0
    if len(menit) == 2:
        index = 1
    if menit[index] == '4' or menit[index] == '9':
        if detik >= 30:
            warn = True
        else:
            warn = False
    else:
        warn = False
    if(warn==False):
        onceOnly = False
    if(warn and onceOnly == False):
        onceOnly = True
        print("BOUNTY OUTPOST TOMB")
        print(menit)
        print(detik)
        playsound("sound.wav")
