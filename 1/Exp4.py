import cv2
import numpy as np

img=cv2.imread('leena.jpg')

cv2.imshow('Image', img)

cv2.waitKey(0)

print(img.shape)

print("Height : ", img.shape[0])
print("Width : ", img.shape[1])
print("Depth : ", img.shape[2])
print("\n")
cv2.destroyAllWindows()

h,w,d=np.shape(img)
print("Height : ", h)
print("Width : ", w)
print("Depth : ", d)
print("Datatype : ", img.dtype)
#unit8  means unsigned integer 8bit =2**8=256==0---255

#image height , width and depth