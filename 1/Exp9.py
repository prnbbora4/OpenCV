import cv2
import numpy as np

background = np.zeros((494,494,3), dtype=np.uint8)

cv2.rectangle(background, (100,100), (300,250), (0,255,0), 6)
cv2.circle(background, (300,300), 100, (0,0,255), -1)

#if thickness is -1 it fills the shape

cv2.imshow("Output", background)

cv2.waitKey()
cv2.destroyAllWindows()