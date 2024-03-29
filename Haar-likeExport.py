import numpy as np
import cv2
from matplotlib import pyplot as plt

img1_src = cv2.imread("images/img_6_6.jpg", cv2.IMREAD_GRAYSCALE)
img1 = cv2.resize(img1_src, (320,240))

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(img1, 1.1, 3)
res1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
for (x, y, w, h) in faces:
    cv2.rectangle(res1, (x,y), (x+w, y+h), (255,0,0), 2)

faces2 = face_cascade.detectMultiScale(img1, 1.5, 3)
res2 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
for (x, y, w, h) in faces2:
    cv2.rectangle(res2, (x,y), (x+w, y+h), (255,0,0), 2)

display = [("input1", img1), ("res1", res1), ("res2", res2)]
for (name, out) in display:
    cv2.imshow(name, out)

cv2.waitKey(0)
cv2.destroyAllWindows()
