import cv2
import numpy as np

img= np.zeros((512,512, 3), dtype=np.uint8)

windowName ='Drawing'

cv2.namedWindow(windowName)

def draw_circle(event, x, y, flags, param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 40, (0,0,255), -1)

    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x,y), 30, (0,255,0), -1)

    if event==cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), 20, (255,0,0), -1)

    if event==cv2.EVENT_LBUTTONUP:
        cv2.circle(img, (x,y), 30, (15,255,190), -1)

cv2.setMouseCallback(windowName, draw_circle)

while True:
    cv2.imshow(windowName, img)
    if cv2.waitKey(20)==27:
        break

cv2.destroyAllWindows()

#mouse event