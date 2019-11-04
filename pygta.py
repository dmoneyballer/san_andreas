# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 19:30:34 2019

@author: drewg
"""
import numpy as np
from PIL import ImageGrab
import cv2
import time
last_time = time.time()
while True:
    # grabbing full screen takes over a second, grabbinb 800x600 takes .35 seconds
    printscreen_pil = ImageGrab.grab(bbox=(0,40,800,600))
    printscreen_numpy = np.array(printscreen_pil.getdata(), dtype='uint8')\
    .reshape((printscreen_pil.size[1],printscreen_pil.size[0],3))
    print( time.time() - last_time)
    last_time = time.time()
    cv2.imshow('window', printscreen_numpy)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindow()
        break