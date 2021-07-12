import cv2
import numpy as np
import mss
import time
import keyboard
import pyautogui as pg
first_catch = 140

def getScreenshot():
    return np.array(sct.grab(screen))
def findBait(img):
    screen_remove = img[:, :, :3]

    result = cv2.matchTemplate(screen_remove, baitImg, cv2.TM_CCOEFF_NORMED)
    # cv2.imshow('Result', result)
    # cv2.waitKey(0)

    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    WIDTH = baitImg.shape[1]
    HEIGHT = baitImg.shape[0]

    cv2.rectangle(img, max_loc,
                (max_loc[0] + WIDTH, max_loc[1] + HEIGHT), (0, 255, 0), 5)

    print(max_val, max_loc)
    cv2.imshow('Screenshot', img)
    if max_loc[1] > 140 and max_loc[0]< 235 and max_loc[0]>225:
        grab()
def grab():
    pg.click(button='right', clicks=2, interval=1.5)
    time.sleep(2)
baitImg = cv2.imread('crop.jpeg')
# print(fullImg)

with mss.mss() as sct:
    screen = {'top':400, 'left': 700, 'width':500, 'height': 500}

fps = time.time()
while True:
    if keyboard.is_pressed('z'):
        break
while True:


    img = getScreenshot()
    findBait(img)

    # cv2.imshow('Bait', baitImg)
    # cv2.waitKey(0)
    
    time.sleep(.10)
    if keyboard.is_pressed('z'):
        break
    
