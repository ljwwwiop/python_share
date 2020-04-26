'''
    其他形态学操作
    顶帽  是开操作图象与原图像的差值图
    黑帽  是闭操作。。。
    形态学梯度  基本梯度 = 膨胀后的图象 - 腐蚀后的图象  得到的差值图象
    cv.MORPH_TOPHAT 顶帽方法   cv.MORPH_BLACKHAT  黑帽
    黑帽  可以取出图中的 亮点   顶帽 消除了图形凉块
'''
import cv2 as cv
import numpy as np

def hat_demo(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))
    dst = cv.morphologyEx(gray,cv.MORPH_BLACKHAT,kernel)
    image = np.array(gray.shape,np.uint8)
    image = 100
    dst = cv.add(dst,image)
    cv.imshow("dst",dst)

def hat_ret_demo(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    cv.imshow("binary",binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dst = cv.morphologyEx(binary,cv.MORPH_BLACKHAT,kernel)
    cv.imshow("dst",dst)

# 形态学梯度
def hat_ti_demo(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    cv.imshow("binary",binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    dst = cv.morphologyEx(binary,cv.MORPH_GRADIENT,kernel)
    cv.imshow("dst",dst)

# 内外梯度
def gradient_demo(img):
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    dm = cv.dilate(img,kernel)
    em = cv.erode(img,kernel)
    dst1 = cv.subtract(img,em) # internal gradient
    dst2 = cv.subtract(dm,img) # external gradient
    cv.imshow("internal",dst1)
    cv.imshow("external",dst2)

img = cv.imread("yuan.jpg")
print('创建成功')
cv.imshow('ljw',img)
gradient_demo(img)

cv.waitKey(0)
cv.destroyAllWindows()

