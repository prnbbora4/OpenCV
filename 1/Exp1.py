import cv2

img=cv2.imread('leena.jpg')

while True:
    cv2.imshow('Image', img)
    if cv2.waitKey(20)==13:
        break

#print(img)

cv2.destroyAllWindows()

#display an image