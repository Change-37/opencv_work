import cv2 as cv
import sys

img = cv.imread("toki.png")
if img is None:
    sys.exit("Could not read image.")

cv.imshow("Dicplay window", img)

k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("toki2.png", img)