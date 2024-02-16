import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('images/img_car_3.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file couldn't be read"

# img = cv.medianBlur(img, 5)

ret, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

images = [img, th1, th2, th3]
for i in range(4):
    plt.subplot(2, 2, i+1),plt.imshow(images[i], 'gray')
    plt.xticks([]),plt.yticks([])
plt.show()