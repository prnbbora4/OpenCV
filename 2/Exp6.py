import cv2
import numpy as np

squre = np.zeros((300,300), np.uint8)

cv2.rectangle(squre, (50,52), (250,250), 255, -1)
cv2.imshow("squre", squre)
cv2.waitKey()

ellipse = np.zeros((300,300),np.uint8)
cv2.ellipse(ellipse, (150,150), (150, 150), 30, 0, 180, 255, -1)
cv2.imshow("Ellipse", ellipse)
cv2.waitKey()

And = cv2.bitwise_and(squre, ellipse)
cv2.imshow("And", And)
cv2.waitKey()

Or = cv2.bitwise_or(squre, ellipse)
cv2.imshow("Or", Or)
cv2.waitKey()

Not = cv2.bitwise_not(squre)
cv2.imshow("Not", Not)
cv2.waitKey()

Xor = cv2.bitwise_xor(squre, ellipse)
cv2.imshow("Xor", Xor)
cv2.waitKey()

cv2.destroyAllWindows()

#bitwise operator