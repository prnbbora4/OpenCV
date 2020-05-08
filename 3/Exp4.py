import cv2
import numpy as np

img=cv2.imread('leena.jpg')
cv2.imshow('Image', img)
cv2.waitKey()

kernel_3x3 = np.ones((3,3), np.float32)/9
blur = cv2.filter2D(img, -1, kernel_3x3)

cv2.imshow("Blur", blur)
cv2.waitKey()

kernel_7x7 = np.ones((7,7), np.float32)/49
blur1 = cv2.filter2D(img, -1, kernel_7x7)

cv2.imshow("Blur1", blur1)
cv2.waitKey()

cv2.destroyAllWindows()
