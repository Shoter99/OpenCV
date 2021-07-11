import cv2
import numpy as np

fullImg = cv2.imread('full.jpeg')
baitImg = cv2.imread('crop.jpeg')
# print(fullImg)


# cv2.imshow('Bait', baitImg)
# cv2.waitKey(0)

result = cv2.matchTemplate(fullImg, baitImg, cv2.TM_CCOEFF_NORMED)
# cv2.imshow('Result', result)
# cv2.waitKey(0)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)


WIDTH = baitImg.shape[1]
HEIGHT = baitImg.shape[0]

cv2.rectangle(fullImg, max_loc,
              (max_loc[0] + WIDTH, max_loc[1] + HEIGHT), (0, 255, 0), 5)

cv2.imshow("Full image", fullImg)
cv2.waitKey(0)
