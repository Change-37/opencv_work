import cv2 as cv
from matplotlib import pyplot as plt

img1 = cv.imread('images/20230403_14.jpg')
img2 = cv.imread('images/20230403_15.jpg')

img3 = cv.subtract(img1, img2)
img4 = cv.absdiff(img1, img2)

title = ['src', 'map', 'sub', 'abs']
imgs = [img1, img2, img3, img4]

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(imgs[i])
    plt.title(title[i])
    plt.xticks([])
    plt.yticks([])
plt.show()