import numpy as np
import cv2
from matplotlib import pyplot as plt

srcs = []
dsts = []
img1 = cv2.imread("images/road.jpg", cv2.IMREAD_GRAYSCALE)

def averaging(srcs):
    x1 = (srcs[0][0]+srcs[2][0])/2
    x2 = (srcs[1][0]+srcs[3][0])/2
    y1 = (srcs[0][1]+srcs[1][1])/2
    y2 = (srcs[2][1]+srcs[3][1])/2
    dsts = []
    dsts.append([x1, y1])
    dsts.append([x2, y1])
    dsts.append([x1, y2])
    dsts.append([x2, y2])
    return dsts

def onMouse(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        srcs.append([x,y])
        print(srcs)
        if len(srcs) >= 4:
            h, w = img1.shape
            point1_src = np.float32(srcs)
            print(averaging(srcs))
            point1_dst = np.float32(averaging(srcs))
            per_mat1 = cv2.getPerspectiveTransform(point1_src, point1_dst)
            res1 = cv2.warpPerspective(img1, per_mat1, (w, h))
            plt.subplot(2, 2, 1)
            plt.imshow(res1, cmap="gray")
            plt.xticks([]), plt.yticks([])
            plt.show()
            srcs.clear()
    
    if event == cv2.EVENT_RBUTTONDOWN:
        srcs.clear()


# h, w = img1.shape
# point1_src = np.float32([[260,120], [410,120], [110,480], [560,480]])
# point1_dst = np.float32([[110,120], [560,120], [110,480], [560,480]])
# per_mat1 = cv2.getPerspectiveTransform(point1_src, point1_dst)
# res1 = cv2.warpPerspective(img1, per_mat1, (w, h))


# ress = []
# ress.append(img1)
# ress.append(res1)

# for i in range(2):
#     plt.subplot(2,2,i+1)
#     plt.imshow(ress[i], cmap='gray')
#     plt.xticks([]), plt.yticks([])
# plt.show()

cv2.imshow("image", img1)
cv2.setMouseCallback("image", onMouse)
cv2.waitKey()
