import cv2
import numpy as np

img=np.zeros((492,494,3), dtype=np.uint8)
#zero matrics for black color using uint8

white=255 * (np.ones((492,494,3), dtype=np.uint8))
#ones matrics for white color using uint8

img2=255 + (np.zeros((492,494,3), dtype=np.uint8))
#zeros matrics for white color using uint8

cv2.imshow("Black", img)
cv2.waitKey()

cv2.imshow("White", white)
cv2.waitKey()

cv2.imshow("White ", img2)
cv2.waitKey()

cv2.destroyAllWindows()

#creating black and white images
