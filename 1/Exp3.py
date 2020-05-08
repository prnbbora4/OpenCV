import cv2

img=cv2.imread('leena.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
#cv2.threshold() returns a value so ret variable is used

ret1, binaryInv = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)


cv2.imshow('Original Image', img)
cv2.waitKey(0)

cv2.imshow('Gray Image', gray)
cv2.waitKey(0)

cv2.imshow('Binary Image', binary)
cv2.waitKey(0)

cv2.imshow('BinaryInv Image', binaryInv)
cv2.waitKey(0)

cv2.destroyAllWindows()


#image color conversion or filter