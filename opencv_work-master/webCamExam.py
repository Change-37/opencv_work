import numpy as np
import cv2
import matplotlib.pylab as plt

CAMERA_ID = 0

def nothing():
    pass

cam = cv2.VideoCapture(CAMERA_ID)
if cam.isOpened() == False:
    print("cannot open Cam-%d" % (CAMERA_ID))
    exit()


cv2.namedWindow("CAM window")

cv2.createTrackbar("blur", "CAM window", 1, 40, nothing)

cv2.setTrackbarPos("blur", "CAM window", 1)

img = np.zeros((512, 512, 3), np.uint8)

while True:
    ret, frame = cam.read()
    blurVal = cv2.getTrackbarPos("blur", "CAM window")

    res = cv2.GaussianBlur(frame, (blurVal, blurVal), 0)

    cv2.imshow("CAM window", res)

    if(cv2.waitKey(10) > 0): 
        cam.release()
        exit()

