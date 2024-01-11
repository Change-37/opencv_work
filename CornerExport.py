import numpy as np
import cv2
from matplotlib import pyplot as plt

img1_src = cv2.imread("images/img_6_4.png", cv2.IMREAD_GRAYSCALE)
img1 = cv2.resize(img1_src, (320,240))

dst = cv2.cornerHarris(img1, 2, 3, 0.06)
dst = cv2.dilate(dst, None)
res1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
res1[dst>0.1*dst.max()] = [0,0,255]

dst2 = cv2.cornerHarris(img1, 5, 3, 0.06)
dst2 = cv2.dilate(dst, None)
res2 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
res2[dst2>0.1*dst2.max()] = [0,0,255]

display = [("input1", img1), ("res1", res1), ("res2", res2)]
for (name, out) in display:
    cv2.imshow(name, out)

cv2.waitKey(0)
cv2.destroyAllWindows()