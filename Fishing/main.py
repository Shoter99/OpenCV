import cv2
import numpy as np
import mss
import time
import keyboard
import pyautogui as pg

pg.PAUSE = 0
times = 0


def getScreenshot(scr):
    return np.array(sct.grab(scr))


def findBait(img):
    global times

    screen_remove = img[:, :, :3]

    result = cv2.matchTemplate(screen_remove, baitImg, cv2.TM_CCOEFF_NORMED)
    # cv2.imshow('Result', result)
    # cv2.waitKey(0)

    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    WIDTH = baitImg.shape[1]
    HEIGHT = baitImg.shape[0]

    cv2.rectangle(img, max_loc,
                  (max_loc[0] + WIDTH, max_loc[1] + HEIGHT), (0, 255, 0), 5)

    print(max_val)
    cv2.imshow('Screenshot', img)
    cv2.waitKey(1)
    if max_val > .7:
        grab()
    else:
        times += .01


def grab():
    pg.click(button='right', clicks=2, interval=1.5)
    time.sleep(2)


def checkForBait():
    checkImg = cv2.imread('crop.jpeg')
    isFising = False
    for _ in range(5):
        scr = getScreenshot(lookforBait)
        rem = scr[:, :, :3]
        res = cv2.matchTemplate(rem, checkImg, cv2.TM_CCOEFF_NORMED)
        h, w = checkImg.shape[0], checkImg.shape[1]
        _, max_val, _, max_loc = cv2.minMaxLoc(res)
        cv2.rectangle(scr, max_loc,
                      (max_loc[0] + w, max_loc[1] + h), (0, 255, 0), 5)
        cv2.imshow('Looking for bait', scr)
        print(max_val)
        if max_val > .6:
            isFising = True
            break
        time.sleep(1)
    print(f'Fising: {isFising}')
    if not isFising:
        pg.click(button='right')


baitImg = cv2.imread('bait.jpeg')

# print(fullImg)

with mss.mss() as sct:
    screen = {'top': 400, 'left': 1300, 'width': 620, 'height': 600}
    lookforBait = {'top': 400, 'left': 700, 'width': 500, 'height': 500}

fps = int(time.time())
timesChecked = 1
while True:
    if keyboard.is_pressed('z'):
        break
while True:
    curTime = int(time.time()) - fps
    if(curTime > 30*timesChecked):
        checkForBait()
        timesChecked += 1
    img = getScreenshot(screen)
    findBait(img)

    # cv2.imshow('Bait', baitImg)
    # cv2.waitKey(0)

    time.sleep(.10)
    if keyboard.is_pressed('z'):
        break
