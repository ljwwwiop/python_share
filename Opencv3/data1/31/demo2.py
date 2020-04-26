'''
 2D 的直方图画法
 直方图反向投影 用于追踪
'''
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 反向投影 需要投影样本颜色 ，投影对象
def back_project():
    sample = cv.imread("")
    target = cv.imread("")
    roi_hsv = cv.cvtColor(sample,cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(sample,cv.COLOR_BGR2HSV)
    # show
    cv.imshow("sample",sample)
    cv.imshow("target",target)

    # 要想投影准确 [180,256]  可以进行密度缩小 [36,48]  这是直方图 [32,32]
    roiHist = cv.calcHist([roi_hsv],[0,1],None,[180,256],[0,180,0,256])
    cv.normalize(roiHist,roiHist,0,255,cv.NORM_MINMAX)
    dst = cv.calcBackProject([target_hsv],[0,1],roiHist,[0,180,0,256],1)
    # 1 不进行大小放缩
    cv.imshow("calcBackProject",dst)

def hist2D_demo(img):
    hsv = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    # 显示的更加精确 需要[180,256] 更改就可以了 [32,32]
    hist = cv.calcHist(hsv,[0,1],None,[32,32],[0,180,0,256])
    plt.imshow(hist,interpolation='nearest')
    plt.title("2D Histogram")
    plt.show()

img = cv.imread("timg (1).jpg")
print('创建成功')
cv.imshow('ljw',img)
hist2D_demo(img)
cv.waitKey(0)
cv.destroyAllWindows()










