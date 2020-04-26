'''
    开闭操作  open and close
    基于膨胀操作的 形态学操作   开操作 = 腐蚀 + 膨胀 ， 输入图片 +  结构元素
    开操作作用   用于消除图片小的  干扰区域  尽量保留别的图形结果
    闭操作  = 膨胀 + 腐蚀  ，输入图片  +  结构元素
    闭操作作用   填充小的封闭区域  填充小黑点
    开操作很重要啊  MORPH_RECT  cv.MORPH_ELLIPSE
'''

import cv2 as cv
import numpy as np

# 开操作  删除小的干扰块
def open_demo(img):
    print(img.shape)
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    cv.imshow("binary",binary)
    # 修改6*6 可以提取水平竖直的线 cv.MORPH_ELLIPSE 可用于保留 3*3以上的块区
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(3,3))
    dst = cv.morphologyEx(binary,cv.MORPH_OPEN,kernel)
    cv.imshow("dst",dst)

# 闭操作
def close_demo(img):
    print(img.shape)
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    cv.imshow("binary",binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(6,6))
    dst = cv.morphologyEx(binary,cv.MORPH_CLOSE,kernel)
    cv.imshow("dst",dst)

img = cv.imread("num2.jpg")
print('创建成功')
cv.imshow('ljw',img)
# close_demo(img)
open_demo(img)

cv.waitKey(0)
cv.destroyAllWindows()

