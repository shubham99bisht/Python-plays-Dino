import os
import sys
import time
from PIL import ImageGrab
from PIL import Image
from os import environ
import cv2
import numpy as np
import pyautogui as pg
pg.PAUSE = 0

#x, y, w, h = 585, 327, 244, 100
while True:
    img = ImageGrab.grab()

    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    img = img[327:427, 585:829]

    for x0 in range(170,240,5):
        px = img[58,x0]
        if (px[0]<=150):
            print("jump")
            pg.press("up")
            time.sleep(0.05)
            break
