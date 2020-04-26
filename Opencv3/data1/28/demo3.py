'''
    EPF 边缘保留滤波
    高斯双边  均值迁移   操作
    美颜操作
'''
import cv2 as cv
import numpy as np

# EPF  高斯
def bi_demo(image):
    dst = cv.bilateralFilter(image,0,100,15)
    cv.imshow("demo",dst)
    # sigmaspace 越小越好 sigmacolor 颜色差异 大一点 d默认0

# 均值迁移 油画风格
def shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(image,10,30)
    # 空间的 sigma的
    cv.imshow("demo2", dst)

img = cv.imread("man.jpg")
print('创建成功')
cv.imshow('ljw',img)
shift_demo(img)

cv.waitKey(0)
cv.destroyAllWindows()