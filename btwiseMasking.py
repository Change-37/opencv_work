import cv2 as cv
import numpy as np
import matplotlib.pylab as plt

img = cv.imread('images/img12.jpg')

mask = np.zeros_like(img)
cv.circle(mask, (260,210), 100, (255,255,255), -1)

masked = cv.bitwise_and(img, mask)

images = [img, mask, masked]
for i in range(3):
    plt.subplot(2, 2, i+1),plt.imshow(images[i])
    plt.xticks([]),plt.yticks([])
plt.show()