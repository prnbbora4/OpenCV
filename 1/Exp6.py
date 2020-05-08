import cv2

rgb=cv2.imread('leena.jpg')

b,g,r=cv2.split(rgb)

cv2.imshow('Image', rgb)
print(rgb.shape)
cv2.waitKey()

cv2.imshow('red', r)
print(r.shape)
cv2.waitKey()

cv2.imshow('green', g)
cv2.waitKey()

cv2.imshow('blue', b)
cv2.waitKey()

combine = cv2.merge([b, g, r])
cv2.imshow('Combine output', combine)
cv2.waitKey()

red = cv2.merge([b-b, g-g, r])
cv2.imshow('Red output', red)
cv2.waitKey()

green = cv2.merge([b-b, g, r-r])
cv2.imshow('Green output', green)
cv2.waitKey()

blue = cv2.merge([b, g-g, r-r])
cv2.imshow('Blue output', blue)
cv2.waitKey()

cv2.destroyAllWindows()


#split and merge images with diff plane i.e RGB