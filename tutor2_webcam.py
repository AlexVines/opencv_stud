import cv2
import numpy as np

# 0 if you have 1 camera, 1 would use second camera if exists
cap = cv2.VideoCapture(0)

# record a video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    out.write(frame)

    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    # press q to close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()