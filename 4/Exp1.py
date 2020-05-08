import cv2
import numpy as np

img = np.zeros((400, 400, 3), np.uint8)
cv2.namedWindow("image")


def nothing(x):
    pass


cv2.createTrackbar("Red", "image", 0, 255, nothing)
cv2.createTrackbar("Green", "image", 0, 255, nothing)
cv2.createTrackbar("Blue", "image", 0, 255, nothing)

switch = "0 : OFF/n1 : ON"
cv2.createTrackbar("Switch", "image", 0, 1, nothing)

while True:
    r = cv2.getTrackbarPos("Red", "image")
    g = cv2.getTrackbarPos("Green", "image")
    b = cv2.getTrackbarPos("Blue", "image")
    s = cv2.getTrackbarPos(switch, "image")

    cv2.imshow("image", img)
    k = cv2.waitKey(1) & 0xFF
    if k == 13:
        break

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv2.destroyAllWindows()
