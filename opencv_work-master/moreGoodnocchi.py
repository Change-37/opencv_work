import cv2 as cv
from matplotlib import pyplot as plt

# img1 = cv.imread('images/20230331_1.jpg')
# img2 = cv.imread('images/20230331_2.jpg')

# mask = cv.subtract(img1, img2)
# cv.imwrite("images/mask.png", mask)
# img3 = cv.imread("images/mask.png", cv.IMREAD_GRAYSCALE)
# img4 = cv.adaptiveThreshold(img3, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

# img5 = cv.bitwise_and(img1, img4)

# title = ['src', 'map', 'sub', 'mask']
# imgs = [img1, img2, img4, img5]

# for i in range(4):
#     plt.subplot(2,2,i+1)
#     plt.imshow(imgs[i])
#     plt.title(title[i])
#     plt.xticks([])
#     plt.yticks([])
# plt.show()

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