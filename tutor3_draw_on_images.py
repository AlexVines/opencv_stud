import numpy as np
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

# create a line from 0 0 to 150 150 coords colored in white (BGR) with pic width of 15 pixels
cv2.line(img, (0, 0), (150, 150), (255, 255, 255), 15)

# create rectangle 15 25 (top left) and 200 150 (bottom right) coords width = 10
cv2.rectangle(img, (15, 25), (200, 150), (0, 255, 0), 15)

# create a circle with center on (100, 63), radius = 55, color = red, (-1 is for filled circle)
cv2.circle(img, (100, 63), 55, (0, 0, 255), -1)

# create poligons
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
# pts = pts.reshape((-1, 1, 2))
# True is for connecting final point to the first point
cv2.polylines(img, [pts], True, (0, 255, 255), 3)

# Write a text starts at (100, 230), size=1, fat=5
font = cv2.FONT_ITALIC
cv2.putText(img, 'OpenCV Tuts!', (100, 230), font, 1, (200, 255, 255), 5, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()