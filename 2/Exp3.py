import cv2
import numpy as np

ref_point=[]
crop=False

def shape_selection(event, x,y,flags,param):
    global ref_point, crop

    if event== cv2.EVENT_LBUTTONDOWN:
        ref_point=[(x,y)]

    if event== cv2.EVENT_LBUTTONUP:
        ref_point.append((x,y))
        cv2.rectangle(image, ref_point[0], ref_point[1], (0, 255, 0), 2)
        cv2.imshow("image", image)


image=cv2.imread("leena.jpg")
clone=image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", shape_selection)

while True:
    cv2.imshow("image", image)
    key=cv2.waitKey(20)

    if key==ord("r"):
        image=clone.copy()
    if key==ord("c"):
        break

if len(ref_point)==2:
    crop_img=clone[ref_point[0][1]:ref_point[1][1], ref_point[0][0]:ref_point[1][0]]
    cv2.imshow("Crop",crop_img)
    cv2.waitKey()

cv2.destroyAllWindows()

#snipping tool