import cv2
import numpy as np

img=cv2.imread('leena.jpg')

h, w= img.shape[0:2]
print(h)
print(w)

q_height, q_width=h/4, w/4

#T = | 1 0 Tx |
#    | 0 1 Ty |

T = np.float32([[1,0, q_width],
                [0,1,q_height]])

img_trans = cv2.warpAffine(img,T,(w,h))
print(T)

cv2.imshow('Image', img)
cv2.waitKey()

cv2.imshow('Translation', img_trans)
cv2.waitKey()

cv2.destroyAllWindows()