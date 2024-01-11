import cv2 as cv

img = cv.imread('toki.png')
cv.imshow('toki', img)
cv.waitKey(0)
cv.destroyAllWindows()