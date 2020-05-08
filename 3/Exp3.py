import cv2
import numpy as np

img=cv2.imread('leena.jpg')


cv2.imshow('Image', img)
cv2.waitKey()


img2 = cv2.resize(img, None, fx=.75, fy=.75)
cv2.imshow('Image2', img2)
cv2.waitKey()

img3 = cv2.resize(img, None, fx=3, fy=3)
cv2.imshow('Image3', img3)
cv2.waitKey()

img4 = cv2.resize(img, (900, 800))
cv2.imshow('Image4', img4)
cv2.waitKey()
#none = height and width

smaller_hafl = cv2.pyrDown(img)
larger_double = cv2.pyrUp(img)
cv2.imshow('Image5', smaller_hafl)
cv2.waitKey()
cv2.imshow('Image6', larger_double)
cv2.waitKey()

cv2.destroyAllWindows()



#image resizing