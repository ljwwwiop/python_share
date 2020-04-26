'''
    模糊操作 -- 实际是卷积离散
    卷积原理  均值模糊 中值模糊  自定义模糊
'''

import cv2 as cv
import numpy as np

# 均值模糊
def blur_demo(image):
    dst = cv.blur(image,(5,2))
    cv.imshow("blur_demo",dst)

# 去除 椒盐  点
def median_blur_demo(image):
    dst = cv.medianBlur(image,5)
    cv.imshow("blur_demo",dst)

def custom_blur_demo(image):
    # 算子
    # kernel = np.ones([5,5],np.float32)/25
    kernel = np.array([[0,1,1],[-1,-1,0],[0,1,0]],np.float32)/9
    dst = cv.filter2D(image,-1,kernel=kernel)
    cv.imshow("custom_blur_demo",dst)

img = cv.imread("timg (1).jpg")
print('创建成功')
cv.imshow('ljw',img)
custom_blur_demo(img)
cv.waitKey(0)
cv.destroyAllWindows()




