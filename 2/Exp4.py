import cv2
import numpy as np

img=cv2.imread("leena.jpg")

img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("Output", img)
cv2.waitKey()

cv2.imshow("Output HSV", img_hsv)
cv2.waitKey()

cv2.imshow("Hue", img_hsv[:,:,0])
cv2.waitKey()

cv2.imshow("Saturation", img_hsv[:,:,1])
cv2.waitKey()

cv2.imshow("Value", img_hsv[:,:,2])
cv2.waitKey()

cv2.destroyAllWindows()
