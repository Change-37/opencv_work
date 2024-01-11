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

cv2.createTrackbar("strength", "CAM window", 1, 10, nothing)

cv2.setTrackbarPos("strength", "CAM window", 1)

img = np.zeros((512, 512, 3), np.uint8)

while True:
    ret, frame = cam.read()
    blurVal = cv2.getTrackbarPos("strength", "CAM window")

    if(cv2.waitKey('o')):
        res = frame

    if(cv2.waitKey('s')):
        res = cv2.Sobel(frame, cv2.FILTER_SCHARR, blurVal/10, 1-(blurVal/10), ksize=3)

    if(cv2.waitKey('c')):
        res = cv2.Scharr(frame, cv2.CV_32FC1, blurVal/10, 1-(blurVal/10))
    
    if(cv2.waitKey('l')):
        res = cv2.Laplacian(frame, cv2.CV_32FC1, ksize=blurVal)

    cv2.imshow("CAM window", res)

    if(cv2.waitKey(10) > 0): 
        cam.release()
        exit()

