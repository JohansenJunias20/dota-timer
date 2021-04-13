#!/usr/bin/env python3

import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

from PIL import ImageGrab
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
from textblob import TextBlob
import datetime
import ctypes
import time
from pydub import AudioSegment
from playsound import playsound

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

warn = False
onceOnly = False
while True:
    # Grab some screen
    time.sleep(0.1)
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
