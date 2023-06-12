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

img = np.zeros((512, 512, 3), np.uint8)

while True:
    ret, frame = cam.read()

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(frame, 1.1, 3)
    res = frame
    for (x, y, w, h) in faces:
        cv2.rectangle(res, (x,y), (x+w, y+h), (255,0,0), 2)

    cv2.imshow("CAM window", res)

    if(cv2.waitKey(10) > 0): 
        cam.release()
        exit()

