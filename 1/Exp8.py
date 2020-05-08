import cv2
import numpy as np

background = np.zeros((494,494,3), dtype=np.uint8)

cv2.line(background, (0,0), (493,493), (0,255,0), 7)

cv2.imshow("Output", background)

cv2.waitKey()
cv2.destroyAllWindows()

#line drawing
