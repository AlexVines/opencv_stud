import cv2
import numpy as np

img1 = cv2.imread('tut5_3.png')
img2 = cv2.imread('tut5_2.png')
img3 = cv2.imread('python.png')

rows, cols, channels = img3.shape
roi = img1[0: rows, 0:cols]

img2gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

# 220 is a threshhold value. basically if pixel value is above 220 it will be converted to 225
ret, mask = cv2.threshold(img2gray, 220, 150, cv2.THRESH_BINARY_INV)

# add 2 images (i prefer second way)
add = img1 + img2
add2 = cv2.add(img1, img2)
# add with priority (0 is gamma value)
weighted = cv2.addWeighted(img1, 0.3, img2, 0.5, 0)


# making a mask to make a bg of icon transparent
mask_inv = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img3_fg = cv2.bitwise_and(img3, img3, mask=mask)

dst = cv2.add(img1_bg, img3_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)
# cv2.imshow('dst', dst)
# cv2.imshow('mask', mask)
# cv2.imshow('fg', img3_fg)
# cv2.imshow('add', weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
