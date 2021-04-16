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




# timer roshan when dead
roshanDied = 0
warn = False
warnRoshan = False
warnExpiredAegis = False

AegisonceOnly = False
BountyonceOnly = False
StackonceOnly = False
RoshanSpawnonceOnly = False

def RoshanSpawnCall():
    global RoshanSpawnonceOnly
    RoshanSpawnonceOnly = True
    print("roshan is spawn")
    playsound("roshan respawn.wav",False)

itemJungleonceOnly = False
def AegisExpiredCall():
    global AegisonceOnly
    AegisonceOnly = True
    print("Aegis expired 1 menit lagi",False)
    # playsound("aegis.wav")

def itemJungleCall():
    global itemJungleonceOnly
    itemJungleonceOnly = True
    playsound("itemJungle.wav",False)

def BountyCall():
    global BountyonceOnly
    BountyonceOnly = True
    playsound("bounty.wav")

def StackCall():
    global StackonceOnly
    StackonceOnly = True

    playsound("stack.wav")

while True:
    # Grab some screen
    time.sleep(0.1)
    # checkRS()
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
    menit = int(menit)

    if pyautogui.locateOnScreen('rs.png',confidence=0.8,region=(0,int(height*0.70),int(width/2),int(height)))!=None:
        roshanDied = menit   
        RoshanSpawnonceOnly = False
        print("\033[92mAegis will expired at: ",menit+5,":",detik)

    if(roshanDied + 4 == menit and AegisonceOnly == False):
        AegisExpiredCall()
        print("\033[93mAegis will expired 1 more minute at: ",menit+1,":",detik)
    if(roshanDied + 8 == menit and RoshanSpawnonceOnly == False):
        RoshanSpawnCall()

    if(menit==7 or menit==17 or menit == 27 or menit == 37 or menit == 60):
        if(itemJungleonceOnly== False):
            itemJungleCall()
    else:
        itemJungleonceOnly = False

    if (menit+1)%3 == 0:
        if detik >= 30:
            warnBounty = True
        else:
            warnBounty = False
    else:
        warnBounty = False
    
    if detik >= 40:
        warnStack = True
    else:
        warnStack = False
        StackonceOnly = False

    if(warnStack and StackonceOnly==False):
        StackCall()

    if(warnBounty==False):
        BountyonceOnly = False
    if(warnBounty and BountyonceOnly == False):
        BountyCall()

