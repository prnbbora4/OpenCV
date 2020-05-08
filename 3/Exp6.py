import cv2

cap = cv2.VideoCapture(0)

def sketch(image):
    img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)

    canny_edge = cv2.Canny(img_gray_blur, 10, 70)

    ret, mask = cv2.threshold(canny_edge,70, 255, cv2.THRESH_BINARY)

    return mask


while True:
    ret, frame = cap.read()
    #cv2.imshow("Camera1", frame)
    cv2.imshow("Output", sketch(frame))
    if cv2.waitKey(20)==13:
        break
cap.release()
cv2.destroyAllWindows()