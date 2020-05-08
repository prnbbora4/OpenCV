import cv2
import numpy as np

img=cv2.imread('leena.jpg')

h, w= img.shape[0:2]

rotation_matrix = cv2.getRotationMatrix2D((w/2, h/2), 90, .6)

rotated_img = cv2.warpAffine(img, rotation_matrix, (w,h))

cv2.imshow('Image', img)
cv2.waitKey()
cv2.imshow('Rotated Image', rotated_img)
cv2.waitKey()
cv2.destroyAllWindows()