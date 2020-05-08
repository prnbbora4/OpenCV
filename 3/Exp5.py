import cv2
import numpy as np

img=cv2.imread('leena.jpg', 0)
#gray scale
cv2.imshow('Image', img)
cv2.waitKey()

#Sobel edge Detection
Sobel_x = cv2.Sobel(img, cv2.CV_64F,1,0, ksize=5)
Sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

cv2.imshow("Sobel_x", Sobel_x)
cv2.waitKey()

cv2.imshow("Sobel_y", Sobel_y)
cv2.waitKey()

Sobel_or = cv2.bitwise_or(Sobel_x, Sobel_y)
cv2.imshow("Sobel_or", Sobel_or)
cv2.waitKey()

Lap = cv2.Laplacian(img,cv2.CV_64F)
cv2.imshow("Lap", Lap)
cv2.waitKey()

Canny = cv2.Canny(img, 50,170)
cv2.imshow("Canny", Canny)
cv2.waitKey()

cv2.destroyAllWindows()