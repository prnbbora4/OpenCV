import cv2
import numpy as np

img=cv2.imread("leena.jpg")

print(img.shape[0:2])

height, width= img.shape[0:2]

start_row, start_col = int(height * .25), int(width * .25)
end_row, end_col = int(height * .75), int(width * .75)

crop=img[start_row:end_row, start_col:end_col]

cv2.imshow("Output", img)
cv2.waitKey()
cv2.imshow("Croping", crop)
cv2.waitKey()

cv2.destroyAllWindows()
#Croping