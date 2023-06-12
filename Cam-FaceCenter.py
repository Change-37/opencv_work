import numpy as np
import cv2
import matplotlib.pylab as plt

CAMERA_ID = 0

x1 = -1
y1 = -1
x2 = -1
y2 = -1
click1 = False
click2 = False

def nothing():
    pass

def mouseCallBack(event, x, y, flags, param):
    global x1, y1, x2, y2, click1, click2, frame
    if event is cv2.EVENT_LBUTTONDOWN:
        x1, y1 = x, y
        click1 = True
    elif event is cv2.EVENT_MOUSEMOVE:
        if click1:
            cv2.rectangle(frame, (x1, y1), (x, y), (0,0,255), 2)
    elif event is cv2.EVENT_LBUTTONUP:
        if click1:
            x2, y2 = x, y
            cv2.rectangle(frame, (x1,y1), (x2,y2), (0,0,255), 2)
            click2 = True
            print("click")

cam = cv2.VideoCapture(CAMERA_ID)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 540)
if cam.isOpened() == False:
    print("cannot open Cam-%d" % (CAMERA_ID))
    exit()

window = "CAM window"

cv2.namedWindow(window)
cv2.setMouseCallback(window, mouseCallBack)

# cv2.imshow(window, frame)
ret, frame = cam.read()
template = frame.copy()

while not click2:
    cv2.imshow(window, frame)

    if(cv2.waitKey(10) > 0): 
        cam.release()
        exit()

w = x2 - x1
h = y2 - y1
template2 = template[y1:y2, x1:x2]

cv2.namedWindow("template")
cv2.imshow("template", template2)

method = cv2.TM_CCORR_NORMED

while True:
    status, frame = cam.read()

    res = cv2.matchTemplate(frame, template2, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    top_left = max_loc
    bottom_right = max_loc[0]+w, max_loc[1]+h

    cv2.rectangle(frame, top_left, bottom_right, (0,0,255), 2)

    if status:
        cv2.imshow(window, frame)
    if(cv2.waitKey(10) > 0): 
        cam.release()
        exit()
