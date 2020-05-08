import cv2
import numpy as np
import time


def main():
    windowName = "Live"
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    row, col, channels = frame.shape
    angle = 0
    scale = 1

    while True:
        ret, frame = cap.read()
        if angle == 360:
            angle = 0
        R = cv2.getRotationMatrix2D((col / 2, row / 2), angle, scale)
        print(R)

        output = cv2.warpAffine(frame, R, (col, row))
        cv2.imshow(windowName, output)
        angle = angle + 1
        #time.sleep(0.01)
        if cv2.waitKey(20) == 27:
            break
    cv2.destroyAllWindows()
    cv2.destroyWindow(windowName)
    cap.release()


main()
