import numpy as np
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

px = img[55, 55]

img[55, 55] = [255, 255, 255]

# convert area of picture into white
img[100:150, 100: 150] = [255, 255, 255]

# move part of the picture and copy into another part
# 211-37 = 174 - 0, etc (size shoud be the same
watch_face = img[37: 211, 107:294]
img[0:174, 0:187] = watch_face

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
