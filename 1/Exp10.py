import cv2
import numpy as np

background = np.zeros((494,494,3), dtype=np.uint8)

pts = np.array([[10,50], [400,50], [90,200], [50,480]], np.int32)

cv2.polylines(background, [pts], True, (0,0,156), 4)


cv2.imshow("Output", background)

cv2.waitKey()
cv2.destroyAllWindows()