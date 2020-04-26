'''
    膨胀 与 腐蚀  图象形态学  数学集合论发展的分支
    膨胀作用   对象大小增加一个象素   平滑对象边缘   减少或填充对象之间的距离
    腐蚀作用   对象大小减少1个象素    平滑对象边缘   增大距离 弱化或分割图象之间连接
    膨胀 ---彩色图片 变亮   腐蚀  ---彩色图片  变暗
'''


import cv2 as cv
import numpy as np

# 腐蚀   如果不取反  则会膨胀
def erode_demo(img):
    print(img.shape)
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV|cv.THRESH_OTSU)
    # 腐蚀算子 3*3规格腐蚀  可以调整
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(6,6))
    dst = cv.erode(binary,kernel)
    cv.imshow("dst",dst)

# 膨胀  如果不取反  则会腐蚀
def dilate_demo(img):
    print(img.shape)
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV|cv.THRESH_OTSU)
    # 腐蚀算子 3*3规格腐蚀  可以调整
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(6,6))
    dst = cv.dilate(binary,kernel)
    cv.imshow("dst",dst)

img = cv.imread("timg (1).jpg")
print('创建成功')
cv.imshow('ljw',img)
# dilate_demo(img)
kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
dst = cv.erode(img, kernel)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()









