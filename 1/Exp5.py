import cv2

rgb=cv2.imread('leena.jpg')

gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)

ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
#cv2.threshold() returns a value so ret variable is used

cv2.imshow('Original Image', rgb)
cv2.imshow('Gray Image', gray)
cv2.imshow('Binary Image', binary)
cv2.waitKey(0)

#save image
cv2.imwrite("rgb.png", rgb)
cv2.imwrite("gray.png", gray)
cv2.imwrite("binary.png", binary)

cv2.destroyAllWindows()