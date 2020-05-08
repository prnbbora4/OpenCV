import cv2
import numpy as np

background = np.zeros((494,494,3), dtype=np.uint8)

name = input("Enter your name :")

cv2.putText(background, name, (55, 290), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 4)


cv2.imshow("Output", background)

cv2.waitKey()
cv2.destroyAllWindows()