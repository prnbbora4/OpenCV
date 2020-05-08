import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_range = np.array([110,50,50])
    upper_range = np.array([130,255,255])

    mask1 = cv2.inRange(hsv, lower_range, upper_range)

    output = cv2.bitwise_and(frame, frame, mask=mask1)

    cv2.imshow("Camera1", frame)
    cv2.imshow("Output HSV", output)
    if cv2.waitKey(20)==13:
        break
cap.release()
cv2.destroyAllWindows()

#blue object detection